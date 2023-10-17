dinheiro=int(input('quantas voce ganha por horas? '))
mes=float(input('quantas horas voce trabalha por mes?'))
salario=dinheiro*mes
imposto=(11*salario)/100
inss=(8*imposto)/100
sindicato=(5*inss)/100
print('salario bruto R$ {}'.format(salario))
print('pago ao INSS: R$ {}' .format(inss))
print('pago ao sindicato: R$ {}' .format(sindicato))
print('salário liquido R$ {}' .format(salario-imposto-inss-sindicato))


