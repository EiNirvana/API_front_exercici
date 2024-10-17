def alumn_schema(alumne) -> dict:
    return {"IdAlumne": alumne[0],
            "IdAula": alumne[1],
            "NomAlumne": alumne[2],
            "Cicle": alumne[3],
            "Curs": alumne[4],
            "Grup": alumne[5],
            "CreatedAt": alumne[6],
            "UpdatedAt": alumne[7]  
            }

def alumnat_schema(alumnat) -> dict:
    return [alumn_schema(alumn) for alumn in alumnat]