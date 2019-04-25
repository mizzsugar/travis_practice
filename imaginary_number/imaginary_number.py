from dataclasses import dataclass


@dataclass
class PurelyImaginaryNumber:
    num: int

    def __str__(self):
        if self.num == 1:
            return 'i'
        elif self.num == -1:
            return '-i'
        return f'{self.num}i'
