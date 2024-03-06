from django.db import models


class News(models.Model):
      title = models.CharField(max_length=100)
      desc = models.TextField(max_length=500)
      pub_date = models.DateField()
      img = models.ImageField(blank=True, null=True)
      url = models.URLField(blank=True)
      
      def __str__(self):
            return self.title

class Category(models.Model):
      title = models.CharField(max_length=100)
      news = models.ForeignKey(News, on_delete=models.CASCADE, null=True)

      def __str__(self):
            return self.title
