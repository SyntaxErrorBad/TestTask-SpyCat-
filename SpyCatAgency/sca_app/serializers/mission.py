from rest_framework import serializers
from ..models import Mission, Target
from .target import TargetSerializer


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = ['id', 'name', 'status', 'cat', 'targets']

    def create(self, validated_data):
        targets_data = validated_data.pop('targets')

        mission = Mission.objects.create(**validated_data)

        for target_data in targets_data:
            Target.objects.create(mission = mission, **target_data)

        return mission
