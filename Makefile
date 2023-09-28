install:
	# install
	pip install --upgrade pip &&\
	pip install -r requirements.txt
format:
	# format code
	black *.py src/*.py
lint:
	# lint the code, R-Recommended C-Configuration
	pylint --disable=R,C *.py src/*.py
test:
	# test
	python3 -m pytest -vv --cov=src tests/*.py
build:
	# buid the container
	docker build . -t fastapi-wikipedia
deploy:
	# deploy
run:
	# run the container
	docker run -p 8000:8000 fastapi-wikipedia
all: install format lint test build deploy 