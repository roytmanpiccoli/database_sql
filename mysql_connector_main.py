# How Make request with connector SQL using python
# About PLrSOXFDHBtfFMB2Qeuej6efzZRvjRdXo8
import mysql.connector as MC

try:
    conn = MC.connect(host = 'localhost', database = 'datatest', user = 'root', password = '')
    cursor = conn.cursor()

    req = ' INSERT INTO table_name(id_name, firts_name, last_name)  VALUES(%s, %s, %s)' 
    infos = (cursor.lastrowid, 'Shikamaru', 'Roytman')
    
    cursor.execute(req, infos)
    conn.commit()
    
    req = 'SELECT * FROM table_name'  
    cursor.execute(req
                  )
    table_name = cursor.fetchall()
    for nanme1 in namelist:
      print('Prénom : {}'.format(name1[1]))
    
except MC.Error as err:
  print(err)
  finaly:
    if(conn.is_connected()):
        cursor.close()
        conn.close()
