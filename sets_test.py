import unittest
from sets import Set, union, intersection, setDifference, relativeCompliment, symmetricDifference

class SetTests(unittest.TestCase):
	def test_add_to_set(self):
		testSet = Set()
		testSet.add(1)
		testSet.add('B')
		testSet.add('C')
		self.assertTrue(testSet.has(1))
		self.assertTrue(testSet.has('B'))
		self.assertTrue(testSet.has('C'))
		self.assertFalse(testSet.has('D'))

	def test_remove_from_set(self):
		testSet = Set()
		testSet.add('A')
		testSet.add('B')
		testSet.add('C')
		self.assertTrue(testSet.has('A'))

		testSet.remove('A')
		self.assertFalse(testSet.has('A'))

	def test_union(self):
		testSetUno = Set()
		testSetUno.add('A')
		testSetUno.add('B')
		testSetUno.add('C')

		testSetDos = Set()
		testSetDos.add('D')
		testSetDos.add('E')
		testSetDos.add('F')

		testUnion = union(testSetUno.getSet(), testSetDos.getSet())
		self.assertTrue('A' in testUnion.values())
		self.assertTrue('B' in testUnion.values())
		self.assertTrue('C' in testUnion.values())
		self.assertTrue('D' in testUnion.values())
		self.assertTrue('E' in testUnion.values())
		self.assertTrue('F' in testUnion.values())

	def test_intersection(self):
		testSetUno = Set()
		testSetUno.add('A')
		testSetUno.add('B')
		testSetUno.add('C')

		testSetDos = Set()
		testSetDos.add('A')
		testSetDos.add('B')
		testSetDos.add('F')

		testIntersection = intersection(testSetUno.getSet(), testSetDos.getSet())
		self.assertTrue('A' in testIntersection.values())
		self.assertTrue('B' in testIntersection.values())
		self.assertFalse('C' in testIntersection.values())

	def test_setDifference(self):
		testSetUno = Set()
		testSetUno.add('A')
		testSetUno.add('B')
		testSetUno.add('C')
		testSetUno.add('D')

		testSetDos = Set()
		testSetDos.add('A')
		testSetDos.add('B')
		testSetDos.add('F')

		testIntersection = setDifference(testSetUno.getSet(), testSetDos.getSet())
		self.assertTrue('C' in testIntersection.values())
		self.assertTrue('D' in testIntersection.values())
		self.assertFalse('A' in testIntersection.values())

	def test_relativeCompliment(self):
		testSetUno = Set()
		testSetUno.add('A')
		testSetUno.add('B')
		testSetUno.add('E')

		testSetDos = Set()
		testSetDos.add('A')
		testSetDos.add('B')
		testSetDos.add('C')
		testSetDos.add('D')

		testRelativeCompliment = relativeCompliment(testSetUno.getSet(), testSetDos.getSet())
		self.assertTrue('C' in testRelativeCompliment.values())
		self.assertTrue('D' in testRelativeCompliment.values())
		self.assertFalse('A' in testRelativeCompliment.values())

	def test_symmetricDifference(self):
		testSetUno = Set()
		testSetUno.add('A')
		testSetUno.add('B')
		testSetUno.add('E')
		testSetUno.add('F')

		testSetDos = Set()
		testSetDos.add('A')
		testSetDos.add('B')
		testSetDos.add('C')
		testSetDos.add('D')

		testSymmetricDifference = symmetricDifference(testSetUno.getSet(), testSetDos.getSet())
		self.assertTrue('E' in testSymmetricDifference.values())
		self.assertTrue('F' in testSymmetricDifference.values())
		self.assertTrue('C' in testSymmetricDifference.values())
		self.assertTrue('D' in testSymmetricDifference.values())
		self.assertFalse('A' in testSymmetricDifference.values())


if __name__ == '__main__':
	unittest.main()
