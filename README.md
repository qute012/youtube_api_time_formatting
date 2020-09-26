# youtube_api_time_formatting
Youtube API need RFC 3339 time format. The module can generate an etherater that returns a day's interval.

# usage
```
from time_iter import TimeIter

A = TimeIter()

A.reset()

while(True):
    try:
        print(A())
    except Exception as e:
        if isinstance(e,Today):
            break
```
