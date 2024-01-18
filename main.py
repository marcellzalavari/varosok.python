from varosok import *

beolvas('varosok.txt')

print(f'3. feladat: Városok száma: {len(varosok)} db')

print(f'4. feladat: indiai nagyvárosok lakosságának összege: {orszag_lakossaga("India")} fő')

legnagyobb=legnagyobb_varos()
print('5. feladat: Legnagyobb város adatai: ')
print(f'\tNév: {legnagyobb.varos}')
print(f'\tOrszág: {legnagyobb.orszag}')
print(f'\tLakosság: {legnagyobb.lakossag} ezer fő')

if orszag_keres('Magyarország'):
    print(f'6. feladat: Van magyar város az adatok között')
else:
    print(f'6. feladat: Nincs magyar város az adatok között')

print(f'7. feladat: Városok egy szóközzel: {szokozos_varosok(1)} db')
print(f'7.1 feladat: Városok kettő szóközzel: {szokozos_varosok(2)} db')
print(f'7.2 feladat: Egy szóból álló városnevek: {szokozos_varosok(0)} db')

print('8. feladat: Ország statisztika')
for key,value in orszag_statisztika().items():
    if value>6:
        print(f'\t{key} {value} db')

print('9. feladat: kina.txt')
orszag_mentes('kina.txt','Kína')

# Legnagyobb lakosságú város bizonyos országból (ha biztos, hogy van olyan ország)
legnagyobb=legnagyobb_varos_orszagban('Kína')
print('10. feladat: A legnagyobb kínai város adatai: ')
print(f'\tNév: {legnagyobb.varos}')
print(f'\tOrszág: {legnagyobb.orszag}')
print(f'\tLakosság: {legnagyobb.lakossag} ezer fő')

# Legnagyobb lakosságú város bizonyos országból ha nem biztos hogy van olyan ország

orszag=input('11. feladat: Melyik ország legnagyobb városára kíváncsi? ')
if legnagyobb_varos_orszagban2(orszag)==False:
    print('\tNincs ilyen ország az adatok között!!')
else:
    legnagyobb=legnagyobb_varos_orszagban2(orszag)
    print('A legnagyobb város adatai: ')
    print(f'\tNév: {legnagyobb.varos}')
    print(f'\tOrszág: {legnagyobb.orszag}')
    print(f'\tLakosság: {legnagyobb.lakossag} ezer fő')