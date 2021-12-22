import tkinter as tk
import random
import pandas as pd
from gaop_grafici import *
#import requests



def ga():
    global lista_serie_utente
    global lista_serie
    global generi
    if len(lista_serie_utente)!=0:
        lista_serie=prepara_dataset(lista_serie, generi)
        lista, lista_codificata=inizializza(lista_serie, lista_serie_utente)
        lista_fit=fitness(lista_serie_utente, lista, lista_codificata)
        while stop(lista_fit)!=True:
            lista_codificata=roulette_wheel_selection(lista_fit)
            lista_codificata=crossover(lista_codificata)
            lista_codificata=mutation_inv(lista_codificata)
            lista_fit=fitness(lista_serie_utente, lista, lista_codificata)
        best=trova_result(lista_fit)
        mostraAschermo(lista, best)
    else:
        text_result=tk.Label(finestra,
                             text="Non hai inserito alcuna serie...",
                             font=("Helvetica", 12))
        #text_result.insert(tk.END, "Non hai inserito alcuna serie...")
        text_result.grid(row=3, column=0, sticky="WE", padx=10)

def mostraAschermo(lista, best):
    global lista_serie_utente
    text_return="Le serie che hai inserito sono: \n"
    for i in lista_serie_utente:
        text_return=text_return+str(i)+"\n"
    text_return=text_return+ "\n I consigli forniti da WorldSeriesTV sono: \n"
    for i in range(len(best)):
        if best[i]==1:
            if len(str(lista[i]))<150:
                text_return=text_return + str(lista[i]) + "\n"
            else:
                text_return=text_return+ "Titolo:"+ str(lista[i][0])+" Genere: "+str(lista[i][4])+"\n Sinossi: \n"+str(lista[i][-1])+"\n"+"\n"
    text_return=text_return+"\n A presto!"
    text_result=tk.Label(finestra,
                         text=text_return,
                         font=("Helvetica", 12))
    #text_result.insert(tk.END, text_return)
    text_result.grid(row=3, column=0, sticky="S", padx=10)

def carica_serie_utente():
    global lista_serie
    global lista_serie_utente
    global generi
    if serie_tv_inp.get():
        inp=serie_tv_inp.get()
        inp=inp.lower()
        aggiungi=cerca_serie(lista_serie,inp)
        if aggiungi in lista_serie_utente:
            text_return="Serie già selezionata"
        elif aggiungi != None:
            lista_serie_utente.append(aggiungi)
            generi_aggiungi=aggiungi[4].split(", ")
            if generi_aggiungi[0] not in generi:
                generi.append(generi_aggiungi[0])
            if generi_aggiungi[1] not in generi:
                generi.append(generi_aggiungi[1])
            if generi_aggiungi[-1] not in generi:
                generi.append(generi_aggiungi[-1])
            
            text_return="E' stata aggiunta la serie "+ str(aggiungi[0])
        elif aggiungi == None:
            text_return="Serie non trovata..."        
    else:
        text_return="Inserisci la serie nella barra dedicata!"
    serie_tv_inp.delete("0", "end")
    text_result=tk.Label(finestra,
                         text=text_return,
                         font=("Helvetica",12))
    #text_result.insert(tk.END, text_return)
    text_result.grid(row=3, column=0, sticky="WE", padx=10)

def cerca_serie(lista_serie, inp):
    for i in range(len(lista_serie.Series_Title)):
        if lista_serie.Series_Title[i].lower()==inp:
            aggiungi=[lista_serie.Series_Title[i], lista_serie.Runtime_of_Series[i], lista_serie.Certificate[i], lista_serie.Runtime_of_Episodes[i], lista_serie.Genre[i], lista_serie.IMDB_Rating[i], lista_serie.Star1[i], lista_serie.Star2[i]]
            return aggiungi
    return None

def caricamento_dati():
    dat=pd.read_csv("series_data.csv")
    return dat



lista_serie=caricamento_dati()
lista_serie_utente=[]
generi=[]

finestra= tk.Tk()
finestra.geometry("1024x900")
#finestra.attributes("-fullscreen", True)
finestra.title("TvSeriesWorld")
finestra.grid_columnconfigure(0, weight=1)

benvenuto_label= tk.Label(finestra,
                          text="Inserisci qui il titolo di una serie tv che hai visto!",
                          font=("Helvetica", 15))
benvenuto_label.grid(row=0, column=0, sticky="N", padx=20)

serie_tv_inp=tk.Entry()
serie_tv_inp.grid(row=1, column=0, sticky="WE", padx=10)

#Inserisci e crea carica serie utente
invia=tk.Button(text="INVIA", command=carica_serie_utente)
invia.grid(row=2, column=0, sticky="E", padx=10)

consiglia=tk.Button(text="CONSIGLIA", command=ga)
consiglia.grid(row=2, column=0, sticky="E", padx=60)

#Inserisci e crea funzione ELIMINA
elimina=tk.Button(text="ELIMINA")
elimina.grid(row=4, column=0, sticky="WE", padx=20, pady=380)


if __name__=="__main__":
    finestra.mainloop()
