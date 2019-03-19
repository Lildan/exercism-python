class HighScores(object):
    def __init__(self, scores:[]):
        self.scores = scores
        self.latest_value = self.scores[len(self.scores)-1]

    def latest(self):
        return self.latest_value

    def personal_best(self):
        self.scores.sort(reverse=True)
        return self.scores[0]
    def personal_top_three(self):
        self.scores.sort(reverse=True)
        return self.scores[0:3]

