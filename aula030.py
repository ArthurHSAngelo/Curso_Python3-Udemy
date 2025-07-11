"""
CONSTANTE = " Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

# maneira correta, mais legível 

velocidade_carro_passou_radar_1 = velocidade > RADAR_1

carro_passou_radar_1 = (LOCAL_1 - RADAR_RANGE) and local_carro <=(LOCAL_1 + RADAR_RANGE)

carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1

if velocidade_carro_passou_radar_1:
    print('A velocidade do carro passou do radar 1')

if carro_passou_radar_1:
    print('O Carro apenas passou no radar 1')

if carro_multado_radar_1:
    print('O carro foi multado no radar 1')



# Maneira ruim, e mais complicada de entender
if velocidade > RADAR_1:
    print('A velocidade do carro passou do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <=(LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
    print('O carro multado em radar 1')
