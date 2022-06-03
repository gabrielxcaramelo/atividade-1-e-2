a  = float(input('informe o valor do salario: ').replace(',','.'))

b  = float(input('informe o valor do aumento do salario: ').replace(',','.'))
                                                                
c = a * (b/100)
d = a+c 
print('o valor de salario vai ser de R$%.2f'%d)