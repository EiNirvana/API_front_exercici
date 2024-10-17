#resolucio de la practica 2

from typing import List
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import Alumne, db_alumnes
# import Aula, db_aules

class tablaAlumne (BaseModel):
    NomAlumne:str
    Cicle:str
    Curs: int
    Grup: str
    DescAula:str

@app.get("/")
def read_root():
    return {"Alumntat API"}

@app.put("/alumne/listAll",  response_model=List[tablaAlumne])
async def read_alumn_aula():
    read_list = db_alumnes.list_alumn_aula(orderby: str | None = None,  contain: str | None = None, 
                    skip: int = 0, limit: int | None = None);
    


#consultar, no funciona
#una conexió entre classe i alumne, només imprimir certs aspectes
#print from AULES when idAlumne = %s???