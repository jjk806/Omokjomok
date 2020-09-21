import tensorflow as tf
import numpy as np
import random
import math
import os

STONE_NONE = 0
STONE_PLAYER1 = 1
STONE_PLAYER2 = 2
STONE_MAX = 5

gridSize = 8
nbActions = gridSize * gridSize
nbStates = gridSize * gridSize
hiddenSize = 100
maxMemory = 500
batchSize = 50
epoch = 100
epsilonStart = 1
epsilonDiscount = 0.999
epsilonMinimumValue = 0.1
discount = 0.9
learningRate = 0.0001
winReward = 1

def randf(s, e):
    return (float(random.randrange(0, (e - s) * 9999)) / 10000) + s

class OmokEnvironment():

	def __init__(self, gridSize):
		self.gridSize = gridSize
		self.nbStates = self.gridSize * self.gridSize
		self.state = np.zeros(self.nbStates, dtype = np.uint8)
        # np.zeros 는 0을 가지는 행렬 만드는 것

	def reset(self):
		self.state = np.zeros(self.nbStates, dtype = np.uint8)

	def getState(self):
		return np.reshape(self.state, (1, self.nbStates))

	def getStateInverse(self):
		tempState = self.state.copy()
		
		for i in xrange(self.nbStates): # range() 결과값은 list이지만, xrange() 결과값은 xrange이다.
			if( tempState[i] == STONE_PLAYER1 ):
				tempState[i] = STONE_PLAYER2
			elif( tempState[i] == STONE_PLAYER2 ):
				tempState[i] = STONE_PLAYER1
		
		return np.reshape(tempState, (1, self.nbStates))

	def GetReward(self, player, action):
	
		# 왼쪽 검사
		if( action % self.gridSize > 0 ):
			if( self.state[action - 1] == player ):
				return 0.05

		# 오른쪽 검사
		if( action % self.gridSize < self.gridSize - 1 ):
			if( self.state[action + 1] == player ):
				return 0.05

		# 위 검사
		if( action - self.gridSize >= 0 ):
			if( self.state[action - self.gridSize] == player ):
				return 0.05

		# 아래 검사
		if( action + self.gridSize < self.nbStates ):
			if( self.state[action + self.gridSize] == player ):
				return 0.05

		# 왼쪽 위 검사
		if( (action % self.gridSize > 0) and (action - self.gridSize >= 0) ):
			if( self.state[action - 1 - self.gridSize] == player ):
				return 0.05

		# 오른쪽 위 검사
		if( (action % self.gridSize < self.gridSize - 1) and (action - self.gridSize >= 0) ):
			if( self.state[action + 1 - self.gridSize] == player ):
				return 0.05

		# 왼쪽 아래 검사
		if( (action % self.gridSize > 0) and (action + self.gridSize < self.nbStates) ):
			if( self.state[action - 1 + self.gridSize] == player ):
				return 0.05

		# 오른쪽 아래 검사
		if( (action % self.gridSize < self.gridSize - 1) and (action + self.gridSize < self.nbStates) ):
			if( self.state[action + 1 + self.gridSize] == player ):
				return 0.05
		
		return 0

	def CheckMatch(self, player):
		for y in xrange(self.gridSize):
			for x in xrange(self.gridSize):
			
				#--------------------------------
				# 오른쪽 검사
				#--------------------------------
				match = 0
				
				for i in xrange(STONE_MAX):
					if( x + i >= self.gridSize ):
						break
	
					if( self.state[y * self.gridSize + x + i] == player ):
						match += 1
					else:
						break;

					if( match >= STONE_MAX ):
						return True

				#--------------------------------
				# 아래쪽 검사
				#--------------------------------
				match = 0
				
				for i in xrange(STONE_MAX):
					if( y + i >= self.gridSize ):
						break
	
					if( self.state[(y + i) * self.gridSize + x] == player ):
						match += 1
					else:
						break;

					if( match >= STONE_MAX ):
						return True

				#--------------------------------
				# 오른쪽 대각선 검사
				#--------------------------------
				match = 0
				
				for i in xrange(STONE_MAX):
					if( (x + i >= self.gridSize) or (y + i >= self.gridSize) ):
						break
	
					if( self.state[(y + i) * self.gridSize + x + i] == player ):
						match += 1
					else:
						break;

					if( match >= STONE_MAX ):
						return True

				#--------------------------------
				# 왼쪽 대각선 검사
				#--------------------------------
				match = 0
				
				for i in xrange(STONE_MAX):
					if( (x - i < 0) or (y + i >= self.gridSize) ):
						break
	
					if( self.state[(y + i) * self.gridSize + x - i] == player ):
						match += 1
					else:
						break;

					if( match >= STONE_MAX ):
						return True
	
		return False

	def isGameOver(self, player):
		if( self.CheckMatch(STONE_PLAYER1) == True ):
			if( player == STONE_PLAYER1 ):
				return True, winReward
			else:
				return True, 0
		elif( self.CheckMatch(STONE_PLAYER2) == True ):
			if( player == STONE_PLAYER1 ):
				return True, 0
			else:
				return True, winReward
		else:
			for i in xrange(self.nbStates):
				if( self.state[i] == STONE_NONE ):
					return False, 0
			return True, 0
	
	def updateState(self, player, action):
		self.state[action] = player;

	def act(self, player, action):
		self.updateState(player, action)
		gameOver, reward = self.isGameOver(player)

		if( reward == 0 ):
			reward = self.GetReward(player, action)
		
		if( player == STONE_PLAYER1 ):
			nextState = self.getState()
		else:
			nextState = self.getStateInverse()
		
		return nextState, reward, gameOver

	def getAction(self, sess, currentState):
		q = sess.run(output_layer, feed_dict = {X: currentState, keep_prob:1.0})
		
		while( True ):
			action = q.argmax()

			if( self.state[action] == STONE_NONE ):
				return action
			else:
				q[0, action] = -99999

	def getActionRandom(self):
		while( True ):
			action = random.randrange(0, nbActions)

			if( self.state[action] == STONE_NONE ):
				return action

