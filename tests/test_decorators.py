import pandas as pd

from src.decorators import log


def test_log(capsys):
    @log()
    def callitka(x=True):
        if x is not True:
            raise TypeError("TypeError")
        else:
            return pd.DataFrame([])

    callitka()
    captured = capsys.readouterr()
    assert captured.out == "callitka ok\n{}\n"
    callitka(False)
    captured = capsys.readouterr()
    assert captured.out == "callitka error: TypeError. Inputs: (False,), {}\n"
