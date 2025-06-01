import pytest
from storage import store_receipt, get_receipt
from processor import calculate_points
from models import Receipt, Item
from datetime import date, time
from pydantic import ValidationError


def test_amazon_17pts():
    receipt = Receipt(
        retailer = "Amazon",
        purchaseDate = date(2025, 5, 29),
        purchaseTime = time(21, 6),
        items = [
            Item(shortDescription = "Bobbie Organic Gentle Baby Formula", price = "29.99"),
            Item(shortDescription = "Pat the Bunny", price = "16.81")
        ],
        total = "46.80"
    )
    assert calculate_points(receipt) == 17
    
def test_amazon_23pts():
    receipt = Receipt(
        retailer = "Amazon",
        purchaseDate = date(2025, 5, 29),
        purchaseTime = time(21, 6),
        items = [
            Item(shortDescription = (
                "Bobbie Organic Gentle Baby Formula Milk Based Powder with "
                "Iron DHA Vitamin D Lactose Like Breast Milk For Fusiness Crying Digestive Health "
                "Newborn Baby 12 Months Old"
            ), price = "29.99"),
            Item(shortDescription = "Pat the Bunny", price = "16.81")
        ],
        total = "46.80"
    )
    assert calculate_points(receipt) == 23

def test_westelm_113pts():
    receipt = Receipt(
        retailer = "West Elm",
        purchaseDate = date(2025, 5, 25),
        purchaseTime = time(14, 30),
        items = [
            Item(shortDescription = "AAA", price = "25.00"),
            Item(shortDescription = "BBB", price = "25.00")
        ],
        total="50.00"
    )
    assert calculate_points(receipt) == 113

def test_zero_point_case():
    receipt = Receipt(
        retailer = "--",
        purchaseDate = date(2025, 4, 2),
        purchaseTime = time(11, 0),
        items = [
            Item(shortDescription="A", price = "9.37")
        ],
        total = "0.02"
    )
    assert calculate_points(receipt) == 0

    # my own method's test - retrieve receipt data from ID
    receipt_id = store_receipt(0, receipt.model_dump()) 
    restored = get_receipt(receipt_id)
    assert restored == receipt.model_dump() 
    

def test_missing_total():
    with pytest.raises(ValidationError):
        Receipt(
            retailer = "Amazon",
            purchaseDate = date(2025, 5, 29),
            purchaseTime = time(21, 6),
            items = [
                Item(shortDescription="Item A", price = "9.99")
            ]
            # missing total
        )

def test_invalid_desc():
    with pytest.raises(ValidationError):
        Receipt(
            retailer = "Amazon",
            purchaseDate = date(2025, 5, 29),
            purchaseTime = time(21, 6),
            items = [
                # invalid desc
                Item(shortDescription = "B#(@*%&!(!)a", price  = "29.99"),
                Item(shortDescription = "          ", price = "16.81" )
            ],
            total = "46.80"
        )
            