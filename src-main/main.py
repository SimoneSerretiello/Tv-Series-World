import pandas as pd
import random 
from gaoperators import *




def main():
    lista_serie=caricamentoDati()
    lista_utente, generi=carica_serie_utente(lista_serie)
    lista_serie=prepara_dataset(lista_serie, generi)
    lista, lista_codificata=inizializza(lista_serie, lista_utente)
    lista_fit=fitness(lista_utente, lista, lista_codificata)
    while True:
        lista_codificata=twoTournament(lista_fit)
        lista_codificata=crossover(lista_codificata)
        lista_codificata=mutation_inv(lista_codificata)
        lista_fit=fitness(lista_utente, lista, lista_codificata)
        if stop(lista_fit)==True:
            break 
    best=trova_result(lista_fit)
    print(stampa_result(lista_utente, lista, best))

        


if __name__=="__main__":
    main()
    inp=input()
    quit()

