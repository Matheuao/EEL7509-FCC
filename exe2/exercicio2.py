"""  
Crie uma função que converta uma string, contendo a
representação textual de um número inteiro, em um 
objeto do tipo int. Tal string pode não ter um preﬁxo
(indicando se tratar de um decimal) ou pode ainda ter
um dentre os preﬁxos 0b, 0o, e 0x, indicando, respectivamente,
que o número é binário, octal ou hexadecimal. A função 
deve ser capaz de identiﬁcar o preﬁxo e converter a string 
corretamente. Você deve utilizar a função int(valor, base)
para converter a string para a base desejada 
[e.g., int('10111',2) faz a conversão considerando base binária].
Posteriormente, utilize a função map() para aplicar a função criada
 a uma lista de strings contendo números em diferentes bases.
"""

def str_to_num(text : str) ->int:

    try:
        words = text.split()
        num = list(map(lambda words: int(words,0),words))

    except ValueError:
        print("The provided string does not match a valid binary, octal, hexadecimal, or decimal value.")     
        return None

    return num 

while(1):
    string = str(input())
    num = str_to_num(string)
    print(num)
    
