# -*- coding: utf-8 -*-
"""
Test Driven Development (TDD) exercises.
"""

PRODUCTS = {
    "12345": 7.25,
    "23456": 12.50,
}


def scan(barcode):
    """
    Kata 5 - Point of Sale kata
    Create a simple app for scanning bar codes to sell products.

    Requirements
    1. Barcode '12345' should display price '$7.25'
    2. Barcode '23456' should display price '$12.50'
    3. Barcode '99999' should display 'Error: barcode not found'
    4. Empty barcode should display 'Error: empty barcode'
    5. Introduce a concept of total command where it is possible to scan multiple items.
       The command would display the sum of the scanned product prices.
    """
    if not barcode:
        return "Error: empty barcode"
    if barcode == "total":
        return "Error: no items scanned"
    if barcode not in PRODUCTS:
        return "Error: barcode not found"
    return f"${PRODUCTS[barcode]:.2f}"


def total(barcodes):
    """
    Returns the total price of all scanned barcodes.
    Ignores invalid or empty barcodes in the sum.
    """
    running_total = 0.0
    for barcode in barcodes:
        if barcode in PRODUCTS:
            running_total += PRODUCTS[barcode]
    return f"${running_total:.2f}"
