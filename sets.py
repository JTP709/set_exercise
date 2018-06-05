class Set():
	def __init__(self):
		self.setDictionary = {}

	def add(self, value):
		if isinstance(value, (int, float, complex)):
			value = str(value)
		hashValue = hash(value)
		self.setDictionary[hashValue] = value

	def remove(self, value):
		if isinstance(value, (int, float, complex)):
			value = str(value)
		hashValue = hash(value)
		del self.setDictionary[hashValue]

	def has(self, value):
		if isinstance(value, (int, float, complex)):
			value = str(value)
		hashValue = hash(value)
		return hashValue in self.setDictionary

def union(set_uno, set_dos):
	return {**set_uno, **set_dos}

def intersection(set_uno, set_dos):
	intersections = {}
	for i in set_uno:
		if i in set_dos:
			intersections[i] = set_uno[i]
	return intersections

def setDifference(set_uno, set_dos):
	differences = {}
	for i in set_uno:
		if i not in set_dos:
			differences[i] = set_uno[i]
	return differences

def relativeCompliment(set_uno, set_dos):
	differences = {}
	for i in set_dos:
		if i not in set_uno:
			differences[i] = set_dos[i]
	return differences

def symmetricDifference(set_uno, set_dos):
	differences = {}
	for i in set_dos:
		if i not in set_uno:
			differences[i] = set_dos[i]
	for i in set_uno:
		if i not in set_dos:
			differences[i] = set_uno[i]
	return differences
