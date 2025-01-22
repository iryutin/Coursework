import pytest


@pytest.fixture()
def conversion_data_out():
    return {
        "quotes": {"USDRUB": 100, "USDEUR": 1.278342, "USDGBP": 0.908019, "USDPLN": 3.731504},
        "source": "USD",
        "success": True,
        "timestamp": 1432400348,
    }


@pytest.fixture()
def stock_prices_data_out():
    return {
        "data": [
            {
                "open": 129.8,
                "high": 133.04,
                "low": 129.47,
                "close": 132.995,
                "volume": 106686703.0,
                "adj_high": 133.04,
                "adj_low": 129.47,
                "adj_close": 132.995,
                "adj_open": 129.8,
                "adj_volume": 106686703.0,
                "split_factor": 1.0,
                "dividend": 0.0,
                "symbol": "AAPL",
                "exchange": "XNAS",
                "date": "2021-04-09T00:00:00+0000",
            },
        ]
    }


@pytest.fixture()
def test_dataframe():
    return {
        "Дата операции": ["18.01.2025 14:11:38", "17.01.2025 11:03:49"],
        "Номер карты": ["*0473", "*8164"],
        "Сумма операции": [-2570, -3973],
        "Кэшбэк": [0, 10],
        "Категория": ["Фастфуд", "123"],
    }
