name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    if line.startswith('From:'):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1
        
bigcount = None
bigemail = None
for email, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigemail = email
    
        
print(bigemail, bigcount)
