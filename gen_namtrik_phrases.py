# GUM Data Generator
import os
import pandas as pd

outname = 'from_txt.xlsx'
outdir = './output'

verbs = [
    ['nadar','nada'],
    ['cocinar', 'nenѳ'],
    ] # Put ]erbs, names and semantic rules pattern

pronouns = {
    'yo': 'r', #na as pronominal
    'su': 'nui',
    'el': 'kѳn',
    'ellos': 'nѳm', # kѳn
    'ellas': 'nѳm',
    'nosotros': 'nam',
}

names = [
    'Jorge',
    'Camilo',
    'Esteban',
    'Monica'
]

things = {
    'arena':'pirimil',
    'tierra': 'pirѳ',
    'mar': 'nupisu',
    'fuego': 'nak',
    'trabajador': 'kuayi',
}

adjectives = {
    'cobarde': 'murkѳmik',
    'médico': 'mѳmaropik',
    'fuerte': 'mѳrik',
    'mamá': 'mama',
}

indicators = {
    'AC': 'al' # TODO: how to apply rules. This is rule 31
}

gen_spa = {
    "yo soy trabajador": "trabajador ser yo"
}

# Replaces a matching word-end from a list with other word. 
# I.e. Julián [án]-> Juliam; Caminando, Corriendo [ando, endo]-> Caminar, Correr
def replace_end(text, arr_match, replacement, preserve = False):
    if isinstance(replacement, list):
        for idx, pos_match in enumerate(arr_match):
            if text.endswith(pos_match):
                return "".join((text[:len(text)-len(pos_match)], replacement[idx])) if text.endswith(pos_match) and not preserve else text + replacement[idx]
    else:
        for pos_match in arr_match:
            if text.endswith(pos_match):
                return "".join((text[:len(text)-len(pos_match)], replacement)) if text.endswith(pos_match) and not preserve else text + replacement
    #TODO: handle possible error replacement not the same size as arr_match
    return text

# testing 
example = "Julián"
print(replace_end(example, ["án"], "am"))

consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
vocals = ["a","e","ѳ","i","o","u"]
# 1. generating on names
for name in names:
    for verb in verbs:
        print('----')
        print(f"{name} {replace_end(verb[0],['r'],'', False)}",
              f"{replace_end(name, ['án'], 'am')}pe {replace_end(verb[1],vocals,'pik',True)} kѳn", sep="\t") # present
        print(f"{name} está {replace_end(verb[0],['r'],'ndo', False)}",
              f"{replace_end(name, ['án'], 'am')}pe {replace_end(verb[1],vocals,'',True)}p unan", sep="\t") # present continous
        print(f"{name} {replace_end(verb[0],['r'],'á', True)}",
              f"{replace_end(name, ['án'], 'am')}pe {replace_end(verb[1],vocals,'n',True)}trap kѳn", sep="\t") # future
        print(f"{name} está {replace_end(verb[0],['r'],'ndo', False)}",
              f"{replace_end(name, ['án'], 'am')}pe {replace_end(verb[1],vocals,'',True)}p unikѳn", sep="\t") # past continous
        print(f"{name} {replace_end(verb[0],['ar','er','ir'],['ó','ió','ió'], False)}",
              f"{replace_end(name, ['án'], 'am')}pe {replace_end(verb[1],vocals,'n',True)}", sep="\t") # past
        
        # print(f"{name} {verb}") # past
        # print(f"{name} {verb}") # past continous
        # print(f"{name} {verb}") # future


# df = pd.DataFrame(columns =['spa', 'gum', 'origin'])

# df['origin'] = 'generated'

# if not os.path.exists(outdir):
#     os.mkdir(outdir)

# fullname = os.path.join(outdir, outname)   

# df.to_excel(fullname)