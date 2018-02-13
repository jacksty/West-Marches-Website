from django.db import models

# Create your models here.

class Map(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

class Tag(models.Model):
    text = models.CharField(max_length=64, unique=True)

class Node(models.Model):
    tags = models.ManyToManyField(Tag)
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    x = models.FloatField(default = 0.0)
    y = models.FloatField(default = 0.0)
    name = models.CharField(max_length=64, unique=True)
    r = models.IntegerField(default = 5)
    fill = models.CharField(max_length=20)
    
class Edge(models.Model):
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    source = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='edges_out')
    target = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='edges_in')
    weight = models.FloatField(default=0.0)
    stroke = models.CharField(max_length = 20)
