import os
import pandas as pd

df = pd.DataFrame([], columns=['spa_text','origin_details'])

inputfilename='biblia_nt_esp_dhhdk.csv'
outname = 'from_txt.xlsx'
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
# ['marcos','MRK',16],
# ['lucas','LUK',24],
# ['juan','JHN',21],
# ['hechos','ACT',28],
# ['romanos','ROM',16],
# ['1 corintios','1CO',16],
# ['2 corintios','2CO',13],
# ['galatas','GAL',6],
# ['efesios','EPH',6],
# ['filipenses','PHP',4],
# ['colosenses','COL',4],
# ['1 tesalonicenses','1TH',5],
# ['2 tesalonicenses','2TH',3],
# ['1 timoteo','1TI',6],
# ['2 timoteo','2TI',4],
# ['tito','TIT',3],
# ['filemon','PHM',1],
# ['hebreos','HEB',13],
# ['santiago','JAS',5],
# ['1 pedro','1PE',5],
# ['2 pedro','2PE',3],
# ['1 juan','1JN',5],
# ['2 juan','2JN',1],
# ['3 juan','3JN',1],
# ['judas','JUD',1],
# ['apocalipsis','REV',22]
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