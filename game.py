import random

bonecos = [""" ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||
| |/         ||
| |          ||
| |          
| |         
| |        
| |              
| |                
| |               
| |          
| |          
| |          
| |           
| |                        """,
           """ ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'.
| |        
| |              
| |                
| |               
| |          
| |          
| |          
| |           
| |                        """,
           """ ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'.
| |        /Y . 
| |       //        
| |      //          
| |     ')            
| |          
| |          
| |          
| |           
| |                        """,
           """ ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       //        \\\\
| |      //          \\\\
| |     ')            (`
| |          
| |          
| |          
| |           
| |                        """,
           """ ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\\\
| |      //  | . |  \\\\
| |     ')   |   |   (`
| |          ||'
| |          || 
| |          || 
| |          || 
| |         / |            """,
           """___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\\\
| |      //  | . |  \\\\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \\
'''''''''|           '''|   
|'|'''''''\\ \\         |'|
| |        \\ \\        | |
: :         \\ \\       : :
. .            `'       . ."""]

finalbonecos = """
''''''''''''''''''''''''''|
|'|'''''''''''''''''''''|'|
| |                     | |
: :                     : :
. .                     . ."""

get_words = open("palavras.txt").read().split()
palavra = random.choice(get_words)
letras_erradas = ""
charspuro = []
for letras in palavra:
    charspuro.append("_")


def tentativa():
    while True:
        get_letra = input("Digite uma letra: ")
        get_letra = get_letra.lower()
        if len(get_letra) != 1:
            print("Digite apenas uma letra!")
        elif get_letra in letras_erradas:
            print("Letra já digitada, tente novamente:")
        elif get_letra in charspuro:
            print("Letra já digitada, tente novamente:")
        else:
            return get_letra


def sel_boneco():
    boneco_selecionado = bonecos[sum(c.isalpha() for c in letras_erradas)]
    return boneco_selecionado


def cabecalho():
    boneco = sel_boneco()
    if letras_erradas != "":
        print(f"                            Letras tentadas: {letras_erradas}")

    if sum(x.isalpha() for x in charspuro) == 0:
        charspalavra = "_ " * len(palavra)
    else:
        charspalavra = " ".join(charspuro)

    print(f"{boneco} {charspalavra} {finalbonecos}")


def jogar_novamente():
    while True:
        get_resposta = input("Deseja jogar novamente? Sim ou Não: ").lower()
        if get_resposta != "sim" and get_resposta != "não":
            print("Digite apenas sim ou não.")
        else:
            return get_resposta


# print(palavra)
while True:
    cabecalho()
    letra_tentada = tentativa()
    indice_letras = []
    if letra_tentada in palavra:
        up = 0
        for i, letra in enumerate(palavra):
            if letra == letra_tentada:
                indice_letras.append(i)
    if not indice_letras:
        letras_erradas = letras_erradas + letra_tentada + " "
    else:
        for indice in indice_letras:
            charspuro[indice] = letra_tentada
    if len(letras_erradas) == 10:
        print(f"Game over. A palavra era {palavra}.\n{bonecos[5]}")
        resposta = jogar_novamente()
        if resposta == "não":
            break
        elif resposta == "sim":
            get_words = open("palavras.txt").read().split()
            palavra = random.choice(get_words)
            letras_erradas = ""
            charspuro = []
            for letras in palavra:
                charspuro.append("_")
    if "_" not in charspuro:
        print(f"Parabéns! Você acertou. A palavra era {palavra}.")
        resposta = jogar_novamente()
        if resposta == "não":
            break
        elif resposta == "sim":
            get_words = open("palavras.txt").read().split()
            palavra = random.choice(get_words)
            letras_erradas = ""
            charspuro = []
            for letras in palavra:
                charspuro.append("_")
