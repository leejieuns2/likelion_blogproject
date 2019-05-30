from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 20, default='제목없음') 
    image = models.FileField(upload_to='images/')
    text = models.CharField(max_length = 500)
    writer = models.CharField(max_length = 10, blank=True)
    date = models.DateTimeField("date published")
    
    def sum(self):
        return self.text[:10]