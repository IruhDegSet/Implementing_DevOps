install:
	pip install --upgrade pip &&\
	pip install requirements.txt &&\
	sudo apt install -y pylint

lint:
	pylint --disable=R,C math_ops.py

test:
	python -m pytest -vv --cov=math_ops test_math_ops.py