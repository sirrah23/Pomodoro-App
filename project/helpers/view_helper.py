from datetime import datetime, timedelta


# TODO: EST
def list_past_n_days(n, start_ts=datetime.utcnow()):
    days = []
    start_date = start_ts.date()
    for i in range(n):
        days.append(str(start_date - timedelta(days=i)))
    days = days[::-1]
    return days


def build_graph_view(n,
                     PomodoroModel,
                     user_id,
                     start=None,
                     logger=None):
    def log(s):
        if logger:
            logger.info(s)

    # NOTE: Default arguments are only computed once so
    # mutable default arguments will not be updated which
    # is why we moved it here
    if not start:
        start = datetime.utcnow()

    log("Building graph data for {}".format(start))

    # Obtain list of days for which we want pomodoro data
    day_range = list_past_n_days(n, start)

    # Obtain the dictionary data inside of rows in the database from the past n days
    pomodoro_dicts = list(map(
        lambda p: p.__dict__,
        PomodoroModel.past_n_days(n, user_id)
    ))

    # Aggregate the data per context e.g. work, home, cafe, etc.
    agg = {}
    for p in pomodoro_dicts:
        # TODO: DefaultDict
        if p['context'] not in agg:
            agg[p['context']] = [0] * len(day_range)
        try:
          agg[p['context']][day_range.index(str(p['end_time'].date()))] += 1
        except ValueError:
            # Obtained too much data, log for later
            log("Index error for date {}".format(p['end_time'].date()))
            log("Day range was: {}".format(day_range))

    log("Done building graph data for {}".format(start))
    return {"dates": day_range, "data": [{"context": k, 'counts': v} for k, v in agg.items()]}
