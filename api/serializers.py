from rest_framework.serializers import ModelSerializer
from .models import Equipment, Court, Timeslot


class EquipmentSerializer(ModelSerializer):
    class Meta:
        model = Equipment
        feilds = "__all__"
        exclude = []


class CourtSerializer(ModelSerializer):
    class Meta:
        model = Court
        feilds = "__all__"
        exclude = []


class TimeslotSerializer(ModelSerializer):
    class Meta:
        model = Timeslot
        feilds = "__all__"
        exclude = []
