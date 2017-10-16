from datetime import datetime, timedelta


# TODO: EST
def list_past_n_days(n, start_ts=datetime.utcnow()):
    days = []
    start_date = start_ts.date()
    for i in range(n):
        # days.insert(0, days.append(str(start_date - timedelta(days=i))))
        days.append(str(start_date - timedelta(days=i)))
    days = days[::-1]
    return days


# TODO: Pomodoro model will need a start ts
def build_graph_view(n, PomodoroModel, user_id, start=datetime.utcnow()):
    day_range = list_past_n_days(n, start)
    # NOTE: May need to inject a function to takes PomodoroModel as input
    pomodoro_dicts = list(map(
        lambda p: p.__dict__,
        PomodoroModel.past_n_days(n, user_id)
    ))
    agg = {}
    for p in pomodoro_dicts:
        # TODO: DefaultDict
        if p['context'] not in agg:
            agg[p['context']] = [0] * len(day_range)
        agg[p['context']][day_range.index(str(p['end_time'].date()))] += 1
    return {"dates": day_range, "data": [{"context": k, 'counts': v} for k, v in agg.items()]}
