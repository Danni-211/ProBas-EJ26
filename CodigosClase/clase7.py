def imprime_lista(lista):
    """Imprime el parametro lista"""
    if isinstance(lista, list):
        for i in range(0, len(lista)):
            print(lista[i])

miLista = ["mango", "papaya", "piña", "sandía"]
imprime_lista(miLista)
