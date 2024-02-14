from django.db import models

# Create your models here.
class People(models.Model):
    PERSON_TYPE_CHOICES = [
        ('electrician', 'Electrician'),
        ('mishtry', 'Mishtry'),
        ('color_work', 'Color Work'),
    ]

    people_name = models.CharField(max_length = 255, blank = True, null = True)
    mobile_no = models.CharField(max_length = 255, blank = True, null = True)

    people_type = models.CharField(max_length=255, blank= True, null = True, choices=PERSON_TYPE_CHOICES)

    def __str__(self):
        return self.people_name

class Building(models.Model):
    building_name = models.CharField(max_length=255, blank = True, null = True)
    office_no = models.CharField(max_length = 255, blank = True, null = True)
    location = models.CharField(max_length = 255, blank = True, null = True)
    address = models.CharField(max_length= 255, blank = True, null = True)

    def __str__(self):
        return self.building_name

class Customer(models.Model):
    customer_name = models.CharField(max_length=255, blank = True, null = True)
    email = models.EmailField(blank = True, null = True)
    phone_no = models.CharField(max_length=15, blank = True, null = True)  

    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    resources = models.ForeignKey(People, on_delete=models.CASCADE)


    def __str__(self):
        return self.customer_name