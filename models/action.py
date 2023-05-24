class Action:
    """"""

    def __init__(self, name, price, profitPerCent) -> None:
        self.name = name
        self.price = price
        self.profitPerCent = profitPerCent

    @property
    def profitEuro(self):
        profitfloat = (float(self.profitPerCent) / 100) * float(self.price)
        profit = round(profitfloat, 2)
        return profit
