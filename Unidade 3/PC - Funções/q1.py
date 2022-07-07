import datetime

hour = int(input())
minute = int(input())
second = int(input())

ronda = datetime.datetime(2022, 7, 1, hour, minute, second)

acrescimos = [0, 3600, 7830, 16850, 43505]  # em segundos


def addAcrescimo(acrescimo):
    mudarData = datetime.timedelta(seconds=acrescimo)
    novaData = ronda + mudarData
    print(novaData.strftime("%H:%M:%S"))


for i in acrescimos:
    addAcrescimo(i)
