from rest_framework import serializers
from .models import *
from datetime import timedelta

class OncallSerializer(serializers.ModelSerializer):
    # id = serializers.CharField(source='pk')

    def get_start(self, obj):
        return (obj.start) - timedelta(minutes=int(self.context['offset']))

    def get_end(self, obj):
        return (obj.end) - timedelta(minutes=int(self.context['offset']))

    class Meta:
        model = Oncall
        fields = ('title', 'start', 'end', 'allDay')