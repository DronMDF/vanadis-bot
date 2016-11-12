#!/usr/bin/env python3
import sys
import logging
from getopt import getopt
import requests

sys.path.append('.')
from bot import Report 		# pylint: disable=wrong-import-position

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%d.%m %H:%M:%S')

host = '127.0.0.1:8000'
revision = '00000000'
project = 'test'

opts, args = getopt(sys.argv[1:], 'h:p:r:', ['host=', 'project=', 'revision='])
for o, v in opts:
	if o in ('-r', '--revision'):
		revision = v
	if o in ('-p', '--project'):
		project = v
	if o in ('-h', '--host'):
		host = v

for a in args:
	report = Report(open(a, 'r'))
	url = 'http://{0}/{1}/import/{2}'.format(host, project, revision)
	r = requests.post(url, data=report.xml())
	if r.status_code != requests.codes.ok:		# pylint: disable=no-member
		logging.error('Response http status code: %u', r.status_code)
