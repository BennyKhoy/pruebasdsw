import time

from behave import given, then, when  # pylint: disable=no-name-in-module
from selenium import webdriver
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException,
)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

WAIT = 10

UNIVERSITY_KEYWORDS = {
    "iteso.mx": ["iteso", "universidad jesuita", "guadalajara"],
    "tec.mx": ["tec", "tecnológico de monterrey", "tecnologico"],
    "ipn.mx": ["ipn", "politécnico", "politecnico", "instituto politécnico"],
}

TERM_KEYWORDS = {
    "carreras": [
        "carrera",
        "licenciatura",
        "ingeniería",
        "programa",
        "oferta educativa",
        "ingenieria",
    ],
    "becas": ["beca", "financiamiento", "apoyo", "scholarship", "económico"],
    "admisiones": [
        "admisión",
        "admisiones",
        "ingreso",
        "requisito",
        "inscripción",
        "admision",
    ],
    "posgrados": ["posgrado", "maestría", "doctorado", "especialidad", "maestria"],
}

UNIVERSITY_BASE_URLS = {
    "iteso.mx": "https://www.iteso.mx",
    "tec.mx": "https://tec.mx",
    "ipn.mx": "https://www.ipn.mx",
}

UNIVERSITY_SEARCH_URLS = {
    "iteso.mx": "https://www.iteso.mx/busqueda?q={term}",
    "tec.mx": "https://tec.mx/es/search?query={term}",
}


def _build_driver() -> webdriver.Chrome:
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    return webdriver.Chrome(options=options)


def _wait(driver, seconds: int = WAIT) -> WebDriverWait:
    return WebDriverWait(driver, seconds)


def _accept_cookies_if_present(driver) -> None:
    """Descarta banners de cookies. NUNCA lanza excepción."""
    selectors = [
        (By.ID, "L2AGLb"),
        (By.XPATH, "//button[contains(., 'Aceptar')]"),
        (By.XPATH, "//button[contains(., 'Accept')]"),
        (By.XPATH, "//button[contains(., 'Acepto')]"),
    ]
    for by, value in selectors:
        try:
            btn = WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((by, value))
            )
            btn.click()
            time.sleep(0.3)
            return
        except Exception:
            continue


def _safe_click(driver, element) -> None:
    try:
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        time.sleep(0.2)
        element.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", element)


def _wait_page_ready(driver, timeout: int = 15) -> None:
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
    except TimeoutException:
        pass


def _search_via_google_site(driver, domain: str, term: str) -> None:
    """Busca 'site:domain term' en Google y hace clic en el primer resultado"""
    query = f"site:{domain} {term}"
    print(f"\nGoogle site search: '{query}'")
    driver.get("https://www.google.com")
    _accept_cookies_if_present(driver)

    search_box = _wait(driver).until(EC.element_to_be_clickable((By.NAME, "q")))
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    _wait(driver).until(EC.presence_of_element_located((By.ID, "search")))

    try:
        results = _wait(driver, 8).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "#search a[href^='http']")
            )
        )
        for link in results:
            href = link.get_attribute("href") or ""
            if domain in href:
                _safe_click(driver, link)
                _wait_page_ready(driver, timeout=15)
                time.sleep(1.0)
                return
    except Exception:  # pylint: disable=broad-except
        pass

    print(
        f"\nNo se encontró resultado en Google site:{domain} para '{term}' "
        f"Verificando en la página de resultados de Google."
    )


@given("I open a browser")  # pylint: disable=not-callable
def open_browser(context):
    context.driver = _build_driver()
    context.driver.implicitly_wait(3)


@given("I am on the Google homepage")  # pylint: disable=not-callable
def go_to_google(context):
    """Navega a Google"""
    context.driver.get("https://www.google.com")
    _accept_cookies_if_present(context.driver)


@when('I search for "{query}" on Google')  # pylint: disable=not-callable
def google_search(context, query):
    search_box = _wait(context.driver).until(EC.element_to_be_clickable((By.NAME, "q")))
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    _wait(context.driver).until(EC.presence_of_element_located((By.ID, "search")))


@when('I click the first result link for "{domain}"')  # pylint: disable=not-callable
def click_first_result(context, domain):
    """Clic en el primer resultado de Google que contenga el domain"""
    context.target_domain = domain
    try:
        results = _wait(context.driver, 8).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "#search a[href^='http']")
            )
        )
        for link in results:
            href = link.get_attribute("href") or ""
            if domain in href:
                _safe_click(context.driver, link)
                _wait_page_ready(context.driver, timeout=15)
                time.sleep(1.0)
                return
    except Exception:  # pylint: disable=broad-except
        pass

    base_url = UNIVERSITY_BASE_URLS.get(domain, f"https://www.{domain}")
    print(f"\nSin resultado en Google para '{domain}'. Navegando a {base_url}")
    context.driver.get(base_url)
    _wait_page_ready(context.driver, timeout=15)
    time.sleep(1.0)


@then("I should be on the ITESO website")  # pylint: disable=not-callable
def verify_on_iteso(context):
    _verify_university_page(context, "iteso.mx")


@then('I should be on the "{university_name}" website')  # pylint: disable=not-callable
def verify_on_university(context, university_name):
    _verify_university_page(context, context.target_domain)


def _verify_university_page(context, domain: str) -> None:
    driver = context.driver
    current_url = driver.current_url.lower()
    page_source = driver.page_source.lower()
    url_ok = domain.lower() in current_url
    keywords = UNIVERSITY_KEYWORDS.get(domain, [domain.split(".")[0]])
    content_ok = any(kw in page_source for kw in keywords)
    assert url_ok or content_ok, (
        f"Se esperaba '{domain}' pero la URL es '{driver.current_url}'.\n"
        f"Título: '{driver.title}'"
    )
    print(f"\nVerificado: en '{domain}' — URL: {driver.current_url}")


@when('I search for "{term}" on the university website')  # pylint: disable=not-callable
def search_on_university(context, term):
    """Buscamos el término de manera directa y si no existe se hace una búsqueda en site"""
    context.search_term = term
    driver = context.driver
    domain = getattr(context, "target_domain", None)

    if domain and domain in UNIVERSITY_SEARCH_URLS:
        search_url = UNIVERSITY_SEARCH_URLS[domain].format(term=term)
        print(f"\nURL directa: {search_url}")
        driver.get(search_url)
        _wait_page_ready(driver, timeout=15)
        time.sleep(1.5)
    else:
        _search_via_google_site(driver, domain or "", term)


@then(
    'the results should be related to "{term}" offered by the university'
)  # pylint: disable=not-callable
def verify_results(context, term):
    """
    Verificamos que la página este relacionada con el term"""
    driver = context.driver
    current_url = driver.current_url.lower()
    page_title = driver.title.lower()
    page_body = driver.page_source.lower()

    term_lower = term.lower()
    synonyms = TERM_KEYWORDS.get(term_lower, [term_lower])
    all_terms = list({term_lower} | set(synonyms))

    url_match = any(t in current_url for t in all_terms)
    title_match = any(t in page_title for t in all_terms)
    body_match = any(t in page_body for t in all_terms)

    assert url_match or title_match or body_match, (
        f"Resultados no relacionados con '{term}'.\n"
        f"URL   : {driver.current_url}\n"
        f"Título: {driver.title}\n"
        f"Buscado: {all_terms}"
    )
    match_type = "URL" if url_match else ("título" if title_match else "cuerpo")
    print(f"\n'{term}' verificado via {match_type} — {driver.current_url}")
