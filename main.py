import re

adn = ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
adn_str = ' '.join(adn)

long = len(adn[0])

horizontal = re.compile(r'^A{4}|T{4}|C{4}|G{4}$') 

vertical = re.compile(r'([ACTG])(.{' + re.escape(str(long)) + r'}\1){3}') 

oblicuo_desc = re.compile(r'([ACTG])(.{' + re.escape(str(long + 1)) + r'}\1){3}')

oblicuo_asc = re.compile(r'([ACTG])(.{' + re.escape(str(long - 1)) + r'}\1){3}')

expr = [horizontal, vertical, oblicuo_desc, oblicuo_asc]
result = list()

for i in expr:
    result.append((bool(i.findall(adn_str))))

if result.count(True) > 1:
    print('Es un mutante')

else:
    print('No es un mutante')