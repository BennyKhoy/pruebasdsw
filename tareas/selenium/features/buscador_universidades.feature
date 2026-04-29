Feature: University Website Search
  As a student exploring universities
  I want to search for academic programs on university websites
  So that I can find information about the careers they offer

  Background:
    Given I open a browser

  Scenario Outline: Search for academic terms on multiple university websites
    Given I am on the Google homepage
    When I search for "<university>" on Google
    And I click the first result link for "<domain>"
    Then I should be on the "<university_name>" website
    When I search for "<search_term>" on the university website
    Then the results should be related to "<search_term>" offered by the university

    Examples:
      | university           | domain   | university_name   | search_term |
      | iteso                | iteso.mx | ITESO             | carreras    |
      | iteso                | iteso.mx | ITESO             | becas       |
      | iteso                | iteso.mx | ITESO             | admisiones  |
      | tec monterrey        | tec.mx   | Tec de Monterrey  | carreras    |
      | tec monterrey        | tec.mx   | Tec de Monterrey  | becas       |
      | tec monterrey        | tec.mx   | Tec de Monterrey  | posgrados   |
      | IPN politecnico      | ipn.mx   | IPN               | carreras    |
      | IPN politecnico      | ipn.mx   | IPN               | becas       |
      | IPN politecnico      | ipn.mx   | IPN               | posgrados   |
