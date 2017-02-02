import time
from datetime import datetime, timedelta


def setcount():
    global hrs
    global mins
    global secs
    global totalsecs
    print('### vul de gevraagde waarden van de countdown timer in ###')
    hrs = int(input('uur: '))
    mins = int(input('minuten: '))
    secs = int(input('seconden: '))
    totalsecs = 3600 * hrs + 60 * mins + secs


def countdown():
    run = str(input('Start? (y/n) >'))
    # Only run if the user types in "y"
    if run == "y":
        ltotalsecs = totalsecs
        while ltotalsecs != 0:
            sec = timedelta(seconds=int(ltotalsecs))
            d = datetime(1, 1, 1) + sec
            print("%d uur %d minuten %d seconden over" % (d.hour, d.minute, d.second))
            # delay for a second
            time.sleep(1)
            # decrement the local seconds total
            ltotalsecs -= 1
            if ltotalsecs == 0:
                print('Tijd is om')

setcount()
countdown()
