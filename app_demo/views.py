from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import * 


# def home(request):
#     return render(request, 'index.html')

@api_view(['GET'])
def home(request):
    student_objs = Student.objects.all()
    serializer = StudentSerializers(student_objs, many=True)
    return Response({'status': 200, 'payload':serializer.data})

@api_view(['POST'])
def post_student(request):
    
    serializer = StudentSerializers(data=request.data)
    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status':403, 'errors':serializer.errors, 'message': 'something went wrong'})
    
    serializer.save()
    return Response({'status':200, 'payload' : serializer.data , 'message':'sent'})


@api_view(['PUT'])
def update_student(request, id):
    try:
        student_obj = Student.objects.get(id=id)
        serializer = StudentSerializers(student_obj, data=request.data, partial = True)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403, 'errors':serializer.errors, 'message': 'something went wrong'})
        
        serializer.save()
        return Response({'status':200, 'payload' : serializer.data , 'message':'sent'})

    except Exception as e:
        print(e)
        return Response({'status' : 200, "message" : "invalid ID"})
    
@api_view(['DELETE'])
def delete_student(request, id):
    try:
        student_obj = Student.objects.get(id=id)
        student_obj.delete()
        return Response({'status' : 200, "message" : "deleted"})
    
    except Exception as e:
        print(e)
        return Response({'status' : 403, "message" : "invalid ID"})





