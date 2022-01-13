from django.db.models import query
from django.shortcuts import render
from rest_framework import status
from rest_framework import serializers
from rest_framework.serializers import Serializer
from .serializers import StudentSerilizer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse # Data to be dumped into json. By default only dict objects are allowed in JsonResponse 
from .models import Student
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response


def student_list_old(request, pk):
    s = Student.objects.get(id=pk)
  #  print(s)
    serializer = StudentSerilizer(s)
  #  print(serializer)
  #  print(dir(serializer))
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = "application/json")



def student_list(request, pk):
    s = Student.objects.get(id=pk)
    serializer = StudentSerilizer(s)
    return JsonResponse(serializer.data)


def student_all(request):
    s = Student.objects.all()
  #  print(s)
    serializer = StudentSerilizer(s, many=True)
  #  print(serializer)
  #  print(dir(serializer))
    #json_data = JSONRenderer().render(serializer.data)
   # return HttpResponse(json_data, content_type = "application/json")
    return JsonResponse(serializer.data, safe = False)


@csrf_exempt
def student_create(request):
    print("s")
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        print(stream)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerilizer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            #json_data = JSONRenderer().render(res)
            #return HttpResponse(json_data, content_type = "application/json")
            return JsonResponse(res) 
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type = "application/json")



#BY USING MODEL SERIALISER

'''
class StudentSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


PATH USED: 
path('studentclass/', views.StudentAll.as_view()),
path('studentclass/<int:pk>', views.StudentAll.as_view()),
'''
class StudentAll(APIView):
    def get(self, request, pk=None, format=None):
        data = {}
        if pk is not None:
            s = Student.objects.get(id=pk)
            serializer = StudentSerilizer(s)
            return Response(serializer.data)
        s =Student.objects.all()
        serializer = StudentSerilizer(s, many=True)
        return Response(serializer.data)
    
    def post(self, request,  format=None):
        serializer = StudentSerilizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, pk, format=None):
        s = Student.objects.get(id = pk)
        serializer = StudentSerilizer(s, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data updated fully'})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def patch(self, request, pk, format=None):
        s = Student.objects.get(id = pk)
        serializer = StudentSerilizer(s, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data updated Partially'})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        s =  Student.objects.get(id = pk)
        s.delete()
        return Response({'msg':'Deleted'})





#Generic API View and ModelMixin

from rest_framework.mixins import ListModelMixin, DestroyModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.generics import GenericAPIView

class StudentMList(GenericAPIView, ListModelMixin,CreateModelMixin ):
    queryset = Student.objects.all()
    serializer_class = StudentSerilizer


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)    

#retrieve, update and delete needs a pk value to pick specific object instance. 

class StudentM_URD(GenericAPIView,  UpdateModelMixin, RetrieveModelMixin ,DestroyModelMixin ):
    queryset = Student.objects.all()
    serializer_class = StudentSerilizer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)    
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)    

