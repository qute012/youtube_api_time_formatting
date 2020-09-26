import datetime

class Today(Exception):
    def __init__(self):
        super().__init__("Iterater reaches today.")


class TimeIter(object):
    def __init__(self, year=2017, mon=1, day=1, timezone='KST'):
        if timezone=='KST':
            self.tz = datetime.timezone(datetime.timedelta(hours=9))
        self.year=year
        self.mon=mon
        self.day=day
        
        self.org = (year, mon, day)

    def _format_rfc3339(self):
        from_ = datetime.datetime(self.year, self.mon, self.day, 0, 0, 0, tzinfo=self.tz).isoformat("T")
        to_ = datetime.datetime(self.year, self.mon, self.day, 23, 59, 59, tzinfo=self.tz).isoformat("T")
        self.day+=1
        return from_, to_
    
    def _is_today(self):
        today = datetime.date.today()
        comp = datetime.date(self.year, self.mon, self.day)
        if today==comp:
            raise Today()
    
    def _oept(self):
        flag = True
        while(flag):
            try:
                time = datetime.datetime(self.year, self.mon, self.day, 0, 0, 0, tzinfo=self.tz).isoformat("T")
                flag = False
            except Exception as e:
                prob=str(e).split(' ')[0]
                if prob=="day":
                    self.day=1
                    self.mon+=1
                elif prob=="month":
                    self.year+=1
                    self.mon=1
                    self.day=1
    
    def __call__(self):
        self._oept()
        self._is_today()
        return self._format_rfc3339()
    
    def reset(self):
        self.year, self.mon, self.day = self.org
        
"""
A = TimeIter()

while(True):
    try:
        print(A())
    except Exception as e:
        if isinstance(e,Today):
            break

A.reset()
"""