def playGame(env, memory, sess, saver, epsilon, iteration):

	winCount = 0

	for i in xrange(epoch):
		env.reset()

		err = 0
		gameOver = False
		currentPlayer = STONE_PLAYER1
		
		while( gameOver != True ):
			action = - 9999
			
			if( currentPlayer == STONE_PLAYER1 ):
				currentState = env.getState()
			else:
				currentState = env.getStateInverse()

			if( randf(0, 1) <= epsilon ):
				action = env.getActionRandom()
			else:
				action = env.getAction(sess, currentState)

			if( epsilon > epsilonMinimumValue ):
				epsilon = epsilon * epsilonDiscount
		
			nextState, reward, gameOver = env.act(currentPlayer, action)

			if( reward == 1 and currentPlayer == STONE_PLAYER1 ):
				winCount = winCount + 1

			memory.remember(currentState, action, reward, nextState, gameOver)

			inputs, targets = memory.getBatch(output_layer, batchSize, nbActions, nbStates, sess)
			
			_, loss = sess.run([optimizer, cost], feed_dict = {X: inputs, Y: targets, keep_prob:1.0})
			err = err + loss
			
			if( currentPlayer == STONE_PLAYER1 ):
				currentPlayer = STONE_PLAYER2
			else:
				currentPlayer = STONE_PLAYER1

		print("Epoch " + str(iteration) + str(i) + ": err = " + str(err) + ": Win count = " + str(winCount) +
				" Win ratio = " + str(float(winCount) / float(i + 1) * 100))

		print(targets)

		if( (i % 10 == 0) and (i != 0) ):
			save_path = saver.save(sess, os.getcwd() + "/OmokModelDeep.ckpt")
			print("Model saved in file: %s" % save_path)
#------------------------------------------------------------



#------------------------------------------------------------
# 메인 함수
#------------------------------------------------------------
def main(_):

	# 환경 인스턴스 생성
	env = OmokEnvironment(gridSize)

	# 리플레이 메모리 인스턴스 생성
	memory = ReplayMemory(gridSize, maxMemory, discount)

	# 텐서플로우 초기화
	sess = tf.Session()
	sess.run(tf.global_variables_initializer())

	# 세이브 설정
	saver = tf.train.Saver()

	# 모델 로드
	if( os.path.isfile(os.getcwd() + "/OmokModelDeep.ckpt.index") == True ):
		saver.restore(sess, os.getcwd() + "/OmokModelDeep.ckpt")
		print('Saved model is loaded!')
	
	# 게임 플레이
	iteration = 0
	while( True ):
		playGame(env, memory, sess, saver, epsilonStart, iteration);
		iteration += 1

	# 세션 종료
	sess.close()
#------------------------------------------------------------



#------------------------------------------------------------
# 메인 함수 실행
#------------------------------------------------------------
if __name__ == '__main__':
	tf.app.run()
#------------------------------------------------------------