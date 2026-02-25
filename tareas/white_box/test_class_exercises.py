# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    authenticate_user,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_quantity_discount,
    calculate_shipping_cost,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_file_size,
    check_flight_eligibility,
    check_loan_eligibility,
    check_number_status,
    divide,
    get_grade,
    get_weather_advisory,
    grade_quiz,
    is_even,
    is_triangle,
    validate_credit_card,
    validate_date,
    validate_email,
    validate_login,
    validate_password,
    validate_url,
    verify_age,
)


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))

    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)

    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when C is greater or equal than A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """
        Checks the three inputs can't form a triangle when B is greater or equal than A + C.
        """
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """
        Checks the three inputs can't form a triangle when A is greater or equal than B + C.
        """
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")

    # 1
    def test_check_number_status_positive(self):
        self.assertEqual(check_number_status(7), "Positive")

    def test_check_number_status_negative(self):
        self.assertEqual(check_number_status(-3), "Negative")

    def test_check_number_status_zero(self):
        self.assertEqual(check_number_status(0), "Zero")

    # 2
    def test_validate_password_valid(self):
        self.assertTrue(validate_password("Valid122!"))

    def test_validate_password_too_short(self):
        self.assertFalse(validate_password("Val1!"))

    def test_validate_password_no_upper(self):
        self.assertFalse(validate_password("valid122!"))

    def test_validate_password_no_lower(self):
        self.assertFalse(validate_password("VALID122!"))

    def test_validate_password_no_digit(self):
        self.assertFalse(validate_password("Validpass!"))

    def test_validate_password_no_special(self):
        self.assertFalse(validate_password("ValidPass122"))

    # 3
    def test_calculate_total_discount_none(self):
        self.assertEqual(calculate_total_discount(99), 0)

    def test_calculate_total_discount_ten_percent(self):
        self.assertEqual(calculate_total_discount(100), 10)
        self.assertEqual(calculate_total_discount(500), 50)

    def test_calculate_total_discount_twenty_percent(self):
        self.assertEqual(calculate_total_discount(501), 100.2)

    # 4
    def test_calculate_order_total_discounts(self):
        items = [
            {"price": 10, "quantity": 2},  # Sin descuento: 20
            {"price": 10, "quantity": 8},  # 5% descuento: 76
            {"price": 10, "quantity": 12},  # 10% descuento: 108
        ]
        # 20 + 76 + 108 = 204
        self.assertEqual(calculate_order_total(items), 204)

    # 5
    def test_shipping_standard(self):
        self.assertEqual(calculate_items_shipping_cost([{"weight": 5}], "standard"), 10)
        self.assertEqual(
            calculate_items_shipping_cost([{"weight": 10}], "standard"), 15
        )
        self.assertEqual(
            calculate_items_shipping_cost([{"weight": 11}], "standard"), 20
        )

    def test_shipping_express(self):
        self.assertEqual(calculate_items_shipping_cost([{"weight": 5}], "express"), 20)
        self.assertEqual(calculate_items_shipping_cost([{"weight": 10}], "express"), 30)
        self.assertEqual(calculate_items_shipping_cost([{"weight": 11}], "express"), 40)

    def test_shipping_invalid_method(self):
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost([{"weight": 5}], "same-day")

    # 6
    def test_validate_login_success(self):
        self.assertEqual(validate_login("user123", "password123"), "Login Successful")

    def test_validate_login_short_username(self):
        self.assertEqual(validate_login("alex", "password123"), "Login Failed")

    def test_validate_login_short_password(self):
        self.assertEqual(validate_login("user123", "123"), "Login Failed")

    # 7
    def test_verify_age_eligible(self):
        self.assertEqual(verify_age(18), "Eligible")
        self.assertEqual(verify_age(35), "Eligible")
        self.assertEqual(verify_age(65), "Eligible")

    def test_verify_age_not_eligible(self):
        self.assertEqual(verify_age(17), "Not Eligible")
        self.assertEqual(verify_age(66), "Not Eligible")

    # 8
    def test_categorize_product_a(self):
        self.assertEqual(categorize_product(25), "Category A")

    def test_categorize_product_b(self):
        self.assertEqual(categorize_product(75), "Category B")

    def test_categorize_product_c(self):
        self.assertEqual(categorize_product(150), "Category C")

    def test_categorize_product_d(self):
        self.assertEqual(categorize_product(9), "Category D")
        self.assertEqual(categorize_product(201), "Category D")

    # 9
    def test_validate_email_valid(self):
        self.assertEqual(validate_email("benja@mail.com"), "Valid Email")

    def test_validate_email_too_short(self):
        self.assertEqual(validate_email("a@b."), "Invalid Email")

    def test_validate_email_missing_at(self):
        self.assertEqual(validate_email("benjamail.com"), "Invalid Email")

    def test_validate_email_missing_dot(self):
        self.assertEqual(validate_email("benja@mailcom"), "Invalid Email")

    # 10
    def test_celsius_to_fahrenheit_valid(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_celsius_to_fahrenheit_invalid_lower(self):
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")

    def test_celsius_to_fahrenheit_invalid_upper(self):
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")

    # 11
    def test_validate_credit_card_valid(self):
        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card")
        self.assertEqual(validate_credit_card("1234567890123456"), "Valid Card")

    def test_validate_credit_card_invalid_length_short(self):
        self.assertEqual(validate_credit_card("1234567890"), "Invalid Card")

    def test_validate_credit_card_invalid_length_long(self):
        self.assertEqual(validate_credit_card("12345678901234567"), "Invalid Card")

    def test_validate_credit_card_non_digits(self):
        self.assertEqual(validate_credit_card("1234567890123a"), "Invalid Card")

    # 12
    def test_validate_date_valid(self):
        self.assertEqual(validate_date(2024, 12, 31), "Valid Date")
        self.assertEqual(validate_date(1900, 1, 1), "Valid Date")

    def test_validate_date_invalid_year_past(self):
        self.assertEqual(validate_date(1899, 5, 10), "Invalid Date")

    def test_validate_date_invalid_year_future(self):
        self.assertEqual(validate_date(2101, 5, 10), "Invalid Date")

    def test_validate_date_invalid_month_past(self):
        self.assertEqual(validate_date(2020, 0, 10), "Invalid Date")

    def test_validate_date_invalid_month_future(self):
        self.assertEqual(validate_date(2020, 13, 10), "Invalid Date")

    def test_validate_date_invalid_day(self):
        self.assertEqual(validate_date(2020, 5, 32), "Invalid Date")

    # 13
    def test_check_flight_eligibility_by_age(self):
        self.assertEqual(check_flight_eligibility(25, False), "Eligible to Book")

    def test_check_flight_eligibility_by_status(self):
        self.assertEqual(check_flight_eligibility(17, True), "Eligible to Book")
        self.assertEqual(check_flight_eligibility(70, True), "Eligible to Book")

    def test_check_flight_eligibility_denied(self):
        self.assertEqual(check_flight_eligibility(15, False), "Not Eligible to Book")

    # 14
    def test_validate_url_http(self):
        self.assertEqual(validate_url("http://google.com"), "Valid URL")

    def test_validate_url_https(self):
        self.assertEqual(validate_url("https://google.com"), "Valid URL")

    def test_validate_url_invalid_protocol(self):
        self.assertEqual(validate_url("mov://files.com"), "Invalid URL")

    def test_validate_url_too_long(self):
        self.assertEqual(validate_url("http://" + "a" * 250 + ".com"), "Invalid URL")

    # 15
    def test_calculate_quantity_discount_none(self):
        self.assertEqual(calculate_quantity_discount(1), "No Discount")
        self.assertEqual(calculate_quantity_discount(5), "No Discount")

    def test_calculate_quantity_discount_five_percent(self):
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")

    def test_calculate_quantity_discount_ten_percent(self):
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")

    # 16
    def test_check_file_size_valid_min(self):
        self.assertEqual(check_file_size(0), "Valid File Size")

    def test_check_file_size_valid_max(self):
        self.assertEqual(check_file_size(1048576), "Valid File Size")

    def test_check_file_size_invalid(self):
        self.assertEqual(check_file_size(1048577), "Invalid File Size")

    # 17
    def test_loan_not_eligible_low_income(self):
        self.assertEqual(check_loan_eligibility(25000, 800), "Not Eligible")

    def test_loan_secured_mid_income_low_score(self):
        self.assertEqual(check_loan_eligibility(45000, 650), "Secured Loan")

    def test_loan_standard_mid_income_high_score(self):
        self.assertEqual(check_loan_eligibility(45000, 750), "Standard Loan")

    def test_loan_premium_high_income_high_score(self):
        self.assertEqual(check_loan_eligibility(70000, 800), "Premium Loan")

    def test_loan_premium_low_income_high_score(self):
        self.assertEqual(check_loan_eligibility(10000, 800), "Not Eligible")

    def test_loan_standard_high_income_low_score(self):
        self.assertEqual(check_loan_eligibility(70000, 700), "Standard Loan")

    # 18
    def test_shipping_small_package(self):
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)

    def test_shipping_medium_package(self):
        self.assertEqual(calculate_shipping_cost(3, 20, 20, 20), 10)

    def test_shipping_large_package_by_weight(self):
        self.assertEqual(calculate_shipping_cost(6, 5, 5, 5), 20)

    def test_shipping_large_package_by_dimension(self):
        self.assertEqual(calculate_shipping_cost(0.5, 40, 10, 10), 20)

    # 19
    def test_grade_quiz_pass(self):
        self.assertEqual(grade_quiz(7, 2), "Pass")

    def test_grade_quiz_fail(self):
        self.assertEqual(grade_quiz(4, 4), "Fail")

    def test_grade_quiz_fail_2(self):
        self.assertEqual(grade_quiz(7, 4), "Fail")

    def test_grade_quiz_fail_3(self):
        self.assertEqual(grade_quiz(3, 2), "Fail")

    def test_grade_quiz_conditional(self):
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")

    # 20
    def test_auth_admin_success(self):
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_auth_user_success(self):
        self.assertEqual(authenticate_user("regularUser", "password123"), "User")

    def test_auth_invalid_short(self):
        self.assertEqual(authenticate_user("benja", "123"), "Invalid")

    # 21
    def test_weather_high_heat_humidity(self):
        self.assertEqual(
            get_weather_advisory(35, 80),
            "High Temperature and Humidity. Stay Hydrated.",
        )

    def test_weather_low_temp(self):
        self.assertEqual(get_weather_advisory(-5, 50), "Low Temperature. Bundle Up!")

    def test_weather_low_temp_2(self):
        self.assertEqual(get_weather_advisory(-1, 80), "Low Temperature. Bundle Up!")

    def test_weather_no_advisory(self):
        self.assertEqual(get_weather_advisory(40, 50), "No Specific Advisory")

    def test_weather_low_temp_low_humidity(self):
        self.assertEqual(get_weather_advisory(20, 50), "No Specific Advisory")
