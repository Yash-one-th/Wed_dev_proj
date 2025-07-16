from django.db import models
# Create your models here.


# class Language(models.Model):
#     name = models.CharField(max_length=50)
#     def __str__(self):
#         return self.name

class Movie(models.Model):
    name = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    language = models.CharField(max_length=15)
    rating = models.FloatField()
    poster = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None, null=True)

    #carousal
    car_1 = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None, null=True)
    car_2 = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None, null=True)
    car_3 = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None, null=True)
    car_4 = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None, null=True)
    car_5 = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None, null=True)

    #how to include multiple genres is still work inprogress stil thinking
    genre = models.CharField(max_length=50)
    
    
    director = models.CharField(max_length=50)
    director_link = models.URLField()
    plot = models.TextField()

    #rating
    imdb = models.FloatField()
    tomatometer = models.IntegerField()
    audience_score = models.FloatField()
    meta_score = models.IntegerField()

    # cast photos and names
    pic_1=models.ImageField(upload_to="images", height_field=None, width_field=None, max_length=None, null=True,default='default.jpg' )
    cast_1=models.CharField(max_length=50, null=True,default='None')
    pic_2=models.ImageField(upload_to="images", height_field=None, width_field=None, max_length=None, null=True,default='default.jpg' )
    cast_2=models.CharField(max_length=50, null=True,default='None')
    pic_3=models.ImageField(upload_to="images", height_field=None, width_field=None, max_length=None, null=True,default='default.jpg' )
    cast_3=models.CharField(max_length=50, null=True,default='None')
    pic_4=models.ImageField(upload_to="images", height_field=None, width_field=None, max_length=None, null=True,default='default.jpg' )
    cast_4=models.CharField(max_length=50, null=True,default='None')
    pic_5=models.ImageField(upload_to="images", height_field=None, width_field=None, max_length=None, null=True,default='default.jpg' )
    cast_5=models.CharField(max_length=50, null=True,default='None')
    pic_6=models.ImageField(upload_to="images", height_field=None, width_field=None, max_length=None, null=True,default='default.jpg' )
    cast_6=models.CharField(max_length=50, null=True,default='None')
    

    #details
    Release_date = models.DateField(auto_now=False, auto_now_add=False)
    Country_of_Origin = models.CharField(max_length=50)
    Languages_Spoken = models.CharField(max_length=50)
    #technical details
    Runtime = models.DurationField()
    Sound_Mix  = models.CharField(max_length=50)
    Color = models.CharField(max_length=50)
    Aspect_Ratio = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name