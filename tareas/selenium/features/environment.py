def after_scenario(context, scenario):
    """Cierra el browser después de cada escenario, incluso si falló."""
    driver = getattr(context, "driver", None)
    if driver is not None:
        try:
            driver.quit()
        except Exception:  # pylint: disable=broad-except
            pass
        context.driver = None