from django.db import models

class nstracing(models.Model):
    Request_Type = models.CharField(max_length = 100)
    Path = models.CharField(max_length = 100, blank = True)
    Pin = models.CharField(max_length = 100, blank = True)
    Prog = models.CharField(max_length = 100, blank = True)
    Open_Id = models.CharField(max_length = 100, blank = True)
    #ZYQ_FileName = models.CharField(max_length = 100, blank = True)

    def __str__(self):
        return self.Request_Type
