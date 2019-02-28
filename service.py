from db import ChallengeDB
from model import Score

import logging
import traceback
import json

class ChallengeService():
    database = ChallengeDB("challenge.sqlite")
    logger = logging.getLogger("challenge_logger")

    def add_scores(self, score_list):
        session = self.database.get_session()

        for score in score_list:
            if session.query(Score).filter(Score.pk == score.pk).first() is not None:
                self.logger.warning("Skipping score with pk {} as it already exists.".format(score.pk))
                continue
            session.add(score)
        try:
            session.commit()
            self.logger.info("Transaction succeeded.")
        except:
            session.rollback()
            traceback.print_exc()
            self.logger.info("Transaction aborted.")

    def get_score(self, pk):
        session = self.database.get_session()
        score = session.query(Score).filter(Score.pk == pk).first()
        return json.dumps({'pk': score.pk, 'score': score.score}) if score is not None else None

    def close_session(self):
        self.database.close_session()
