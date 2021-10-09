import re
import sqlite3

pattern1 = "lex\((\w*),"
pattern2 = "CAT=(\w*)"

con = sqlite3.connect('frases.db')

cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS palavras (
  palavra text,
  categoria text
);

''')



linhas = []
with open('resultado.txt') as res:
    linhas = res.readlines()


conjunto = set()
plv_cat = ()
for linha in linhas:
    try:
        palavra = re.search(pattern1, linha).group(1)
        categoria = re.search(pattern2, linha).group(1)
        plv_cat = (palavra, categoria)
        conjunto.add(plv_cat)
    except:
        print(linha)


cur.executemany("INSERT INTO palavras VALUES (?,?)", conjunto)

con.commit()

con.close()
