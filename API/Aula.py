def aula_schema(aula) -> dict:
    return {"Idaula": aula[0],
            "DescAula": aula[1],
            "Edifici": aula[2],
            "Pis": aula[3],
            "CreatedAt": aula[4],
            "UpdatedAt": aula[5]  
            }

def aules_schema(alumnat) -> dict:
    return [aula_schema(classe) for classe in alumnat]