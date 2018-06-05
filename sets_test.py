import unittest
from sets import Set, union, intersection, setDifference, relativeCompliment, symmetricDifference

def addHelper(data):
	testSet = Set()
	for i in data:
		testSet.add(i)
	return testSet

def testHasHelper(testObject, testList):
	for i in testList:
		if testObject.has(i) == False:
			return False
	return True


class SetTests(unittest.TestCase):
	def test_add_to_set(self):
		testData = (1,7.09,'C')
		testSet = addHelper(testData)

		self.assertTrue(testHasHelper(testSet, testData))
		self.assertFalse(testSet.has('D'))

	def test_remove_from_set(self):
		testData = ('A','B','C')
		testSet = addHelper(testData)
		testSet.remove('A')

		self.assertFalse(testSet.has('A'))

	def test_union(self):
		testData1 = ('A','B','C')
		testSetUno = addHelper(testData1)
		testData2 = ('D','E','F')
		testSetDos = addHelper(testData2)
		testUnion = union(testSetUno.getSet(), testSetDos.getSet())

		self.assertTrue('A' in testUnion.values())
		self.assertTrue('B' in testUnion.values())
		self.assertTrue('C' in testUnion.values())
		self.assertTrue('D' in testUnion.values())
		self.assertTrue('E' in testUnion.values())
		self.assertTrue('F' in testUnion.values())

	def test_intersection(self):
		testData1 = ('A','B','C')
		testSetUno = addHelper(testData1)
		testData2 = ('A','B','F')
		testSetDos = addHelper(testData2)
		testIntersection = intersection(testSetUno.getSet(), testSetDos.getSet())

		self.assertTrue('A' in testIntersection.values())
		self.assertTrue('B' in testIntersection.values())
		self.assertFalse('C' in testIntersection.values())

	def test_setDifference(self):
		testData1 = ('A','B','C','D')
		testSetUno = addHelper(testData1)
		testData2 = ('A','B','F')
		testSetDos = addHelper(testData2)
		testIntersection = setDifference(testSetUno.getSet(), testSetDos.getSet())

		self.assertTrue('C' in testIntersection.values())
		self.assertTrue('D' in testIntersection.values())
		self.assertFalse('A' in testIntersection.values())

	def test_relativeCompliment(self):
		testData1 = ('A','B','E')
		testSetUno = addHelper(testData1)
		testData2 = ('A','B','C','D')
		testSetDos = addHelper(testData2)
		testRelativeCompliment = relativeCompliment(testSetUno.getSet(), testSetDos.getSet())

		self.assertTrue('C' in testRelativeCompliment.values())
		self.assertTrue('D' in testRelativeCompliment.values())
		self.assertFalse('A' in testRelativeCompliment.values())

	def test_symmetricDifference(self):
		testData1 = ('A','B','E','F')
		testSetUno = addHelper(testData1)
		testData2 = ('A','B','C','D')
		testSetDos = addHelper(testData2)
		testSymmetricDifference = symmetricDifference(testSetUno.getSet(), testSetDos.getSet())

		self.assertTrue('E' in testSymmetricDifference.values())
		self.assertTrue('F' in testSymmetricDifference.values())
		self.assertTrue('C' in testSymmetricDifference.values())
		self.assertTrue('D' in testSymmetricDifference.values())
		self.assertFalse('A' in testSymmetricDifference.values())


if __name__ == '__main__':
	unittest.main()
