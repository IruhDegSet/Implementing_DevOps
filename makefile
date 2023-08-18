install:
	pip install --upgrade pip &&\
	pip install requirements.txt &&\
	sudo apt install -y pylint

lint:
	pylint --disable=R,C math_ops.py

test:
	pytest -v test_math_ops.py