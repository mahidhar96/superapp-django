from django.db import models

# Create your models here.


class MicroApp(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    icon = models.CharField(max_length=1000)
    source = models.CharField(max_length=1000)

    def __str__(self):
        return "{id: "+str(self.id)+" name: "+self.name+" type: "+self.type+" source: "+self.source+"}"

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    transactor = models.CharField(max_length=60)
    amount = models.CharField(max_length=200)
    time = models.CharField(max_length=20)
    type = models.IntegerField()

    def __str__(self):
        return "{id: "+str(self.id)+" transactor: "+self.transactor+" amount: "+self.amount+" time: "+self.time+" type: "+str(self.type)+"}"
