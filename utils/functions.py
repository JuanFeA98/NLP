def riqueza_lexica(texto):
    vocabulario = sorted(set(texto))
    rl = round((len(vocabulario)) / len(texto)*100, 2)
    
    return rl  

def porcentaje_palabra(palabra, texto):
    porc_pal = f'{round(texto.count(palabra) / len(texto)*100, 2)}%'

    return porc_pal