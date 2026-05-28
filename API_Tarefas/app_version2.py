

from fastapi import FastAPI, HTTPException, Depends # type: ignore
from fastapi.security import HTTPBasic, HTTPBasicCredentials # type: ignore
from fastapi import FastAPI, HTTPException  # type: ignore
from pydantic import BaseModel # type: ignore
import secrets
import os

app = FastAPI(
    title="API de Tarefas",
    description="API para gerenciar tarefas diárias",
    version="1.0.0",
    contact={
        "name":"Gilberto Lima",
        "email":"ogildev@gmail.com"
    }
)

USUARIO = "admin"
SENHA = "admin"

security = HTTPBasic()

def autenticacao(credentials: HTTPBasicCredentials = Depends(security)):
    is_username_correct = secrets.compare_digest(credentials.username, USUARIO)
    is_password_correct = secrets.compare_digest(credentials.password, SENHA)

    if not (is_username_correct and is_password_correct):
        raise HTTPException(
            status_code=401,
            detail="Usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Basic"},
        )

class Tarefa(BaseModel):
    nome: str
    descricao: str
    concluida: bool = False
    ordem: int = 0

tarefas = [
    Tarefa(nome="Tarefa 1", descricao="Lavar louça", concluida=False, ordem=3),
    Tarefa(nome="Tarefa 2", descricao="Estudar Python", concluida=False, ordem=2),
    Tarefa(nome="Tarefa 3", descricao="2hrs de games para curtição", concluida=False, ordem=1),
]

@app.get("/tarefas")
def get_tarefas(page: int = 1, limit: int = 10, escolha: int = 0, credentials: HTTPBasicCredentials = Depends(autenticacao)):
    if page < 1 or limit < 1:
        raise HTTPException(status_code=422, detail="Page e limit inválidos! Os valores devem ser maiores que 0.")
    
    if not tarefas:
        return {"message": "Não existe essa tarefa."}
    
    if escolha == 1:
        tarefas_ordenadas = sorted(tarefas, key=lambda t: t.ordem)
    elif escolha == 2:
        tarefas_ordenadas = sorted(tarefas, key=lambda t: t.nome)
    elif escolha == 3:
        tarefas_ordenadas = sorted(tarefas, key=lambda t: t.descricao)
    else:
        tarefas_ordenadas = tarefas

    start = (page - 1) * limit
    end = start + limit

    tarefas_paginadas = [
        {
            "nome": tarefa.nome,
            "descricao": tarefa.descricao,
            "concluida": tarefa.concluida,
            "ordem": tarefa.ordem
        }
        for tarefa in tarefas_ordenadas[start:end]
    ]

    return {
        "page": page,
        "limit": limit,
        "total_tarefas": len(tarefas),
        "tarefas": tarefas_paginadas
    }

@app.post("/adicionar")
def post_tarefas(tarefa: Tarefa, credentials: HTTPBasicCredentials = Depends(autenticacao)):
    for t in tarefas:
        if t.nome == tarefa.nome:
            raise HTTPException(status_code = 409, detail = "Essa tarefa já existe!")
        
    tarefas.append(tarefa)

    return{"message": "A tarefa foi adicionada com sucesso!"}

@app.put("/atualizar/{nome}")
def put_tarefa(nome: str, credentials: HTTPBasicCredentials = Depends(autenticacao)):
    for t in tarefas:
        if t.nome == nome:
            t.concluida = True
            return {"message": "A tarefa foi alterada com sucesso!"}
        
    raise HTTPException(status_code = 404, detail = "Essa tarefa não existe para ser atualizada!")    

@app.delete("/deletar/{nome}")
def delete_tarefa(nome: str, credentials: HTTPBasicCredentials = Depends(autenticacao)):
    for tarefa in tarefas:
        if tarefa.nome == nome:
            tarefas.remove(tarefa)
            return {"message": "Tarefa deletada com sucesso!"}    
        
    raise HTTPException(status_code=404, detail="Não existe tarefa para ser excluída!")

