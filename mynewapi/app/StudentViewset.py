from rest_framework import viewsets 
from .models import Student 
from .StudentSerializer import StudentSerializer 
class StudentViewset(viewsets.ModelViewSet): 
    queryset=Student.objects.all() 
    serializer_class=StudentSerializer