from datetime import datetime

from datetime import timedelta, date

#If At Site Date = Now + 10 days, set route to Ground and set Required Delivery Date to Need by Date minus 5 days.
# At site date is 7/15/20 -> Required Delivery date -> 7/10/20.

def funCalDeliveryDate(varSiteDate, varNowDate, varNeedByDate):
        varnow = datetime.strptime(varNowDate,'%d/%m/%y')
        print ("The type of the date is now",  type(varnow))
        print ("The date is", varnow)