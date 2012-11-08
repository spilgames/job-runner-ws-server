clean-pyc:
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

pep8:
	pep8 --show-pep8 -r job_runner_ws_server && echo "All good!"

unittest: clean-pyc
	coverage erase
	SETTINGS_PATH='.' coverage run --include "job_runner_ws_server*" --omit "*test*" -m unittest2 discover
	coverage report

test: pep8 unittest
