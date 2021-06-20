""" print() format: Condition ? Action """

import sys


class Algo():
    def __init__(self):
        self.__count = 0

    def count_get(self) -> int:
        """ Return next value of counter """
        self.__count += 1
        return self.__count

    def count_reset(self) -> int:
        self.__count = 0
        return self.__count

    def Print(self, msg: str) -> None:
        print(f"[{self.count_get()}]", msg)

    def __once(self):
        """ Call once per session """
        print()
        self.count_reset()
        self.Print('Run MStar mo3 ETF Quickrank [https://www.morningstar.com/etfs/screener-rank]')
        self.Print('Run Schwab screen Bob-a for y1 outperformers.')
        self.Print('Buy to $3100 (most a/c): FBGRX FCPVX')
        self.Print('Buy AOM/AOR $1k daily, to soak-up excess cash')
        # self.Print("Buy $LoBal if:\n\t"
        #         "1] % chg today is +ve\n\t"
        #         "2] Not bot > wk1.\n\t"
        #         "3] SMA20 > SMA200\n\t"
        #         "4] SMA20 > SMA20d1 [SMA20 has +ve slope]\n\t"
        #         "5] Stock: y3 > VOO, y5 > VOO.\n\t"
        #         "6] ETF: StdDev / Return > 1")
        self.Print("Momentum play: Buy [stocks/ETF/MF] that:\n\t"
                "1] Today's highest % gainer\n\t"
                "3] SMA20 > SMA200\n\t"
                "4] SMA20 > SMA20d1 [SMA20 has +ve slope]\n\t"
                "5] Stock: y3 > VOO, y5 > VOO.\n\t"
                "6] ETF: StdDev / Return > 1")

    def __frequent(self):
        """ Frequent messages """
        self.Print('Check cash.')
        self.Print('Check ModAlloc')
        self.Print('Push open BUYs.')

    def ind441(self):
        print('[Ind441] *********')
        self.__frequent()
        self.Print('Cash := $10k.  Excess>Buy AOM/AOR in trades of $1k daily.')
        self.Print("MaxBal > $15k ? Trim.")
        self.Print("Check Total gain/loss %.")
        self.Print('Check d1    gain/loss %.')

    def roth089(self):
        print('[Roth089] *********')
        self.__frequent()
        self.Print('MaxBal > $15k ? Trim.')

    def roll128(self):
        print('[Roll128] *********')
        self.__frequent()

    def utma611(self):
        print('[UTMA611] *********')
        self.__frequent()
        self.Print('MaxBal > $1100 ? Trim.')

    def jroll214(self):
        print('[JRoll214] *********')
        self.__frequent()
        self.Print('MaxBal > $7000 ? Trim.')

    def jroth900(self):
        print('[JRoth900] *********')
        self.__frequent()
        self.Print('Cash is critically low!  No trading, except to build cash.')
        self.Print('MaxBal > $4000 ? Trim.')

    def jind668(self):
        print('[JInd668] *********')
        self.__frequent()
        self.Print('Cash := $10k.  Excess > Buy AOM in trades of $4k daily.')
        self.Print('MaxBal > $7000 ? Trim.')

    def utma118(self):
        print('[UTMA118] *********')
        self.__frequent()
        self.Print('MaxBal > $1500 ? Trim.')

    def run(self):
        """ Create a list of function pointers and call them in a loop """
        self.__once()
        # List of function pointers:
        accounts = [self.ind441, self.roth089, self.roll128, self.utma611, self.jroll214,
                self.jroth900, self.jind668, self.utma118]
        for account in accounts:
            self.count_reset()
            if input(f'\n\n[{account.__name__}] ********* [(q)uit]\t') == 'q': sys.exit("Goodbye ...\n\n\n")
            account()
        print('\n')


if __name__ == '__main__':
    algo = Algo()
    algo.run()

        # self.Print("Monitor: Dimensional’s U.S. Equity ETF (DFUS), U.S. Small Cap ETF (DFAS), "
        #       "U.S. Core Equity 2 ETF (DFAC) and U.S. Targeted Value ETF (DFAT)")
        # self.Print("IDEA: Higher balance posn should show higher % gain, b/c I have more at "
        #       "stake.  Balance/Gain should be linearly related.")
        # self.Print("IDEA: Buy posn with largest gain/loss to push their total "
        #       "gain/loss towards some imaginary median.')
        # self.Print(Check today's biggest gainers & decliners")
        # self.Print("Stocks can have good/bad entry points.  See y1 chart to decide.\n\tSouring on "
        #       "unknown stocks b/c of time and unpredictability.")
