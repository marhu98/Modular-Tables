build:
	docker build -t test .
run:
	docker run --rm -v $$(pwd)/frames:/frames --name test test
	python gifphy.py
runExample:
	python figs.py
	docker run --rm -v $$(pwd)/frames:/frames --name test test
	python gifphy.py
rm:
	docker rm test
it:
	docker run --rm -v $$(pwd)/frames:/frames -it --name test test bash
configure:
	docker volume create --name cairo
