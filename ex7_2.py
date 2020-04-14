fname = input("Enter file name")
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        print(count, line)
        linez=line[20:]
liney=float(linez)
liney = (liney + liney)
pepega = liney/count
print(liney)
print (pepega)
