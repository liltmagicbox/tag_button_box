import time
def millisec():
    return str(int(time.time()*1000))
def strsec():
    return str(int(time.time()))

def intsec():
    return int(time.time())

import datetime
tzinfo=datetime.timezone(datetime.timedelta(seconds=32400))#+9
def datestr():
    now = datetime.datetime.now()
    now=now.astimezone(tzinfo)
    return now.strftime("%Y.%m.%d %H:%M:%S")

def daystr():
    now = datetime.datetime.now()
    now=now.astimezone(tzinfo)
    return now.strftime("%Y.%m.%d")

# dayholder = 0
# def isnewday(self):
#     global dayholder
#     daynow = time.localtime().tm_mday
#     if not dayholder == daynow:
#         dayholder = daynow
#         return True
#     else:
#         return False


class dayholder:
    def __init__(self):
        self.dayint = time.localtime().tm_mday
    def isnewday(self):
        daynow = time.localtime().tm_mday
        if not self.dayint == daynow:
            self.dayint = daynow
            return True
        else:
            return False
dayman = dayholder()

#datetime.datetime.utcfromtimestamp(1606644954)
#datetime.datetime(2020, 11, 29, 10, 15, 54)
#datetime.datetime.utcfromtimestamp(1606644954+(9*3600))
#datetime.datetime(2020, 11, 29, 19, 15, 54)
def datestrstamp(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp+(9*3600)).strftime("%Y.%m.%d %H:%M:%S")
