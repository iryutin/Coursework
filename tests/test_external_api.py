from unittest.mock import patch

from src.external_api import currency_conversion, stock_prices


@patch("requests.request")
def test_currency_conversion(mock_recvest, conversion_data_out):
    """Тест функции currency_conversion"""
    mock_recvest.return_value.json.return_value = conversion_data_out
    assert currency_conversion("USD") == 100.0


@patch("requests.get")
def test_stock_prices(mock_recvest, stock_prices_data_out):
    """Тест функции stock_prices"""
    mock_recvest.return_value.json.return_value = {"data": [{"close": 100, "open": 20}, {"s": 1}]}
    assert stock_prices("test_symbol") == 100.0
