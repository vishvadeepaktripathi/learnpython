import time
import datetime
from datetime import date
from _datetime import datetime_CAPI


def CompareDate(self):
    date_1 = date.today()
    end_date = date_1 + datetime.timedelta(days=10)
    end_date.strftime("%x")
    #print(self)
    dt_new=time.strptime(self, "%x")
    #print(str(dt_new))
    #datetime.strptime(dt,"%x").date()
    dt_new=time.strptime(self,"%x")
    #dt_new=datetime.date(2020,7,19)
    #print(end_date)
    if dt_new!=end_date:
            varOutput= "Date is not equal"
            return varOutput