
#formatēšana
#pirmā metode
print('mēs te-%s-kaut ko ieliksim'%'kaut kas',end='\n\n')

#otrā metode
print('teksta ievietošana ar.format metodi:{}'.format('hey,tev sanāca!'))

print('{0}{1}'.format('juhuuuu,','sanāca!!!!!'))
print('{1}{0}'.format('juhuuuu,','sanāca!!!!!'))

print('{a}{b}'.format(a='juhuuuu,',b='sanāca!!!!!'))

#trešā metode
#f strings, tikai python 3.6+
vards='saule'
print(f'ārā spīd {vards}')