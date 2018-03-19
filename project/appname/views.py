from rest_framework import viewsets
from .models import Member
from .serializers import MemberSerializer




class Members(viewsets.ModelViewSet):
	queryset = Member.objects.all()
	serializer_class = MemberSerializer

