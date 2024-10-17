from client import db_client

def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("select * from AULA")
    
        aules = cur.fetchall()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    
    return aules

def read_alumn_id(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "select * from AULA WHERE IdAula = %s"
        value = (id,)
        cur.execute(query,value)
    
        aula = cur.fetchone()

    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    
    return aula

def create(IdAula, DescAula, Edifici, Pis, CreatedAt, UpdatedAt):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "insert into AULA (IdAula, DescAula, Edifici, Pis, CreatedAt, UpdatedAt) VALUES (%s,%s,%s,%s,%s,%s);"
        values=(IdAula, DescAula, Edifici, Pis, CreatedAt, UpdatedAt)
        cur.execute(query,values)
    
        conn.commit()
        aula_id = cur.lastrowid
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()

    return aula_id

    "atalens1"