name = input('Enter file:')
if len(name) < 1: name = 'mbox-short.txt'
handle = open(name)

count = dict()
for line in handle:
    if line.startswith('From:'): continue
    if line.startswith('From'):
        words = line.split()
        #print(words[5])
        time = words[5]
        #print(time)
        listime = time.split(':')
        #print(listime)
        hours = listime[0]
        hourslist = list()
        hourslist.append(hours)
        #print(hours)
    #print(hourslist)

        for hour in hourslist:
            count[hour] = count.get(hour, 0) + 1
        #print(count)

lst = list()
scount = sorted(count.items())
for key, val in scount:
    print(key, val)
