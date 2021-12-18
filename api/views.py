# from django.shortcuts import render
# from django.http import JsonResponse
# api view decorators and response for api
from rest_framework.decorators import api_view
from rest_framework.response import Response
# serializer froms serializers.py
from .serializers import TaskSerializer
# task model
from .models import Task

# the decorator which kind of method can call
@api_view(['GET'])
def apiOverview(request):
    # api list for references
    api_urls = {
        "List": '/task-list/',
        "Detail View": '/task-detail/<str:pk>',
        "Create": '/task-create/',
        "Update": '/task-update/<str:pk>',
        "Delete": '/task-delete/<str:pk>',
    }
    # returning json response for api
    return Response(api_urls)

# the decorator which kind of method can call  or view
@api_view(['GET'])
def taskList(request):
    # get all tasks and ordered them newest to oldest
    tasks = Task.objects.all().order_by("-id")
    # and using task serializer to turn task data to json format
    # many= True means we are doing more than one data from database
    serializer = TaskSerializer(tasks, many=True)
    # our data is always serializer.data and this is json data
    return Response(serializer.data)

# the decorator which kind of method can call  or view
@api_view(['GET'])
def taskDetail(request, pk):
    # get specific dtask
    tasks = Task.objects.get(id=pk)
    #    # and using task serializer to turn task data to json format
    #     # many= False means we are doing only one data from database
    serializer = TaskSerializer(tasks, many=False)
    # our data is always serializer.data and this is json data
    return Response(serializer.data)

# the decorator which kind of method can call or view
@api_view(['POST'])
def taskCreate(request):
    # and using task serializer to turn task data to json format
    # send the data so we can create django handle everything in the backend
    serializer = TaskSerializer(data=request.data)
    # check if serializer is valid
    if serializer.is_valid():
        # then save this json data to database
        # again django handle all the logic and transformation
        serializer.save()
    # our data is always serializer.data and this is json data
    return Response(serializer.data)

# the decorator which kind of method can call or view
@api_view(['GET','POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    # and using task serializer to turn task data to json format
    # get the data so we can update our databbase
    serializer = TaskSerializer(instance=task, data=request.data)
    # django handle all the logic and transformations
    if serializer.is_valid():
        serializer.save()
    # our data is always serializer.data and this is json data
    return Response(serializer.data)

# the decorator which kind of method can call  or view
@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    # just do task delete and it should delete
    task.delete()

    return Response("IT has been Deleted")
