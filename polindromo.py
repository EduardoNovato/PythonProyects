def palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def main():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("La palabra {} es palindromo".format(palabra))
    else:
        print("La palabra {} no es palindromo".format(palabra))


if __name__ == "__main__":
    main()
