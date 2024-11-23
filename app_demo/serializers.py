from rest_framework import serializers
from .models import *

class StudentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Student

        # fields = ['name', 'age']  #take only name and age
        # exclude = ['id',]  # ID is not include
        fields = '__all__'  #everything in model is included



    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError({'errors':"age can not be less than 18"})

        return data
