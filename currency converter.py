#################################
######CURRENCY CONVERTOR#########
#################################

from forex_python.converter import CurrencyRates

c = CurrencyRates()
amount = int(input('Please enter the amount to be converted: '))
form_currency = input('Please enter form which currency to convert: ').upper()
to_currency = input('Please specify the currency tha target currency:').upper()

print(f'the amount of:', amount, 'converted from :', form_currency, 'to:', to_currency)
result = c.convert(form_currency, to_currency, amount)
print('Conversion result ist:','{:.3f}'.format(result))
