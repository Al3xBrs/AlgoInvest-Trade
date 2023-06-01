class Action:
    """"""

    def __init__(self, name, price, profitEuro) -> None:
        self.name = name
        self.price = price
        self.profitEuro = profitEuro

    # @property
    # def profitEuro(self):
    #     profitfloat = (self.profitPerCent / 100) * self.price
    #     profit = profitfloat
    #     return profit
