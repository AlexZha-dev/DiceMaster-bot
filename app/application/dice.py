from random import randint

class Dice:
    def roll(self, sides: int, num_rols: int = 1) -> list[int]:
        return [randint(1, sides) for _ in range(num_rols)]

    def sum_rols(self, rols: list[int]) -> int:
        return sum(rols)