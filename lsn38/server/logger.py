import datetime
from functools import wraps


def event_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with open(f'event_log_for_{str(datetime.datetime.now().date())}.txt', 'a') as logger:
            event = f"[{datetime.datetime.now().time().strftime('%H:%M:%S')}] {func(*args, **kwargs)}\n"
            logger.writelines(event)
            logger.close()
    return wrapper