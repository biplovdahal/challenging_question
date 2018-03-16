from django.shortcuts import render
 
from rest_framework import viewsets
from .models import Member
from .serializers import MemberSerializer

from rest_framework.views import APIView, Response
import json 


class Members(APIView):


	def get(self, request, format=None):
		members = Member.objects.all()
		serializer = MemberSerializer(members, many=True)
		return Response(serializer.data)


	def post(self, request, format=None):
		payload = request.POST.dict()
		try:
			first_name = payload['first_name']
			last_name = payload['last_name']
			phone_number = payload['phone_number']
			email = payload['email']
			role = payload['role']
			createMember = Member(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email, role=role)
			createMember.save()
			serializer = MemberSerializer(createMember)
			return Response(serializer.data)
		except KeyError as e:
			return Response('missing key: '+ e.args[0])


	def put(self, request, format=None):
		payload = request.POST.dict()
		try:
			user_id = payload.get('id')
			if user_id:
				payload.pop('id') 
				member = Member(id=user_id, **payload)
				member.save()
				serializer = MemberSerializer(member)
				return Response(serializer.data)
			else:
				return Response("this user does not exists!")
		except:
			return Response('uh.. oh something went wrong')


	def delete(self, request, format=None):
		payload = request.POST.dict()
		try:
			user_id = payload.get('id')
			if user_id:
				member = Member(id=user_id).delete()
				return Response('')
			else:
				return Response('You must pass valid user id to update!')
		except:
			return Response('uh.. oh something went wrong')

	
		

		