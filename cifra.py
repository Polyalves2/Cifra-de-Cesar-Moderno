import random
import string

def criptografar(frase):
    frase = frase.lower()
    vogais = 'aeiou'
    alfabeto = string.ascii_lowercase
    resultado = ""

    for letra in frase:
        if letra == " ":
            numero = random.randint(0, 9)
            resultado += f"{numero}/"
        elif letra in alfabeto:
            pos = alfabeto.index(letra)
            if letra in vogais:
                nova_pos = (pos - 2) % 26
                resultado += f"{alfabeto[nova_pos]}/"
            else:
                nova_pos = (pos + 3) % 26
                resultado += alfabeto[nova_pos]
        else:
            resultado += letra
    return resultado

def descriptografar(frase_cripto):
    vogais_originais = 'aeiou'
    alfabeto = string.ascii_lowercase
    # Mapeia qual letra criptografada veio de vogal
    # Se vogal original -2 = criptografada, então criptografada +2 = original
    resultado = ""
    i = 0
    while i < len(frase_cripto):
        char = frase_cripto[i]

        # Verifica se tem barra depois (padrão de vogal ou espaço)
        if i + 1 < len(frase_cripto) and frase_cripto[i+1] == "/":
            if char.isdigit():
                # É um espaço
                resultado += " "
            else:
                # É uma vogal criptografada, volta +2
                if char in alfabeto:
                    pos = alfabeto.index(char)
                    pos_original = (pos + 2) % 26
                    resultado += alfabeto[pos_original]
                else:
                    resultado += char
            i += 2 # Pula a letra/número e a barra
        else:
            # É consoante, volta -3
            if char in alfabeto:
                pos = alfabeto.index(char)
                pos_original = (pos - 3) % 26
                resultado += alfabeto[pos_original]
            else:
                resultado += char
            i += 1

    return resultado

# Testando a frase
frase = "seja positivo e atraia a positividade"
cripto = criptografar(frase)
descripto = descriptografar(cripto)

print(f"Original: {frase}")
print(f"Cripto: {cripto}")
print(f"Descripto: {descripto}")