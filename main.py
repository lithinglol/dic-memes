meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "LMAO": "Mismo significado que LOL pero un nivel mas alto",
    "SKIBIDI": "Referente a la serie de internet Skibidi toilet"
}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print (meme_dict[word])
else:
    print ("Esa palabra no se encuentra en el diccionario")
