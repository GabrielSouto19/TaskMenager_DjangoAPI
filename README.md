
# TasklistDjango API

TasklistDjango é uma API RESTful simples desenvolvida com Django, sem o uso do Django Rest Framework (DRF). Esta API permite criar, listar, atualizar e deletar tarefas.

## Funcionalidades

- **Criar uma tarefa** (`POST /cratetask/`)
- **Listar todas as tarefas** (`GET /listtask/`)
- **Listar uma tarefa por ID** (`GET /task/<int:id>/`)
- **Atualizar uma tarefa** (`PUT /updatetask/<int:id>/`)
- **Deletar uma tarefa** (`DELETE /deletetask/<int:id>/`)

## Model

O projeto utiliza o seguinte modelo `Task`:

```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
```

## Views

### 1. Criar uma tarefa

```python
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from app.models import Task

@csrf_exempt
def createtaskview(request):
    if request.method == "POST":
        data = json.loads(request.body)
        task = Task.objects.create(
            title=data.get("title"),
            description=data.get("description"),
            completed=data.get("completed")
        )
        return JsonResponse({"id": task.id, "message": "Task adicionada com sucesso"})
```

### 2. Listar todas as tarefas

```python
@csrf_exempt
def listtasksview(request):
    if request.method == "GET":
        tasklist = Task.objects.all().values()
        return JsonResponse(list(tasklist), safe=False)
```

### 3. Listar uma tarefa por ID

```python
@csrf_exempt
def listtaskid(request, id):
    try:
        tasklist = Task.objects.get(id=id)
        tarefa = {
            "id": tasklist.id,
            "title": tasklist.title,
            "description": tasklist.description,
            "completed": tasklist.completed,
        }
        return JsonResponse(tarefa)
    except Task.DoesNotExist:
        return JsonResponse({"message": "Task não encontrada"})
```

### 4. Atualizar uma tarefa

```python
@csrf_exempt
def updatetaskview(request, id):
    if request.method == "PUT":
        try:
            task = Task.objects.get(id=id)
            dados = json.loads(request.body)
            task.title = dados.get("title", task.title)
            task.description = dados.get("description", task.description)
            task.completed = dados.get("completed", task.completed)
            task.save()
            return JsonResponse({"message": "Task atualizada com sucesso"})
        except Task.DoesNotExist:
            return JsonResponse({"error": "Task não encontrada"}, status=404)
```

### 5. Deletar uma tarefa

```python
@csrf_exempt
def deletetask(request, id):
    if request.method == "DELETE":
        try:
            task = Task.objects.get(id=id)
            task.delete()
            return JsonResponse({"message": "Task deletada com sucesso"})
        except Task.DoesNotExist:
            return JsonResponse({"message": "Task não encontrada"}, status=404)
```

## Endpoints

### Criar uma tarefa

- **URL**: `/createtask/`
- **Método**: `POST`
- **Body**:

```json
{
  "title": "Minha Tarefa",
  "description": "Descrição da tarefa",
  "completed": false
}
```

- **Resposta**:

```json
{
  "id": 1,
  "message": "Task adicionada com sucesso"
}
```

### Listar todas as tarefas

- **URL**: `/listtask/`
- **Método**: `GET`
- **Resposta**:

```json
[
  {
    "id": 1,
    "title": "Minha Tarefa",
    "description": "Descrição da tarefa",
    "completed": false
  },
  {
    "id": 2,
    "title": "Outra Tarefa",
    "description": "Outra descrição",
    "completed": true
  }
]
```

### Listar uma tarefa por ID

- **URL**: `/task/<int:id>/`
- **Método**: `GET`
- **Resposta**:

```json
{
  "id": 1,
  "title": "Minha Tarefa",
  "description": "Descrição da tarefa",
  "completed": false
}
```

### Atualizar uma tarefa

- **URL**: `/updatetask/<int:id>/`
- **Método**: `PUT`
- **Body**:

```json
{
  "title": "Tarefa Atualizada",
  "description": "Nova descrição",
  "completed": true
}
```

- **Resposta**:

```json
{
  "message": "Task atualizada com sucesso"
}
```

### Deletar uma tarefa

- **URL**: `/deletetask/<int:id>/`
- **Método**: `DELETE`
- **Resposta**:

```json
{
  "message": "Task deletada com sucesso"
}
```

## Como Executar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/TasklistDjango.git
```
# ATENÇÃO PARA CRIAÇÃO DOS AMBIENTES VIRTUAIS, SIGA O PASSO DE UM OU OUTRO !
2 Crie um ambiente virtual (WINDOWS):

```bash
python -m venv .venv
.venv\Scripts\activate
```

Crie um ambiente virtual (LINUX):

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Prepare as migrações:

```bash
python manage.py makemigrations
```
5. Execute as migrações:

```bash
python manage.py migrate
```

5. Inicie o servidor:

```bash
python manage.py runserver
```

5. Acesse a API em `http://localhost:8000/`.

## Observações

- Esta API utiliza views simples do Django e **não** utiliza Django Rest Framework (DRF).
- A proteção CSRF foi desativada com o decorador `@csrf_exempt` para simplificar o uso de métodos `POST`, `PUT` e `DELETE`. Em produção, considere habilitar a proteção CSRF para segurança.
- Para facilitar o processo de testes , recomendo usar a ferramenta postman
