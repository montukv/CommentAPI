from rest_framework import serializers
from .models import UserComment

class commentSerializer(serializers.ModelSerializer):
		class Meta:
			model = UserComment
			#return all fields
			fields = '__all__'