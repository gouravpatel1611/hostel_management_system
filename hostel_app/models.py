from django.db import models

# Create your models here.

class Admin_pass(models.Model):
    username = models.CharField(max_length=50,null=False)
    password = models.CharField(max_length=20,null=False)
    def __str__(self):
        return self.username
    
class Student_pass(models.Model):
    username = models.CharField(max_length=50,null=False)
    password = models.CharField(max_length=20,null=False)
    def __str__(self):
        return self.username
    
class Student_data(models.Model):
    student_name = models.CharField(max_length=50,null=False)
    username = models.CharField(max_length=50,default="123")
    student_number = models.CharField(max_length=20, null=False)    
    student_email = models.CharField(max_length=50, null=False)    
    father_name = models.CharField(max_length=50, null=False)    
    parents_number = models.CharField(max_length=20, null=False)    
    address = models.CharField(max_length=100,null=False)
    course = models.CharField(max_length=20,null=False)
    room_no = models.CharField(max_length=10,default="00")
    join_date = models.DateField()
    join_by = models.CharField(max_length=20,default=" ")
    status = models.CharField(max_length=10,default="IN")
    gate_pass_no = models.CharField(max_length=10,default="NO")
    
    def __str__(self):
        return self.student_name
    
class Guard_pass(models.Model):
    username = models.CharField(max_length=50,null=False)
    password = models.CharField(max_length=20,null=False)
    def __str__(self):
        return self.username
    
class Guard_data(models.Model):
    guard_name = models.CharField(max_length=50,null=False)
    username = models.CharField(max_length=50,default="123")
    guard_number = models.CharField(max_length=20, null=False)    
    guard_email = models.CharField(max_length=50, null=False)    
    address = models.CharField(max_length=100,null=False)
    join_date = models.DateField()
    join_by = models.CharField(max_length=20,default=" ")
    
    def __str__(self):
        return self.guard_name
    
    
    

class Admin_data(models.Model):
    admin_name = models.CharField(max_length=50,null=False)
    username = models.CharField(max_length=50,default="123")
    admin_number = models.CharField(max_length=20, null=False)    
    admin_email = models.CharField(max_length=50, null=False)    
    post = models.CharField(max_length=100,null=False)
    join_date = models.DateField()
    join_by = models.CharField(max_length=20,default=" ")
    
    def __str__(self):
        return self.admin_name
    
class Gatepass(models.Model):
    issue_by = models.CharField(max_length=50,null=False)
    username = models.CharField(max_length=50,null=False)
    name = models.CharField(max_length=50,null=False)
    email = models.CharField(max_length=50,null=False)
    phone = models.CharField(max_length=50,null=False)
    course = models.CharField(max_length=50,null=False)
    input_date = models.CharField(max_length=50,null=False)
    region = models.CharField(max_length=50,null=False)
    issue_date = models.DateTimeField()
    out_time = models.CharField(max_length=20,default="not-set",null=True)
    out_date = models.CharField(max_length=20,default="not-set",null=True)
    in_time = models.CharField(max_length=20,default="not-set",null=True)
    in_date = models.CharField(max_length=20,default="not-set",null=True)
    status = models.CharField(max_length=10,default="IN")
    hex_code = models.CharField(max_length=500,default=" ")
    outing_scan_by = models.CharField(max_length=50,default="not-set")
    entry_scan_by = models.CharField(max_length=50,default="not-set")
    
    def __str__(self):
        return self.name
        