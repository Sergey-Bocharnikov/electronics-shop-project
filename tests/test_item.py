"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item_1():
    return Item("Смартфон", 10000, 20)


def test_items_init(item_1):
    assert item_1.name == "Смартфон"
    assert item_1.price == 10000
    assert item_1.quantity == 20


def test_calculate_total_price(item_1):
    assert item_1.calculate_total_price == 200000.0
