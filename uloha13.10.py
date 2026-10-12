print('stvrta uloha')
a=0
b=0
c=int(input('zadaj cislo (nulu pre ukoncenie): '))
while c!=0:
    a+=c
    b+=1
    c=int(input('zadaj dalsie cislo (nulu pre ukoncenie): '))
if b>0:
    d=a/b
    print('priemer je: ',d)

input()
print('piata uloha')
e=0
f=input('zadaj slovo: ')
while not f.startswith('x'):
    e+=len(f)
    print('mozes zadat dalsie slovo')
    f=input('daj slovo: ')
print('sucet znakov je: ',e)