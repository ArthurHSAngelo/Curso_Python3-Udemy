# Ordem de precedência
# 1. (n + n) # Os () de mais de dentro são executados primeiros
# 2. **
# 3. * / // %
# 4. + - 
conta_1 = (1 + 1) ** (5 + 5) # 1024
conta_2 = (1 + int(0.5 + 0.5)) ** (5 + 5) 
print(conta_1)
print(conta_2)