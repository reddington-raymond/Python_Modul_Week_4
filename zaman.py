import datetime

def zaman_damgasi():
    an = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return an


def iade_tarihi():
    fark=datetime.timedelta(days=14)
    iade_tarihi = datetime.datetime.today()+fark
    return iade_tarihi.strftime("%Y-%m-%d %H:%M:%S")

print(iade_tarihi())