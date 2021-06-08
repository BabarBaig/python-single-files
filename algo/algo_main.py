""" print() format: Condition ? Action """

import sys

class Counter():
    def __init__(self, start=0):
        self.counter = start

    def get_count(self):
        self.counter += 1
        return self.counter

    def reset(self):
        self.counter = 0


class Algo():
    def __init__(self):
        self.count = Counter()

    def prompt_user(self, prompt: str):
        resp = input(prompt)
        if resp == 'q':     sys.exit("Quitting\n")
        return resp

    def __once(self):
        """ Call once per session """
        self.count.reset()
        print()
        print(f"[{self.count.get_count()}] Check today's biggest gainers & decliners")
        print(f"[{self.count.get_count()}] Bias against buying what I bought < week ago.")

    def __all(self):
        """ Suggested actions common to all accounts """
        print(f'[{self.count.get_count()}] Check open orders')
        print(f'[{self.count.get_count()}] Check cash')
        print(f'[{self.count.get_count()}] Check ModAlloc')

    def ind441(self):
        print('In Ind441')
        self.__all()
        print(f"[{self.count.get_count()}] Check today's biggest decliners and gainers")

    def roth089(self):
        print('In Roth089')
        self.__all()

    def roll128(self):
        print('In Roll128')
        self.__all()

    def utma611(self):
        print('In UTMA611')
        self.__all()

    def jroll124(self):
        print('In JRoll124')
        self.__all()

    def jroth900(self):
        print('In JRoth900')
        self.__all()
        print(f"[{self.count.get_count()}] MaxBal > $4k ? Trim to cash.")

    def jind668(self):
        print('In JInd668')
        self.__all()
        print(f"[{self.count.get_count()}] Check today's biggest decliners and gainers")

    def utma118(self):
        print('In JRoth900')
        self.__all()

    def run(self):
        """ Create a list of function pointers and call them in a loop """
        self.__once()
        accounts = [self.ind441, self.roth089, self.roll128, self.utma611, self.jroll124,
                self.jroth900, self.jind668, self.utma118]
        for account in accounts:
            if self.prompt_user(f'\n[{account.__name__}] ********* [(q)uit, (s)kip]\t') == 's':    return
            self.count.reset()
            account()
        print()


if __name__ == '__main__':
    algo = Algo()
    algo.run()
