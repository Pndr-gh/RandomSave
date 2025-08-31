from rest_framework import serializers

from .models import Classroom

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'
    def validate_capacity(self, value):
        if value < 5:
            raise serializers.ValidationError('error: Minimum Capacity is 5!')
        return value