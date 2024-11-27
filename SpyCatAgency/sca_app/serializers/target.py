from rest_framework import serializers
from ..models import Target
from .note import NoteSerializer


class TargetSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True, read_only=True)

    class Meta:
        model = Target
        fields = ['id', 'name', 'location', 'status', 'notes']
