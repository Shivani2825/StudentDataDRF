from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import Students  
from .serializers import StudentSerializer  
from django.shortcuts import get_object_or_404  
  
class StudentView(APIView):  
    def get(self, request, id=None):  
        if id is not None:  
            result = Students.objects.get(id=id)  
            serializer = StudentSerializer(result)  
            return Response({'status': 'success', "student": serializer.data}, status=status.HTTP_200_OK)  
  
        results = Students.objects.all()  
        serializer = StudentSerializer(results, many=True)  
        return Response({'status': 'success', "students": serializer.data}, status=status.HTTP_200_OK)  
  
    def post(self, request):  
        serializer = StudentSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def patch(self, request, id):  
        result = Students.objects.get(id=id)  
        serializer = StudentSerializer(result, data = request.data, partial=True)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data})  
        else:  
            return Response({"status": "error", "data": serializer.errors})  
        

    def delete(self, request, id=None):  
        result = get_object_or_404(Students, id=id)  
        result.delete()  
        return Response({"status": "success", "data": "Record Deleted"})  