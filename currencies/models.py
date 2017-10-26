from django.db import models

class Currency(models.Model):
  code = models.CharField(max_length=3)
  name = models.CharField(max_length=255)
  symbol = models.CharField(max_length=10)
    
  def __str__(self):
    return '{0}:{1}({2})'.format(self.code,self.name,self.symbol)

  class Meta:
    verbose_name_plural = "currencies"