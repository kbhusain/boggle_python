import re,  math, random, sys, time, bisect, string, time

cubes16 = ['FORIXB', 'MOQABJ', 'GURILW', 'SETUPL',
           'CMPDAE', 'ACITAO', 'SLCRAE', 'ROMASH',
           'NODESW', 'HEFIYE', 'ONUDTK', 'TEVIGN',
           'ANEDVZ', 'PINESH', 'ABILYT', 'GKYLEU']
		   
neighbors = [[4, 5, 1], [5, 4, 6, 0, 2], [6, 5, 7, 1, 3], [7, 6, 2], 
			[0, 1, 8, 9, 5], [1, 0, 2, 9, 8, 10, 4, 6], [2, 1, 3, 10, 9, 11, 5, 7], [3, 2, 11, 10, 6], 
			[4, 5, 12, 13, 9], [5, 4, 6, 13, 12, 14, 8, 10], [6, 5, 7, 14, 13, 15, 9, 11], [7, 6, 15, 14, 10], 
			[8, 9, 13], [9, 8, 10, 12, 14], [10, 9, 11, 13, 15], [11, 10, 14]]

class pyBoggle:
	def __init__(self, board=None):
		self.scores = [0, 0, 0, 0, 1, 2, 3, 5] + [11] * 100
		self.makeWords()     # Make a dictionary. 
		self.found = {}      # Initiate words found. 
		self.board = board   # Use the passed board. 
		if self.board == None:  
			self.make_board()
	
	def makeWords(self):
		woids = open('big.txt').read()
		mywords = re.findall('[A-Z]+', woids.upper())    # Get words
		self.allwords = { } # collections.defaultdict(lambda: 1)
		for f in mywords: 
			try:
				self.allwords[f] += 1
			except: 
				self.allwords[f] = 1

	def make_board(self):
		# Makes a 4x4 board. 
		cubes = [cubes16[i % 16] for i in range(16)]
		random.shuffle(cubes)
		self.board = map(random.choice, cubes)
		#self.make_neighbors()
		self.neighbors = neighbors; 
		
	def show_board(self):
		"Print the board in a 2-d array."
		n2 = 16; n = 4
		for i in range(16):
			if i % n == 0: print
			if self.board[i] == 'Q':
				print ("QU"),
			else: 
				print (str(self.board[i]) + " "),
		print

	def findWords(self, board=None):
		self.found = {}
		atime = time.time() 
		for i in range(16):
			visited = [False,]* 16
			prefix  = '' 
			self.findme(i, visited, prefix)
		print ("Time %d", time.time() - atime)
		woids = self.found.keys()
		woids.sort()
		return woids
		
	def findme(self, i, visited, prefix):
		"""
		Recursive function. 
		Looking in square i, find the words that continue the prefix,
        considering the entries in self.wordlist.words[lo:hi], and not
        revisiting the squares in visited."""
		if visited[i]: return
		visited[i] = True;
		sprefix = prefix + self.board[i]
		if self.allwords.has_key(sprefix) and len(sprefix) > 2:
			try:
				self.found[sprefix] = +1
			except: 
				self.found[sprefix] = 1
			#if self.found[sprefix] == 1: print sprefix
		for j in self.neighbors[i]: 
			if not visited[j]: self.findme(j, visited, sprefix)
		visited[i] = False; 
		
		
	def words(self): return self.found.keys()
	def score(self,words): return sum([self.scores[len(w)] for w in words])
	def __len__(self):       return len(self.found)
	
if __name__ == '__main__': 
	x = pyBoggle()
	x.show_board()
	woids = x.findWords()
	x.show_board()
	print (woids)
	print (x.score(woids))