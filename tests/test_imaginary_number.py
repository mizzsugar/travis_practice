from imaginary_number.imaginary_number import PurelyImaginaryNumber


def test_stringify():
    purely_imaginary_number = PurelyImaginaryNumber(2)
    assert '2i'==str(purely_imaginary_number)
