
#elementi var tikt mainīgi

#definēšana notiek ar {}
my_list=[1,2,3]
print(my_list,'\n')

#var būt gan skaitļi,gan teksts
your_list=['teksts',2,3.5]
print(your_list,'\n')

#var izmantot funkciju len
print('Lenght my_list:',len(my_list),'\n')

#var izmantot index
print('mainīgā list pirmais elements:',my_list[0])
print('mainīgā list pirmais elements:',your_list[0])

#elementa maiņa
my_list[0]='NOMAINĪJU'
print(my_list,'\n')

#jauna elementa pievienošana
print(my_list+['JAUNUMS'])
print(my_list)

my_list=my_list+['JAUNUMS']
print(my_list)