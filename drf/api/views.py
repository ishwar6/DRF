from django.shortcuts import render
from .serializers import StudentSerilizer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from .models import Student


def student_list(request, pk):
    s = Student.objects.get(id=pk)
  #  print(s)
    serializer = StudentSerilizer(s)
  #  print(serializer)
  #  print(dir(serializer))
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = "application/json")



def student_all(request):
    s = Student.objects.all()
  #  print(s)
    serializer = StudentSerilizer(s, many=True)
  #  print(serializer)
  #  print(dir(serializer))
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = "application/json")

