#!/bin/bash
set -e
PYTHONPATH=.
find ./ -name "*.py" | xargs -r pep8 --show-source --max-line-length=100 --ignore=W191,E128
find ./ -name "*.py" | xargs -r pylint --max-line-length=100 --indent-string="	" -fparseable \
	-r no --const-rgx="[a-z][a-z0-9_]{0,30}$" --variable-rgx="[a-z][a-z0-9_]{0,30}$" \
	--function-rgx="[a-z][a-zA-Z0-9]{0,30}$" --module-rgx="[a-zA-Z][a-zA-Z0-9]{0,30}$" \
	-e all -d missing-docstring,bad-continuation,too-few-public-methods,invalid-name
