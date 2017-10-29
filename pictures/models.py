from django.db import models

# Create your models here.
class Main_pic(models.Model) :
    title = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to='upload_files/main/%y/%m/%d')

class Logo_and_icons(models.Model) :
    title = models.CharField(max_length=200)
    logo = models.ImageField(blank = True, upload_to='upload_files/logo/%y/%m/%d')
    icons = models.ImageField(blank = True, upload_to='upload_files/icons/%y/%m/%d')
