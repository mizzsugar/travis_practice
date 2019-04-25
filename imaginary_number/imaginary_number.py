from dataclasses import dataclass


@dataclass
class PurelyImaginaryNumber:
    num: int

    def __str__(self):
        return f'{self.num}i'
