fname = input('Enter file name:')
fh = open(fname)
count = 0
x = 0
for line in fh:
    if line.startswith('X-DSPAM-Confidence'):
        count = count + 1
        data = line
        nos = data[19:]
        fnos = float(nos)

        if x == 0:
            x = fnos
        else:
            x = x + fnos

tot = x / count
print('Average spam confidence:', tot)
