fhandle = open ('mbox-short.txt')
pinto = fhandle.read()
for lines in pinto:
    pintop=pinto.rstrip()
    print(pintop.upper())
    quit()
