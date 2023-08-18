import os
import pandas as pd

df = pd.DataFrame([], columns=['spa_text','origin_details'])

inputfilename='biblia_nt_esp_dhhdk.csv'
outname = 'v2.xlsx'
outdir = './output'

target = []
with open(f"v2/{inputfilename}", encoding='latin-1') as f:
    lines = f.readlines()
    for line in lines:
        line = str(line).replace('\n','')
        if len(line) > 0:
            target.append(line)

books = [
['San Mateo',28],
['San Marcos',16],
['San Lucas',24],
['San Juan',21],
['Hechos',28],
['Romanos',16],
['1 Corintios',16],
['2 Corintios',13],
['Gálatas',6],
['Efesios',6],
['Filipenses',4],
['Colosenses',4],
['1 Tesalonicenses',5],
['2 Tesalonicenses',3],
['1 Timoteo',6],
['2 Timoteo',4],
['Tito',3],
['Filemón',1],
['Hebreos',13],
['Santiago',5],
['1 Pedro',5],
['2 Pedro',3],
['1 Juan',5],
['2 Juan',1],
['3 Juan',1],
['Judas',1],
['Apocalipsis',22]
]

for book in books:
    book_name = book[0]
    book_chapters = book[1]
    book_chapter_indexes = []
    for book_chapter in range(1, book_chapters+1):
        book_title = f'{book_name} {book_chapter}'
        book_chapter_indexes.append(target.index(book_title))

    print(book_chapter_indexes)
    chapters = []
    for idx in range(0,len(book_chapter_indexes)):
        chapter_index = book_chapter_indexes[idx]+1
        if(idx + 1 < len(book_chapter_indexes)):
            index_before_next_book = book_chapter_indexes[idx + 1]
            # chapters.append(target[chapter_index:index_before_next_book])
            new_df = pd.DataFrame([], columns=['spa_text','origin_details'])
            new_df['spa_text'] =  target[chapter_index:index_before_next_book]
            new_df['origin_details'] = target[book_chapter_indexes[idx]]
        # for chapter in chapters:
        #     file_df = pd.DataFrame(list(zip(chapter, source_lines, )),
        #         columns =['verses', 'source'])
        #     file_df['origin'] = file
            df = pd.concat([df, new_df])

    print(df)
# Save to TXT
# with open(f'cleaned_{inputfilename}.txt', 'w', encoding="utf-8") as f:
#     for line in lines: 
#         f.write(line)
#         f.write('\n')

if not os.path.exists(outdir):
    os.mkdir(outdir)

fullname = os.path.join(outdir, outname)   

df.to_excel(fullname)