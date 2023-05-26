import pytest
from statusbar import statusbar


def test_statusbar_arguments_validation():
    with pytest.raises(AssertionError):
        statusbar(tam=-1, total=10, correctas=5)
    with pytest.raises(AssertionError):
        statusbar(tam=81, total=10, correctas=5)
    with pytest.raises(AssertionError):
        statusbar(tam=50, total=-1, correctas=5)
    with pytest.raises(AssertionError):
        statusbar(tam=50, total=10, correctas=-1)
    with pytest.raises(AssertionError):
        statusbar(tam=50, total=10, correctas=11)


def test_statusbar_output():
    assert statusbar(tam=50, total=10, correctas=5) == "[=========================                         ] 50% SUCESS"
    assert statusbar(tam=50, total=10,
                     correctas=10) == "[==================================================] 100% SUCESS"
    assert statusbar(tam=50, total=10, correctas=0) == "[                                                  ] 0% SUCESS"
