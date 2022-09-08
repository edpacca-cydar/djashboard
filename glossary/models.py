from django.db import models

class Domain(models.Model):
    title = models.CharField(max_length=80)
    acronym = models.CharField(max_length=30, blank=True)
    description = models.TextField(max_length=2000, blank=True)
    objects = models.Manager()
    def __str__(self):
        if self.acronym:
            return self.acronym
        return self.title

class Entry(models.Model):
    class Meta:
        verbose_name_plural = "entries"
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    acronym = models.CharField(max_length=30, blank=True)
    description = models.TextField(max_length=2000)
    objects = models.Manager()
    def __str__(self):
        if self.acronym:
            return self.acronym
        return self.title

