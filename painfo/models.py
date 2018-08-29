from django.db import models
#from django.contrib.auth.models import User


def get_image_filename(instance, filename):
    title=instance.uhid
    title1 = instance.ipno
 #   print(str(title),"==aasdanlksnflkasdnlkasndlkasnslkfnalksdddddddddddddddddddddddd")
   # slug=slugify(title)
    # return 'images/'+str(title)+"/"%(title, filename)
    # print ("jhjhgj==================")
    return 'painfo/static/images/%s/%s/%s'%(title,title1,filename)


class Painf(models.Model):
    name = models.CharField(max_length=250,null=False)
#    ipno = models.CharField(max_length=250,null=False)
    uhid = models.CharField(max_length=250,unique=True)
#    types = models.CharField(max_length=250,null=False)
#    dep = models.CharField(max_length=250,null=False)
    date=models.DateField()
#    doc = models.ImageField(upload_to=get_image_filename)

#make uhid unique key (check its working or not)
class docs(models.Model):
    post = models.ForeignKey(Painf,on_delete=models.CASCADE)
    uhid = models.CharField(max_length=250)
    ipno = models.CharField(max_length=250)
    date = models.DateField()
    doc = models.FileField(upload_to=get_image_filename)

class ipnos(models.Model):
    post= models.ForeignKey(Painf,on_delete=models.CASCADE)
    date = models.DateField()
    ipno=models.CharField(max_length=250,unique=True)
    uhid = models.CharField(max_length=250)
    types = models.CharField(max_length=250, null=False)
    dep = models.CharField(max_length=250, null=False)