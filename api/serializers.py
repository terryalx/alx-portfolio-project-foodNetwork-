from rest_framework import serializers
# from ..webapp.models import all_resturant
from webapp.models import all_resturant



class AllModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = all_resturant
        fields = '__all__'
