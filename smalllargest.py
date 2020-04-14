largest = None
smallest = None
while True :
 num = input('Enter a number: ')
 if num == 'done' :
  break
 try:
  snum = float(num)
 except:
  print('Invalid input')
  continue
 snum = float(num)
 if largest is None :
  largest = snum
 if smallest is None :
  smallest = snum
 if snum > largest :
  largest = snum
 if snum < smallest :
  smallest = snum
print('Maximum is', largest)
print('Minimum is', smallest)
