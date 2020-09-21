import math
import numpy as np

class mcts():
    def __init__(self, game, nnet):
        self.game = game
        self.nnet = nnet
        self.Qsa = {}    # Q values for s,a (as defined in the paper)
        self.Nsa = {}    # times edge s,a was visited
        self.Ns = {}     # times board s was visited
        self.Ps = {}     # initial policy (returned by neural net)
        self.Es = {}     # game.getGameEnded ended for board s
        self.Vs = {}     # game.getValidMoves for board s

    def getactionprob(self, oneminusone, new_board, temp=1):
        """
        This function performs numMCTSSims simulations of MCTS starting from
        canonicalBoard.

        Returns:
            probs: a policy vector where the probability of the ith action is
                   proportional to Nsa[(s,a)]**(1./temp)
        """
        for i in range(400):  # 왜 400인지는 아직 의문
            self.search(oneminusone, new_board)

        s = self.game.stringstring(oneminusone) # 판을 문자열 형식으로 변환하는 과정
        counts = [self.Nsa[(s, a)] if (s, a) in self.Nsa else 0 for a in range(self.game.actionsize())]

        if temp == 0:
            bestA = int(np.argmax(counts))
            probs = [0] * len(counts)
            probs[bestA] = 1
            return probs

        counts = [x**(1. / temp) for x in counts]
        probs = [x / float(sum(counts)) for x in counts]
        return probs

    def search(self, oneminusone, new_board):
        """
        This function performs one iteration of MCTS. It is recursively called
        till a leaf node is found. The action chosen at each node is one that
        has the maximum upper confidence bound as in the paper.

        Once a leaf node is found, the neural network is called to return an
        initial policy P and a value v for the state. This value is propogated
        up the search path. In case the leaf node is a terminal state, the
        outcome is propogated up the search path. The values of Ns, Nsa, Qsa are
        updated.

        NOTE: the return values are the negative of the value of the current
        state. This is done since v is in [-1,1] and if v is the value of a
        state for the current player, then its value is -v for the other player.

        Returns:
            v: the negative of the value of the current canonicalBoard
        """
        s = self.game.stringstring(oneminusone)

        if s not in self.Es:  
            self.Es[s] = self.game.ggeutnam(oneminusone, 1)
        if self.Es[s] != 0:
            # terminal node
            return -self.Es[s]

        if s not in self.Ps: # ps => initial policy
            # leaf node 맨 아래 노드
            self.Ps[s], v = self.nnet.predict(new_board)
            valids = self.game.validmove(oneminusone, 1) # 가능한 자리에 1이 들어간 채로 있는 배열
            self.Ps[s] = self.Ps[s] * valids  # masking invalid moves
            sum_Ps_s = np.sum(self.Ps[s]) # 가능한 자리의 갯수의 합

            if sum_Ps_s > 0:
                self.Ps[s] /= sum_Ps_s  # renormalize
            else:
                print("All valid moves were masked, do workaround.")
                self.Ps[s] = self.Ps[s] + valids
                self.Ps[s] /= np.sum(self.Ps[s])

            self.Vs[s] = valids
            self.Ns[s] = 0
            return -v

        valids = self.Vs[s]
        cur_best = -float('inf')
        best_act = -1

        for a in range(self.game.actionsize()):  # 가장 높은 확률의 행동을 찾는 과정
            if valids[a]:
                if (s, a) in self.Qsa:
                    u = self.Qsa[(s, a)] + 5 * self.Ps[s][a] * math.sqrt(self.Ns[s]) / (1 + self.Nsa[(s, a)])
                else:
                    u = 5 * self.Ps[s][a] * math.sqrt(self.Ns[s] + 1e-8)  # Q = 0 ?

                if u > cur_best:
                    cur_best = u
                    best_act = a

        a = best_act
        next_s, next_player, next_board = self.game.nextstate(oneminusone, new_board ,1, a)
        next_s = self.game.oneminusone(next_s, next_player)
        next_board = self.game.oneminusone(next_board, next_player)

        v = self.search(next_s, next_board)

        if (s, a) in self.Qsa:
            self.Qsa[(s, a)] = (self.Nsa[(s, a)] * self.Qsa[(s, a)] + v) / (self.Nsa[(s, a)] + 1)
            self.Nsa[(s, a)] += 1

        else:
            self.Qsa[(s, a)] = v
            self.Nsa[(s, a)] = 1

        self.Ns[s] += 1
        return -v

