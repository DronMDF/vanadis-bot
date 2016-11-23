#!/usr/bin/env python3
import sys
import logging
from getopt import getopt

sys.path.append('.')
# pylint: disable=wrong-import-position
from bot import (Filelist, Report, RequestImport, RequestLogTime, Server)

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%d.%m %H:%M:%S', level=logging.INFO)

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

server = Server(host, project)

for a in args:
	filelist = Filelist()
	report = Report(open(a, 'r'), filelist)
	RequestLogTime(
		RequestImport(server, revision, report.xml())
	).act()
