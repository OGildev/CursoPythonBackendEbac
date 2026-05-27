


from fastapi import FastAPI, HTTPException  # type: ignore
from pydantic import BaseModel # type: ignore

app = FastAPI()

class Tarefa(BaseModel):
    nome: str
    descricao: str
    concluida: bool

tarefas = [
    Tarefa(nome="Tarefa 1", descricao="Lavar louça", concluida=False),
    Tarefa(nome="Tarefa 2", descricao="Estudar Python", concluida=False),
    Tarefa(nome="Tarefa 3", descricao="2hrs de games para curtição", concluida=False)
]

@app.get("/tarefas")
def get_tarefas():
    if not tarefas:
        return {"message": "Não existe essa tarefa."}
    else:
        return {"tarefas": tarefas}
    
@app.post("/adicionar")
def post_tarefas(tarefa: Tarefa):
    for t in tarefas:
        if t.nome == tarefa.nome:
            raise HTTPException(status_code = 400, detail = "Essa tarefa já existe!")
        
    tarefas.append(tarefa)

    return{"message": "A tarefa foi adicionada com sucesso!"}

@app.put("/atualizar/{nome}")
def put_tarefa(nome: str):
    for t in tarefas:
        if t.nome == nome:
            t.concluida = True
            return {"message": "A tarefa foi alterada com sucesso!"}
        
    raise HTTPException(status_code = 400, detail = "Essa tarefa não existe para ser atualizada!")    

@app.delete("/deletar/{nome}")
def delete_tarefa(nome: str):
    for tarefa in tarefas:
        if tarefa.nome == nome:
            tarefas.remove(tarefa)
            return {"message": "Tarefa deletada com sucesso!"}    
        
    raise HTTPException(status_code=404, detail="Não existe tarefa para ser excluída!")

