import pandas as pd
import math
 
# read by default 1st sheet of an excel file
df = pd.read_excel('dirty/biblia_esp_gum.xlsx')
df = df.dropna()
new_df = pd.DataFrame([], columns=['spa_text', 'gum_text', 'origin', 'origin_details'])

book = 'Mateo 1' # first book

for ind in df.index:
    spa_text = str(df['Mateo 1'][ind]).split(u'\xa0', 2)
    gum_text = str(df['Mateo 1.1'][ind]).split(u'\xa0', 2)

    if len(spa_text) > 1 and len(gum_text) > 1:
        origin_details = book + ' - ' + spa_text[1]
        new_df.loc[len(new_df.index)] = [spa_text[2], gum_text[2], 'bible', origin_details]
    else:
        if spa_text[0] == gum_text[0]:
            book = df['Mateo 1'][ind]
        else:
            if len(spa_text) > 1:
                #gum no tienen \xa0
                origin_details = book + ' - ' + spa_text[1]
                new_df.loc[len(new_df.index)] = [spa_text[2], gum_text[0].split(' ', 1)[1], 'bible', origin_details]
            else:
                #esp no tienen \xa0 
                origin_details = book + ' - ' + gum_text[1]
                new_df.loc[len(new_df.index)] = [spa_text[0].split(' ', 1)[1], gum_text[2], 'bible', origin_details]

print(new_df.head())
new_df.to_excel("dataset/spa-gum_bible.xlsx")
new_df.to_csv("dataset/spa-gum_bible.csv")
