#!/bin/sh
set -e
find ./ -name "*.py" | xargs -r pep8 --show-source --max-line-length=100 --ignore=W191,E128
find ./ -name "*.py" | xargs -r pylint --max-line-length=100 --indent-string="	" -fparseable \
	-e all -r no
