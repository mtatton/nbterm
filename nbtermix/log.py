DEBUG = 1


def log(logstr):
    if DEBUG == 1:
        import datetime

        now = datetime.datetime.now()
        dt = now.strftime("%Y%m%d %H:%M:%S")
        f = open("/tmp/nbtermix.log", "a")
        f.write("\n" + dt + "|" + str(logstr))
        f.close()
