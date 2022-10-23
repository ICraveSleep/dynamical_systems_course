
def create_time_span(t_start, t_end, step_size):
    """
    Create a timespan from t_start to t_end with step_size increments.
    :param t_start: start time
    :param t_end: end time
    :param step_size: step size (delta time)
    :return: A list of the timespan
    """
    time_span = []
    time_c = t_start
    while time_c <= t_end:
        time_span.append(time_c)
        time_c += step_size
    time_span.append(time_c)
    return time_span
