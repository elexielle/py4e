name = input('Enter file:')
if len(name) < 1 : name = 'mbox-short.txt'
handle = open(name)

count = dict()
for line in handle:
    if line.startswith('From:'): continue
    if line.startswith('From'):
        words = line.split()
        email = words[1]
        count[email] = count.get(email, 0) + 1
        #print(count.items())

largest = None
lemail = None
for email, count in count.items():
    if largest is None or count > largest:
        largest = count
        lemail = email

print(lemail, largest)
