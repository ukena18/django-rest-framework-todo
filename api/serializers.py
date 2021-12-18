# django library
from rest_framework import serializers
# import Task model
from .models import Task

# to turn model database to json or from json to model database
# task serializer handle the connections between both of them
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # all those fields from the model
        fields = '__all__'
