from django.shortcuts import redirect, render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Users
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
def index(request):
    return render(request,'index.html')
@api_view(['GET'])   
def api_check(request):
    apiurls = {
        'this/':'home',
        'api-auth/':'rest_framework.urls',
        'postspage/':'postpage' ,
        'postspage/<int:id>/': 'posts'
    }
    return Response(apiurls)
@api_view(['GET'])   
def api_users(request):
    user1 = Users.objects.all()
    serializer = TaskSerializer(user1 , many=True)
    return Response(serializer.data)
@api_view(['GET'])   
def api_userdetails(request,pk):
    user1 = Users.objects.get(id=pk)
    serializer = TaskSerializer(user1 , many=False)
    return Response(serializer.data)
@api_view(['POST'])
def api_createuser(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['POST'])
def api_updateuser(request,id):
    user1 = Users.objects.get(id=id)
    serializer = TaskSerializer(instance=user1 , data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def api_deleteuser(request,id):
    user1 = Users.objects.get(id=id)
    user1.delete()
    return Response("this item is successfully deleted")

