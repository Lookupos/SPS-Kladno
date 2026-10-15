x = "5"
y = "50"
string = "SOučEt ČíseL x = {} a Y = {} Je {}"
### řádky výše NEMĚNIT ###
# Váš kód sem 👇
x = int(x)
y = int(y)

x = x * y

string = string.lower()
string = string.format(x, y, x)