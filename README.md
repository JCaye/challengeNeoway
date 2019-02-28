# What?
Service to persist and lookup score values based on unique identifiers.

# How?
## Requirements
You need:
* docker
* make

## Setup
Run `make build run` to build a docker image for the application and run it. Optional arguments are:
* `CHALLENGE_IMAGE` - sets the image name. Defaults to "challenge"
* `CHALLENGE_PORT` - sets the localhost port the app will be accessed through. Defaults to 5000

## Usage
Run `make get CHALLENGE_PK=number` to lookup the score for the item identified by the (integer) key `number`. Returns a json of the form `{'pk': 0, 'score': 0}`. Returns the following HTTP responses:
* `200` if score was found
* `404` if score was not found

Run `make post CHALLENGE_FOLDER=folder_path` to persist all values present in .jsonl files within the specified file path. If an entry's identifier is already in the database, it is skipped (and this is logged at warning level). Returns the following HTTP codes:
* `201` upon successful persistence of objects
* `400` if no file was present
* `415` if the file extension is not .jsonl
