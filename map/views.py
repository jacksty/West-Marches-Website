from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.views.decorators.csrf import csrf_exempt

from .models import Node, Edge, Tag, Map
from .serializers import NodeSerializer, EdgeSerializer

# Create your views here.

def index(request, map=2):
    template = loader.get_template('map/index.html')
    nodes = Node.objects.filter(map=map, hidden=False)
    edges = Edge.objects.filter(map=map, hidden=False)
    nodeSerializer = NodeSerializer(nodes, many=True)
    edgeSerializer = EdgeSerializer(edges, many=True)

    context = {
        'nodes': json.dumps(nodeSerializer.data),
        'edges': json.dumps(edgeSerializer.data),
        'width': 900,
        'height': 600,
        'map': map,
    }
 
    return HttpResponse(template.render(context, request))

def edit(request, map=2):
    template = loader.get_template('map/edit.html')
    nodes = Node.objects.filter(map=map)
    edges = Edge.objects.filter(map=map)
    nodeSerializer = NodeSerializer(nodes, many=True)
    edgeSerializer = EdgeSerializer(edges, many=True)

    context = {
        'nodes': json.dumps(nodeSerializer.data),
        'edges': json.dumps(edgeSerializer.data),
        'width': 900,
        'height': 600,
        'map': map,
    }
 
    return HttpResponse(template.render(context, request))

def submit_node(request):
    name = request.POST.get('node_name', None)
    fill = request.POST.get('node_fill', 'white')
    radius = request.POST.get('node_r', 10)
    tags = request.POST.get('node_tags', '')
    map = request.POST.get('map', 1)
    hidden = request.POST.get('node_hidden', False)

    if hidden == 'on':
        hidden = True
    elif hidden == 'off':
        hidden = False

    tags = tags.split(',')
        
    node_pk = None
    map = Map.objects.get(pk=map)

    if(name):
        node = Node(name=name, fill=fill, r=radius, map=map, hidden=hidden)
        node.save()
        
        for tag in tags:
            if not Tag.objects.filter(text=tag):
                tagobj = Tag(text=tag)
                tagobj.save()
                node.tags.add(tagobj.pk)
            else:
                tagobj = Tag.objects.get(text=tag)
                node.tags.add(tagobj.pk)
    return HttpResponseRedirect("/" + str(map.id) + "/edit")



def submit_edge(request):
    source = request.POST.get('source_name', None)
    target = request.POST.get('target_name', None)
    weight = request.POST.get('weight', None)
    map = request.POST.get('map', None)
    hidden = request.POST.get('edge_hidden', False)

    if hidden == 'on':
        hidden = True
    elif hidden == 'off':
        hidden = False

    if source and target and weight and map:
        source = Node.objects.get(name=source)
        target = Node.objects.get(name=target)
        map = Map.objects.get(pk=map)

        if source and target and map:
            edge = Edge(source=source, target=target, weight=weight, map=map, hidden=hidden)
            edge.save()

    if map:
        return HttpResponseRedirect('/' + str(map.id) + "/edit")
    else:
        return HttpResponseRedirect('')



@csrf_exempt
def update_locations(request, map=1):
    body = json.loads(request.body)

    if body:
        for obj in body:
            partial = Node.objects.get(pk=obj['id'])
            partial.x = obj['x']
            partial.y = obj['y']
            partial.save()
    return HttpResponseRedirect('../')
