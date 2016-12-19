from unittest import TestCase
from bot import Filelist


class TestFilelist(TestCase):
	def testValidateToFull(self):
		# Given
		filelist = Filelist('<revision><file><name>zebra/zserv.c</name></file></revision>')
		# Then
		self.assertEqual(filelist.canonize('zserv.c'), 'zebra/zserv.c')
		self.assertEqual(filelist.canonize('./zserv.c'), 'zebra/zserv.c')

	def testValidateToCut(self):
		# Given
		filelist = Filelist('<revision><file><name>zebra/zserv.c</name></file></revision>')
		# Then
		self.assertEqual(filelist.canonize('projects/zebra/zserv.c'), 'zebra/zserv.c')
		self.assertEqual(filelist.canonize('../zebra/zserv.c'), 'zebra/zserv.c')

	def testValidateToNormal(self):
		# Given
		filelist = Filelist('<revision><file><name>zebra/zserv.c</name></file></revision>')
		# Then
		self.assertEqual(filelist.canonize('test/zebra/../zebra/zserv.c'), 'zebra/zserv.c')
