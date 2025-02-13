"""
All your application modules and serializers are going to be declared inside this file
"""
from rest_framework import serializers
from django.db import models

"""
Define he Contact Entity into your applcation model
"""


class Todo(models.Model):
    label = models.CharField(max_length=200, default='')
    done = models.BooleanField(default=False)


"""
The ContactSerializer is where you will specify what properties
from the ever Contact should be inscuded in the JSON response
"""


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # what fields to include?
        fields = ('id', 'label', 'done',)
