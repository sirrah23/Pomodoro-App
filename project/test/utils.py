class FakePomodoro(object):

    def __init__(self, seed):
        self.data = []
        for s in seed:
            self.data.append(FakeDataWrapper(s[0], s[1], s[2], s[3], s[4]))

    def past_n_days(self, n, user_id):
        return self.data


class FakeDataWrapper(object):

    def __init__(
            self,
            length_seconds,
            end_time, context,
            interruptions,
            user_id
    ):
        self.length_seconds = length_seconds
        self.end_time = end_time
        self.context = context
        self.interruptions = interruptions
        self.user_id = user_id
