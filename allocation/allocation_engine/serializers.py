from rest_framework import serializers
from allocation_engine.models import Employee_table


class employeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model=Employee_table
        fields=("id","empid", "empname","empemail","emppassword","empexp")
class empSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model=Employee_table
        fields=("empid", "empname","empemail","emppassword","empexp")

