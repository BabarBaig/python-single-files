""" print() format: Condition ? Action """

import sys

class Counter():
    def __init__(self, start=0):
        self.counter = start

    def get(self):
        """ Return next value of counter """
        self.counter += 1
        return self.counter

    def reset(self):
        self.counter = 0


class Algo():
    def __init__(self):
        self.count = Counter()

    def __once(self):
        """ Call once per session """
        self.count.reset()
        print()
        print(f"[{self.count.get()}] Run MStar mo3 ETF Quickrank [https://www.morningstar.com/etfs/screener-rank]")
        print(f"[{self.count.get()}] Check today's biggest gainers & decliners")
        print(f"[{self.count.get()}] Bias against buying what I bought < week ago.")

    def __all(self):
        """ Suggested actions common to all accounts """
        print(f'[{self.count.get()}] Check open orders.  Push BUYs')
        print(f'[{self.count.get()}] Check cash')
        print(f'[{self.count.get()}] Check ModAlloc')

    def ind441(self):
        print('[Ind441] *********')
        self.__all()
        print(f"[{self.count.get()}] MaxBal > $15k ? Trim.")
        print(f"[{self.count.get()}] Check today's biggest decliners and gainers")

    def roth089(self):
        print('[Roth089] *********')
        self.__all()

    def roll128(self):
        print('[Roll128] *********')
        self.__all()

    def utma611(self):
        print('[UTMA611] *********')
        self.__all()

    def jroll124(self):
        print('[JRoll124] *********')
        self.__all()

    def jroth900(self):
        print('[JRoth900] *********')
        self.__all()
        print(f"[{self.count.get()}] MaxBal > $4k ? Trim.")

    def jind668(self):
        print('[Ind668] *********')
        self.__all()
        print(f"[{self.count.get()}] Check today's biggest decliners and gainers")

    def utma118(self):
        print('[JRoth900] *********')
        self.__all()
        print(f"[{self.count.get()}] MaxBal > $1.5k ? Trim.")

    def run(self):
        """ Create a list of function pointers and call them in a loop """
        self.__once()
        # List of function pointers below
        accounts = [self.ind441, self.roth089, self.roll128, self.utma611, self.jroll124,
                self.jroth900, self.jind668, self.utma118]
        for account in accounts:
            # self.prompt_user(f'\n[{account.__name__}] ********* [(q)uit]\t')
            if input(f'\n[{account.__name__}] ********* [(q)uit]\t') == 'q': sys.exit("Goodbye ...\n")
            self.count.reset()
            account()
        print()


if __name__ == '__main__':
    algo = Algo()
    algo.run()
