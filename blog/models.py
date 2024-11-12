from django.db import models

class Student(models.Model):
    # Basic student information
    name = models.CharField(max_length=100)
    college_id = models.CharField(max_length=20, unique=True)  # College ID as a unique string
    branch = models.CharField(max_length=50)
    
    # Additional fields
    age = models.PositiveIntegerField()  # Age of the student
    email = models.EmailField(unique=True)  # Unique email address
    enrollment_date = models.DateField()  # Date of enrollment
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Optional phone number
    address = models.TextField(blank=True, null=True)  # Optional address field
    
    def __str__(self):
        return self.name
    

