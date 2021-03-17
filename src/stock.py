class Stock:
    """a self containing class that contains information and methods pertaining to a single stock """

    def __init__(self, ticker):
        self.ticker = ticker
        self.data = []

    def print(self):
        self.print = ""
