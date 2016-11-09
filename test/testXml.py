from unittest import TestCase
from bot import Xml


class TestXml(TestCase):
	def testEmpty(self):
		# Given
		media = Xml('root')
		# When
		text = media.xml()
		# Then
		self.assertEqual(text, '<?xml version="1.0"?><root></root>')

	def testPrimitiveTypes(self):
		media = Xml('primitives')
		# When
		media.write(int=12345)
		media.write(string='test')
		# Then
		self.assertIn('<primitives><int>12345</int><string>test</string>', media.xml())

	def testPrintableTypes(self):
		class Printable:
			def print(self, media):
				media.write(printed='yes')
		media = Xml('primitives')
		printable = Printable()
		# When
		media.write(printable=printable)
		# Then
		self.assertIn('<primitives><printable><printed>yes</printed></printa', media.xml())
