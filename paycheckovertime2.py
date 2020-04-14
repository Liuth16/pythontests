# Variaveis
xh=input('Enter hours:')
xr=input('Enter rate:')
try:
    fxh = float(xh)
    fxr=float(xr)
except:
    print('Error, please enter numeric input')
    quit()
if fxh > 40:
    #print('Overtime')
    reg=fxh*fxr
    ot=(fxh-40)*(fxr*0.5)
    xp=reg+ot
else:
    #print('Regular')
    xp=fxh*fxr
print('Pay:',xp)
