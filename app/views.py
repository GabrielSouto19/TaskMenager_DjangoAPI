from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app.models import Task
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def createtaskview(request):
    if request.method == "POST":
        data = json.loads(request.body)
        task = Task.objects.create(
            title=data.get("title"),
            description=data.get("description"),
            completed=data.get("completed")
        )
        return JsonResponse({"id":task.id,"message":"Task adicionada com sucesso"})



@csrf_exempt
def listtasksview(request):
    if request.method == "GET":
        tasklist = Task.objects.all().values()
        print(tasklist)
        return JsonResponse(list(tasklist),safe=False)

@csrf_exempt
def listtaskid(request,id):
    try:
        tasklist = Task.objects.get(id=id)

        tarefa = {
            "title":tasklist.id,
            "title":tasklist.title,
            "description":tasklist.description,
            "completed":tasklist.completed,
        }
        return JsonResponse(tarefa)
    except Task.DoesNotExist:
        return JsonResponse({"message":"Task não encontrada"})

@csrf_exempt
def updatetaskview(request,id):
    if request.method == "PUT":
        try:
            #captando a task correspondente a este id
            task = Task.objects.get(id=id)
            #carrega a corpo da requisição do json
            dados = json.loads(request.body)
            #atualiza os campos que forem fornecidos
            task.title = dados.get("title",task.title)
            task.description = dados.get("description",task.description)
            task.completed = dados.get("completed",task.completed)
            #Para salvar as mudanças temos que dar o comando .save()
            task.save()
            return JsonResponse({"message":"Task atualizada com sucesso"})
        except Task.DoesNotExist:
            return JsonResponse({"error":"Task não encontrada"},status=404)
   
    
@csrf_exempt
def deletetask(request,id):
    if request.method == "DELETE":
        try:
            task = Task.objects.get(id=id)
            task.delete()

            return JsonResponse({"message":"Task deletada com sucesso"})
        except DoesNotExist:
            return JsonResponse({"message":"Task não encontrada"},status=404)