import re
import sqlite3

pattern1 = "lex\((\w*),"
pattern2 = "CAT=(\w*)"

con = sqlite3.connect('frases.db')

cur = con.cursor()

cur.execute(
    '''SELECT 
            palavra 
        FROM palavras p 
            WHERE p.categoria IN ('v') ORDER BY RANDOM() LIMIT 1
    ''')

verbo = cur.fetchone()[0]

cur.execute(
    '''SELECT 
            palavra 
        FROM palavras p 
            WHERE p.categoria IN ('art') ORDER BY RANDOM() LIMIT 1
    ''')

artigo = cur.fetchone()[0]

cur.execute(
    '''SELECT 
            palavra 
        FROM palavras p 
            WHERE p.categoria IN ('a_nc','nc') ORDER BY RANDOM() LIMIT 1
    ''')

substantivo = cur.fetchone()[0]


print(verbo + " " + artigo + " " + substantivo)
