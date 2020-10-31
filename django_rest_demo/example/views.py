from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated

from . import permissions


from api.serializers import IndustrySerializer, CompanySerializer, PersonSerializer
from .models import Industry, Company, Person
# Create your views here.

# if login then update, unless just read the data.............
class IndustryView(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    permission_classes = [permissions.IsAdminOrReadOnly]   # without loging just readOnly View


# without login can't seen or update any data...........
class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

# any one can read and update data.........
class PersonView(viewsets.ModelViewSet):

    queryset = Person.objects.all()
    serializer_class = PersonSerializer

# permission to settings.py for global execution