import json

try:
    with open('conf_voo.json', 'r') as arquivo:
        dados_lidos = json.load(arquivo)
        #O json.load, basicamente, carrega as infomações

    print('Configurações:')
    print(f'O nome do drone: {dados_lidos['nome_drone']}')
    print(f'Sua baterias max: {dados_lidos['bateria_max']}')

    lista_organizada = ', '.join(dados_lidos['sensores'])
    print(f'Seus sensores: {lista_organizada}')
    print(f'Ganhos de kp: {dados_lidos['ganhos_PID']['kp']}')

except FileNotFoundError:
    print('Arquivo não encontrado')

