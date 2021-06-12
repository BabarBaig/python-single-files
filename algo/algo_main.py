""" print() format: Condition ? Action """

import sys

class Counter():
    def __init__(self, start=0):
        self.counter: int = start

    def get(self) -> int:
        """ Return next value of counter """
        self.counter += 1
        return self.counter

    def reset(self) -> int:
        self.counter = 0
        return self.counter


class Algo():
    def __init__(self):
        self.count = Counter()

    def __once(self):
        """ Call once per session """
        self.count.reset()
        print()
        # print(f"[{self.count.get()}] HIGHLY DISPURPTIVE IDEA: The higher the balance, the higher " +
                # "the % gain it should show.  Balance & Gain should be linearly related.")
        # print(f"[{self.count.get()}] Check today's biggest gainers & decliners")
        print(f"[{self.count.get()}] Run MStar mo3 ETF Quickrank [https://www.morningstar.com/etfs/screener-rank]")
        print(f"[{self.count.get()}] Stocks can have good/bad entry points.  See y1 chart to decide.")
        print(f"[{self.count.get()}] Souring on unknown stocks b/c of time and unpredictability.")
        print(f"[{self.count.get()}] Build large balances ONLY if SD/Return > 1")
        print(f"[{self.count.get()}] Wait a week before buying more.")
        print(f"[{self.count.get()}] Recent momentum [MOON MRNA SFYF SPXL]")

    def ind441(self):
        self.count.reset()
        print('[Ind441] *********')
        print(f'[{self.count.get()}] Sell SCHP SCHR SPIT VGIT to $1000 > AOM in trades of $2k daily.')
        print(f'[{self.count.get()}] Cash to $10,000 > Excess cash > AOM in trades of $2k daily.')
        print(f'[{self.count.get()}] Check open orders.  Push BUYs')
        print(f'[{self.count.get()}] Check cash')
        print(f'[{self.count.get()}] Check ModAlloc')
        print(f'[{self.count.get()}] Consider buying $LoBal')
        print(f"[{self.count.get()}] MaxBal > $15k ? Trim.")
        print(f'[{self.count.get()}] Check positions with greatest % gain/loss')
        print(f"[{self.count.get()}] Check today's biggest decliners and gainers")

    def roth089(self):
        self.count.reset()
        print('[Roth089] *********')
        print(f'[{self.count.get()}] Check open orders.  Push BUYs')
        print(f'[{self.count.get()}] Check cash')
        print(f'[{self.count.get()}] Check ModAlloc')
        print(f'[{self.count.get()}] Consider buying $LoBal')
        print(f"[{self.count.get()}] MaxBal > $15k ? Trim.")

    def roll128(self):
        self.count.reset()
        print('[Roll128] *********')
        print(f'[{self.count.get()}] Check open orders.  Push BUYs')
        print(f'[{self.count.get()}] Check cash')
        print(f'[{self.count.get()}] Check ModAlloc')
        print(f'[{self.count.get()}] Consider buying $LoBal')

    def utma611(self):
        self.count.reset()
        print('[UTMA611] *********')
        print(f'[{self.count.get()}] Check open orders.  Push BUYs')
        print(f'[{self.count.get()}] Check cash')
        print(f'[{self.count.get()}] Check ModAlloc')
        print(f'[{self.count.get()}] Consider buying $LoBal')

    def jroll124(self):
        self.count.reset()
        print('[JRoll124] *********')
        print(f'[{self.count.get()}] Check open orders.  Push BUYs')
        print(f'[{self.count.get()}] Check cash')
        print(f'[{self.count.get()}] Check ModAlloc')
        print(f'[{self.count.get()}] Consider buying $LoBal')
        print(f"[{self.count.get()}] MaxBal > $7k ? Trim.")

    def jroth900(self):
        self.count.reset()
        print('[JRoth900] *********')
        print(f'[{self.count.get()}] Check open orders.  Push BUYs')
        print(f'[{self.count.get()}] Check cash')
        print(f'[{self.count.get()}] Check ModAlloc')
        print(f'[{self.count.get()}] Consider buying $LoBal')
        print(f"[{self.count.get()}] Cash is critically low!  No trading, except to build cash.")
        print(f"[{self.count.get()}] MaxBal > $4k ? Trim.")

    def jind668(self):
        self.count.reset()
        print('[JInd668] *********')
        print(f'[{self.count.get()}] Check open orders.  Push BUYs')
        print(f'[{self.count.get()}] Check cash')
        print(f'[{self.count.get()}] Check ModAlloc')
        print(f'[{self.count.get()}] Consider buying $LoBal')
        print(f"[{self.count.get()}] Bias against buying a position more than once/wk")

    def utma118(self):
        self.count.reset()
        print('[UTMA118] *********')
        print(f'[{self.count.get()}] Check open orders.  Push BUYs')
        print(f'[{self.count.get()}] Check cash')
        print(f'[{self.count.get()}] Check ModAlloc')
        print(f'[{self.count.get()}] Consider buying $LoBal')
        print(f"[{self.count.get()}] MaxBal > $1.5k ? Trim.")

    def run(self):
        """ Create a list of function pointers and call them in a loop """
        self.__once()
        # List of function pointers:
        accounts = [self.ind441, self.roth089, self.roll128, self.utma611, self.jroll124,
                self.jroth900, self.jind668, self.utma118]
        for account in accounts:
            if input(f'\n\n[{account.__name__}] ********* [(q)uit]\t') == 'q': sys.exit("Goodbye ...\n")
            account()
        print()


if __name__ == '__main__':
    algo = Algo()
    algo.run()
