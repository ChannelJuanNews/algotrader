import order
import stock


class Application:
    def __init__(self, paper=True):
        self.trades = []  # list of trades the application has made so far
        self.stocks = []  # list of stocks the application is holding so far
        self.paper = paper
