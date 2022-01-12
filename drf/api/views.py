from django.shortcuts import render
from .serializers import StudentSerilizer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse # Data to be dumped into json. By default only dict objects are allowed in JsonResponse 
from .models import Student
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


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
