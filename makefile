build:
	docker build -t test .
run:
	docker run --rm -v $$(pwd)/frames:/frames --name test test
rm:
	docker rm test
it:
	docker run --rm -v $$(pwd)/frames:/frames -it --name test test bash
configure:
	docker volume create --name cairo
