from client import db_client

def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("select * from ALUMNE")
    
        alumnes = cur.fetchall()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    
    return alumnes

def read_id(IdAlumne):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "select * from ALUMNE WHERE IdAlumne = %s"
        value = (IdAlumne)
        cur.execute(query,value)
    
        alumne = cur.fetchone()

    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    
    if alumne is None:
        return None
    
    return alumne

def create(IdAula, NomAlumne, Cicle, Curs, Grup, CreatedAt, UpdatedAt):
    try:
        conn = db_client()
        cur = conn.cursor()
        alumne_id = cur.lastrowid
        query = "insert into ALUMNES (alumne_id, IdAula, NomAlumne, Cicle, Curs, Grup, CreatedAt, UpdatedAt) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
        values=(alumne_id, IdAula, NomAlumne, Cicle, Curs, Grup, CreatedAt, UpdatedAt)
        cur.execute(query,values)
    
        conn.commit()
        
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()

    return alumne_id

def update_alumn(IdAula, NomAlumne, Cicle, Curs, Grup, CreatedAt, UpdatedAt, id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "update ALUMNES SET IdAula = %s, NomAlumne = %s, Cicle = %s, Curs = %s, Grup = %s, CreatedAt = %s, UpdatedAt = %s  WHERE id = %s;"
        values=(IdAula, NomAlumne, Cicle, Curs, Grup, CreatedAt, UpdatedAt, id)
        cur.execute(query,values)
        updated_alum = cur.rowcount
    
        conn.commit()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()

    return updated_alum

def delete_alumn(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "DELETE FROM ALUMNES WHERE id = %s;"
        cur.execute(query,(id,))
        deleted_alum = cur.rowcount
        conn.commit()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
        
    return deleted_alum

def list_alumn_aula(orderby: str | None = None,  contain: str | None = None, 
                    skip: int = 0, limit: int | None = None):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = """
                SELECT alumn.NomAlumne, alumn.cicle, alumn.grup, alumn.curs, alumn.grup, classe.DescAula
                FROM alumn 
                JOIN aula ON alumn.IdAula = aula.IdAula
                """
        if limit is not None:
            query += f" LIMIT {limit} OFFSET {skip}"

        cur.execute(query)
        list_alum = cur.fetchall()

    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    finally:
        cur.close()
        conn.close()

    return list_alum