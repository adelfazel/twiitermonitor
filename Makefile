build:
	docker build -t twitterappimage:latest .

run: build
	docker run -p 5000:5000 -t --name twitterapp twitterappimage:latest

stop:
	docker stop twitterapp
	docker container rm twitterapp

inspectcontainer:
	docker exec -it twitterapp bash

test: build
	docker run --name twitterapp twitterappimage:latest
