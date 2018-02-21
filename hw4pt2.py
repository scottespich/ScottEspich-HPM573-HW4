from enum import Enum

import numpy as np









class outcome(Enum):
    Tails = 1
    Head = 0
class Game(object):
    def __init__(self, id):
        self._id = id
        self._outcome = outcome.Tails
        self._wins = 0
        self._Tails2 = 0
        self._events = 20
        self._eventnumber = 1
        self._rnd = np.random
        self._rnd.seed(self._id * self._eventnumber)
    def nextflip(self): #make outcome for sequential flips
        if self._outcome == outcome.Tails:

            if self._rnd.random_sample() < 0.4:
                if self._Tails2 >= 2:
                    self._wins += 1
                self._outcome = outcome.Head
                self._Tails2 = 0

            if self._rnd.random_sample() > 0.4:
                self._outcome = outcome.Tails
                self._Tails2 += 1
        elif self._outcome == outcome.Head:

            if self._rnd.random_sample() < 0.4:
                self._outcome = outcome.Head
                self._Tails2 = 0

            if self._rnd.random_sample() > 0.4:
                self._outcome = outcome.Tails
                self._Tails2 = 1
        self._eventnumber += 1
    def flipcoin(self):
        for i in range(1, self._events+1):
            self._rnd = np.random
            self._rnd.seed(self._id * self._eventnumber)
            self.nextflip()

    def reward(self):
        self.flipcoin()
        self._payout = -250
        self._payout += 100*self._wins
        return self._payout
#creat class with
class Cohort:
    def __init__(self, id, Npeople):
        self._people = []
        n = 1

        while n <= Npeople:
            people = Game(id=id * Npeople + n)

            self._people.append(people)
            n += 1

    def run(self):
        game_rewards = []
        for people in self._people:
            game_rewards.append(people.reward())
        return sum(game_rewards)/len(game_rewards)
FLIP = Cohort(id=1, Npeople=1000)
print('Result:', FLIP.run())
