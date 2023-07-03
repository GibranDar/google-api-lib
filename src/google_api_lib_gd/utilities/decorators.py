from functools import wraps
from time import sleep
from typing import Any, Callable, Optional

from googleapiclient.errors import HttpError


def exponential_backoff_decorator(
    status_code: Optional[int] = None,
    retry_count: int = 5,
    retry_interval: int = 2,
    max_retry_interval: int = 60,
):
    """
    Decorator function for exponential backoff strategy.

    Args:
        retry_count (int): Number of retries.
        retry_interval (int): Initial interval between retries.
        max_retry_interval (int): Maximum interval between retries.
    """

    def wrapper(func: Callable[..., Any]):
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            for retry_count_ in range(retry_count):
                try:
                    return func(*args, **kwargs)
                except HttpError as e:

                    if status_code and e.resp.status != status_code:
                        raise e

                    print(f"Retrying {func.__name__}")
                    print("Rate limit exceeded, backing off due to:", e.reason)

                    if retry_count_ == retry_count - 1:
                        raise e
                    else:
                        sleep_time = retry_interval * (2**retry_count_)
                        if sleep_time > max_retry_interval:
                            sleep_time = max_retry_interval
                        sleep(sleep_time)
                        continue
                except Exception as e:
                    raise e

        return inner

    return wrapper
