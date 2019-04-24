import pytest

from imaginary_number.imaginary_number import PurelyImaginaryNumber


@pytest.mark.parametrize("num, expected", [
        (2, "2i"),
        (-2, "-2i"),
    ])
def test_stringify(num, expected):
    purely_imaginary_number = PurelyImaginaryNumber(num)
    assert expected==str(purely_imaginary_number)
