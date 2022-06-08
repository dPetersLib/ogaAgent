from django.db import models

# Create your models here.

job_type = (
    ('FT', 'Full Time'),
    ('PT', 'Part Time'),
    ('RT', 'Remote'),
    ('FL', 'Freelance'),
)

job_cat = (
    ('HS', 'House Hold Work'),
    ('CO', 'Corperate'),
    ('ST', 'Onsite'),
)

job_qualification = (
    ('SSC', 'Secondary School Certificate'),
    ('OND', 'National Diploma'),
    ('HND', 'Higher National Diploma'),
    ('BSC', 'Bachelors Degree'),
    ('MSC', 'Masters Degree'),
    ('OTH', 'Others'),
)

class Location(models.Model):
    town = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50, default='Nigeria')

    def __str__(self):
        return f"{self.town}, {self.state}"

class Requirement(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField()
    requirements = models.ManyToManyField(Requirement, null=True, blank=True)
    type = models.CharField(max_length=2, choices=job_type)
    number = models.IntegerField()
    posted_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=2, choices=job_cat)
    lowest_salary = models.FloatField()
    highest_salary = models.FloatField()
    min_qualification = models.CharField(max_length=3, choices=job_qualification)
    experience_years = models.IntegerField()

    def __str__(self):
        return self.title
    
    def get_salary_range(self):
        min = int(self.lowest_salary / 1000)
        max = int(self.highest_salary / 1000)
        return f"N{min}K - N{max}K"
    
    # def get_type(self):
        
            

    


# job
# agent
# client
