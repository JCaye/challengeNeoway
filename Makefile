.PHONY: build

CHALLENGE_PK ?= 0
CHALLENGE_PORT ?= 5000
CHALLENGE_FOLDER ?= files
CHALLENGE_IMAGE ?= challenge

build:
	docker build -t $(CHALLENGE_IMAGE) .

run:
	docker run -p 5000:$(CHALLENGE_PORT) $(CHALLENGE_IMAGE)

get:
	curl http://localhost:$(CHALLENGE_PORT)/node/$(CHALLENGE_PK)

post:
	for file in $(CHALLENGE_FILEFOLDER)/*.jsonl; do curl -X POST -F "file=@$$file" http://localhost:$(CHALLENGE_PORT)/node; done
