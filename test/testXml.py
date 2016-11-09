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
