#!/usr/bin/env python3

import sys
from getopt import getopt
from os.path import dirname
from unittest import TestLoader, TextTestRunner


def createTestRunner():
	opts, _ = getopt(sys.argv[1:], '', ['xml='])
	for o, v in opts:
		if o == '--xml':
			from xmlrunner import XMLTestRunner
			return XMLTestRunner(output=open(v, 'wb'))
	return TextTestRunner()


if __name__ == '__main__':
	cwd = dirname(sys.argv[0])
	suite = TestLoader().discover(cwd + '/test')
	runner = createTestRunner()
	result = runner.run(suite)
	sys.exit(not result.wasSuccessful())
