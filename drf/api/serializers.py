from rest_framework import serializers

class StudentSerilizer(serializers.Serializer):
    name = serializers.CharField(max_length=11)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    