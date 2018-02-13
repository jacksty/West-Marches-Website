from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import json

from .models import Node, Edge, Tag
from .serializers import NodeSerializer, EdgeSerializer

# Create your views here.

def index(request, map=1):
    template = loader.get_template('map/index.html')
    nodes = Node.objects.filter(map=map)
    edges = Edge.objects.filter(map=map)
    nodeSerializer = NodeSerializer(nodes, many=True)
    edgeSerializer = EdgeSerializer(edges, many=True)

    context = {
        'nodes': json.dumps(nodeSerializer.data),
        'edges': json.dumps(edgeSerializer.data),
    }
    print(str(context))
    return HttpResponse(template.render(context, request))
