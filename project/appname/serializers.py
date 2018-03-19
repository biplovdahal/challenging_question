from rest_framework import serializers
from .models import Member
 




class MemberSerializer(serializers.ModelSerializer):
	roles = serializers.SerializerMethodField()


	class Meta:
		model = Member
		fields = ('first_name','id','last_name','phone_number','email','roles')

	def get_roles(self,obj):
		return obj.get_role_display()

