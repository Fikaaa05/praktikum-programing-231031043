print('praktikum-3\n\n')

print('NAMA : Nur safikah')
print('NIM  : 231031043')
print('prodi: sistem informasi B\n')

##########################################
a = True
b = False


print('============NXOR============')
hasil = not(a ^ a)
print(a,'nxor',a,'adalah=',hasil)      
hasil = not (a ^ b)
print(a,'nxor',b,'adalah=',hasil)       
hasil = not (b ^ a)
print(b,'nxor',a,'adalah=',hasil)      
hasil = not (b ^ b)
print(b,'nxor',b,'adalah=',hasil)


print('============NXOR============')
hasil = not(a ^ a)
print(a,'nxor',a,'adalah=',hasil)      
hasil = not (a ^ b)
print(a,'nxor',b,'adalah=',hasil)       
hasil = not (b ^ a)
print(b,'nxor',a,'adalah=',hasil)      
hasil = not (b ^ b)
print(b,'nxor',b,'adalah=',hasil)

# ini operator membership
print('============ IN ============')
nama = 'fika'

test = 'ka'# isi nama dengan 2 huruf di nama
cek = test in nama
print(test,'ada di',nama,'adalah=',cek)
      
test = 'ak'# isi nama dengan 2 huruf di nama
cek = test in nama
print(test,'ada di',nama,'adalah=',cek)     

test1 ='a'
test2 ='i'
test3 ='u'
test4 ='e'
test5 ='o'

cek = test1 in nama
print(test1,'ada di',nama,'adalah=',cek)
cek = test2 in nama
print(test2,'ada di',nama,'adalah=',cek)
cek = test3 in nama
print(test3,'ada di',nama,'adalah=',cek)
cek = test4 in nama
print(test4,'ada di',nama,'adalah=',cek)
cek = test5 in nama
print(test5,'ada di',nama,'adalah=',cek)

#ini operator bitwise
print('\n')
a= 18#Tanggal lahir
b= 9#Bulan lahir
a+=60
b+=80
print('==========AND==========')
print('Nilai',a,'biner adalah=',format(a,'08b'))
print('Nilai',b,'biner adalah=',format(b,'08b'))
print('==========================AND')
c= a&b
print('Nilai',a,'&',b,'biner adalah=',format(c,'08b'))


print('==========OR==========')
print('NIlai', a, 'biner adalah =', format(a,'09b'))
print('NIlai', b, 'biner adalah =', format(b,'09b'))
print('-----------------------------------------OR')
c = a | b
print('Nilai', a, '||', b, 'biner adalah =', format(c, '09b'))
           
print('==========XOR==========')
print('NIlai', a, 'biner adalah =', format(a,'09b'))
print('NIlai', b, 'biner adalah =', format(b,'09b'))
print('-----------------------------------------XOR')
c = a ^ b
print('Nilai', a, 'xor', b, 'biner adalah =', format(c, '09b'))

print('\==========NOT==========')     
C=~a
print('Nilai ',a,'biner adalah =',format(c,'09b'))
print('Nilai not',a,'biner adalah =',format(c,'09b'))
print('\n==========left shif==========')
c=a << 2
print('Nilai ',a,'biner adalah =',format(a,'09b'))
print('Nilai ',a,'<< 2 adalah =',format(c,'09b'))

c=b << 2

print('Nilai ',b,'biner adalah =',format(a,'09b'))
print('Nilai ',b,'<< 2 adalah =',format(c,'09b'))
c
c=a << 2
print('Nilai ',a,'biner adalah =',format(a,'09b'))
print('Nilai ',a,'>> 2 biner adalah =',format(c,'09b'))

c=b << 2

print('Nilai ',b,'biner adalah =',format(b,'09b'))
print('Nilai ',b,'>> 2 biner adalah =',format(c,'09b'))

print('\n==========Right shif==========')
c=a << 2
print('Nilai ',a,'biner adalah =',format(a,'09b'))
print('Nilai ',a,'<< 2 adalah =',format(c,'09b'))

c=b << 2

print('Nilai ',b,'biner adalah =',format(a,'09b'))
print('Nilai ',b,'<< 2 adalah =',format(c,'09b'))

####################################################
print()
print('=======NOT AND===========')
print('NIlai', a, 'biner adalah =', format(a,'09b'))
print('NIlai', b, 'biner adalah =', format(b,'09b'))
print('-----------------------------------------NOT AND')
c = ~(a & b)
print('Nilai', a, 'not and', b, 'biner adalah =', format(c, '09b'))
print()

print('==========NOT OR==========')
print('NIlai', a, 'biner adalah =', format(a,'09b'))
print('NIlai', b, 'biner adalah =', format(b,'09b'))
print('-----------------------------------------NOT OR')
c = ~(a | b)
print('Nilai', a, 'not and', b, 'biner adalah =', format(c, '09b'))
print()

print('==========NOT XOR==========')
print('NIlai', a, 'biner adalah =', format(a,'09b'))
print('NIlai', b, 'biner adalah =', format(b,'09b'))
print('-----------------------------------------NOT XOR')
c = ~(a ^ b)
print('Nilai', a, 'not xor', b, 'biner adalah =', format(c, '09b'))
print()

print('==========NOT<<2 ==========')
c = ~(a << 2)
print('Nilai', a, 'biner adalah =', format(a, '09b'))
print('Nilai',a, 'not << 2 biner adalah =', format(c, '09b'))

c = ~(b << 2)
print('Nilai', b, 'biner adalah =', format(b, '09b'))
print('Nilai',b, 'not << 2 biner adalah =', format(c, '09b'))
print()

print('==========NOT>>2 ==========')
c = ~(a >> 2)
print('Nilai', a, 'biner adalah =', format(a, '09b'))
print('Nilai',a, 'not >> 2 biner adalah =', format(c, '09b'))

c = ~(b >> 2)
print('Nilai', b, 'biner adalah =', format(b, '09b'))
print('Nilai',b, 'not >> 2 biner adalah =', format(c, '09b'))
