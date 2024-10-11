from django.contrib import admin
from django.urls import path
from app.views import createtaskview,listtasksview,updatetaskview,deletetask,listtaskid

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createtask/', view=createtaskview,name="create_task"),
    path('listtask/', view=listtasksview,name="list_task"),
    path('task/<int:id>', view=listtaskid,name="task"),
    path('updatetask/<int:id>', view=updatetaskview,name="update_task"),
    path('deletetask/<int:id>', view=deletetask,name="delete_task"),
]
