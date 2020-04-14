counts = dict()
name = input('Enter file name')
textao = open(name)
content = textao.read()
words=content.split()
print("counting:")
for word in words:
    counts[word] = counts.get(word,0) + 1
#print('Counts', counts)
bigcounts = None
bigword = None
for word,count in counts.items():
    if bigcounts is None or count>bigcounts:
        bigword = word
        bigcounts=count
print(bigword, bigcounts)
