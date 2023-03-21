"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item_1():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item_1):
    assert Item.calculate_total_price == 200000.00


def test_apply_discount(item_1):
    assert Item.apply_discount == 8500.0
