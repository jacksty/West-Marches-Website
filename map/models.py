from django.db import models

# Create your models here.

class Map(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name

class Tag(models.Model):
    text = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.text

class Node(models.Model):
    tags = models.ManyToManyField(Tag)
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    x = models.FloatField(default = 0.0)
    y = models.FloatField(default = 0.0)
    name = models.CharField(max_length=64, unique=True)
    r = models.IntegerField(default = 5)
    fill = models.CharField(max_length=20)
    hidden = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Edge(models.Model):
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    source = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='edges_out')
    target = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='edges_in')
    weight = models.FloatField(default=0.0)
    stroke = models.CharField(max_length = 20, default='black')
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return '(' + str(self.source) + ', ' + str(self.target) + ')'
