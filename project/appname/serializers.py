from rest_framework import serializers
from .models import Member
 




class MemberSerializer(serializers.ModelSerializer):
	roles = serializers.SerializerMethodField()


	class Meta:
		model = Member
		fields = ('__all__')

	def get_roles(self,obj):
		return obj.get_role_display()

