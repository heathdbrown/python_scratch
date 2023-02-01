name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

lines = handle.readlines()

hours = []
for line in lines:
    if line.startswith("From:"):
        continue
    if line.startswith("From"):
        hours.append(line.split()[5].split(":")[0])


counts = sorted(list(set([(hour, hours.count(hour)) for hour in sorted(hours)])))

# reomve duplicate hour and sums
for count in counts:
    print(count[0], count[1])
