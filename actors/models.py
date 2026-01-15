from django.db import models

NATIONALITY_CHOICES = [
    ('US', 'United States'),
    ('UK', 'United Kingdom'),
    ('CA', 'Canada'),
    ('AU', 'Australia'),
    ('IN', 'India'),
    ('FR', 'France'),
    ('DE', 'Germany'),
    ('JP', 'Japan'),
    ('CN', 'China'),
    ('BR', 'Brasil'),
]
class Actor(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        choices=NATIONALITY_CHOICES,
        max_length=100, 
        blank=True, 
        null=True
       )
    
    def __str__(self):
        return self.name
    
