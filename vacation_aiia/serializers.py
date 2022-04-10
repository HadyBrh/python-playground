from rest_framework import serializers
from .models import Vacation

class VacationSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Vacation
        fields = (
            'title', 'description', 'from_date', 'to_date'
        )