maxTime = float(input())
times = []
aptos = []

verify = True

while verify == True:
    time = float(input())
    if time != -1:
        times.append(time)
        if times[-1] < maxTime:
            aptos.append(times[-1])
    else:
        verify = False

laps = (int(len(aptos))/8) + (1 * (len(aptos) % 8 > 0))

print(len(aptos))
print(int(laps))
