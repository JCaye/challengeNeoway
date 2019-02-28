from flask import abort, Flask, request, Response
from model import Score
from service import ChallengeService

import json
import logging

app = Flask(__name__)

@app.route("/node/<pk>", methods = ["GET"])
def read_node(pk):
    node = ChallengeService().get_score(pk)
    return node if node is not None else abort(404)

@app.route("/node", methods = ["POST"])
def save_nodes():
    file = validate_file(request.files)

    service = ChallengeService()

    logging.getLogger("challenge_logger").info("Persisting data from file", file.filename)

    scores = []
    batch_size = 100
    for i, line in enumerate(file):
        if i % batch_size == 0 and len(scores) > 0:
            service.add_scores(scores)
            scores = []
        data = json.loads(line.decode('utf-8'))
        try:
            scores.append(Score(pk=int(data['pk']), score=int(data['score'])))
        except:
            logging.get_logger("challenge_logger").warning("Malformated data:", line)
    if (len(scores) > 0):
        service.add_scores(scores)

    return Response(status="201")

@app.teardown_request
def remove_session(ex=None):
    ChallengeService().close_session()

def validate_file(request_files):
    if "file" not in request_files:
        abort(400)

    file = request_files["file"]
    if file.filename == "":
        abort(400)

    if not is_valid_file_type(file.filename):
        abort (415)

    return file

def is_valid_file_type(filename):
    return "." in filename and filename.split(".")[-1] == "jsonl"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
