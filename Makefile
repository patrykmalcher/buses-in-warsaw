setup:
	python -m venv venv && \
	. venv/bin/activate && \
	pip install -r requirements.txt

test:
	. venv/bin/activate && \
	python -m unittest discover -s src/test/datacollector -p '*Test.py'

