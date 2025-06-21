# Conversão de tipos, coerção, type convertion, typecasting, coercion
# Basicamente é o ato de converter um tipo em outros tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' ')) # uma string com qualquer coisa,  é considerada True
print(bool('')) # uma string sem nenhum valor, é considerada False
print(str(11) + 'b')