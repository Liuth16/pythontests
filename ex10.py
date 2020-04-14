fname = input("Enter file name: ")
handle = open(fname)
di = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    for w in words:
        di[w] = di.get(w, 0) +1
#print(di)

inversao = list()
for k, v in di.items():
    newlista = (v,k)
    inversao.append(newlista)
#print(inversao)
inversao = sorted(inversao, reverse=True)
#print(inversao[:5])

for v,k in inversao[:5]:
    print(k,v)
