from rest_framework import serializers
from .models import *

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = UwpathApp
        fields =  '__all__'

class CourseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseInfo
        fields =  '__all__'


class AntireqsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Antireqs
        fields =  '__all__'


class CoreqsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coreqs
        fields =  '__all__'

class PrereqsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prereqs
        fields =  '__all__'

class RequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields =  '__all__'

class CommunicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communications
        fields =  '__all__'