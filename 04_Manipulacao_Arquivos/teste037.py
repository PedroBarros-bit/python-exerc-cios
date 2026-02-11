import json

conf_drone = {
    'nome_drone': 'Hidrone-J',
    'bateria_max': 100,
    'sensores': ['Giroscópio', 'Acalerometro', 'GPS'],
    'ganhos_PID': {
        'kp': 12.5,
        'ki': 0.05,
        'ka': 4.2
    }
}

with open('conf_voo.json', 'w') as arquivo:
    json.dump(conf_drone, arquivo, indent=4)
    #indent=4 deixa o arquivo indentado para ler depois
print('Configuração salva')

