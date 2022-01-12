from rest_framework import serializers

from .models import Student

class StudentSerilizer(serializers.Serializer):
  #  id = serializers.IntegerField()
    name = serializers.CharField(max_length=11)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    
    def create(self, data):
        return Student.objects.create(**data)