from models.action import Action


class Portfolio:
    def __init__(self, actions_list=[]) -> None:
        self.actions_list = actions_list

    @property
    def getPNL(self):
        pnlfloat = 0
        for action in self.actions_list:
            pnlfloat += float(action.profitEuro)

        pnl = round(pnlfloat, 2)

        return pnl

    @property
    def getFullActionsPrice(self):
        full_actions_pricefloat = 0
        for action in self.actions_list:
            full_actions_pricefloat += float(action.price)

        full_actions_price = round(full_actions_pricefloat, 2)
        return full_actions_price
