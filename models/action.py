class Action:
    """"""

    def __init__(self, name, price, profitPerCent) -> None:
        self.name = name
        self.price = int(price)
        self.profitPerCent = int(profitPerCent)

    @property
    def profitEuro(self):
        profit = (self.profitPerCent / 100) * self.price
        return profit
