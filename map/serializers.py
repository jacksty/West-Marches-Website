from rest_framework import serializers

from .models import Node, Edge

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ('__all__')
        depth = 1

class EdgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Edge
        fields = ('__all__')
        depth = 0
