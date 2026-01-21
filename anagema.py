import random

def e_anagrama():
    primeiro_nome = input('Digite a primeira palavra: ')
    segundo = input('Segunda palavra: ')

    if len(primeiro_nome) != len(segundo):
        print('Não tem como ser um anagrama, têm quantidades diferentes de letras.')
        return False

    if sorted(primeiro_nome) == sorted(segundo):
        print('São anagramas')
        print('Vou reorganizar')

        p_numero1 = list(primeiro_nome)
        random.shuffle(p_numero1)
        print("".join(p_numero1))

        p_numero2 = list(segundo)
        random.shuffle(p_numero2)
        print("".join(p_numero2))

        return True
    else:
        print('Não são anagramas, pois possuem letras diferentes')
        return False
    
e_anagrama()
