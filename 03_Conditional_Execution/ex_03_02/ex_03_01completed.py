sh=input('Enter Hours: ')
sr=input('Enter Rate: ')

# 35.0 , '35.0'
fh=float(sh)
fr=float(sr)

# print(fh,fr)
Overtime = fh-40
reg=fr*fh

otp=0
if Overtime > 0:
    otp=(fh-40.0)*(fr*0.5)

xp=reg+otp

print(xp)