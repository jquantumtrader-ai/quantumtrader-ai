from app.domain.common.financial_core.portfolio.assets import (
    Asset,
)


def test_asset_normalizes_symbol():

    asset = Asset(
        " petr4 "
    )

    assert asset.symbol == "PETR4"



def test_asset_string():

    asset = Asset(
        "vale3"
    )

    assert str(asset) == "VALE3"



def test_asset_empty_symbol_not_allowed():

    try:
        Asset("")

        assert False

    except ValueError:

        assert True
