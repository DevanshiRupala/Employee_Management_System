from django.db import models
from django.contrib.auth.models import User


class emp_details(models.Model):
      user = models.ForeignKey(User,on_delete=models.CASCADE)
      emp_id = models.CharField(max_length=10,null=True)
      email = models.CharField(max_length=50, null=True)
      empdept = models.CharField(max_length=50,null=True)
      designation = models.CharField(max_length=50, null=True)
      contact = models.IntegerField(null=True)
      joindate = models.DateField(null=True)

      def __str__(self):
          return self.emp_id


class payroll(models.Model):
      emp_id = models.CharField(max_length=10)
      reg_salary = models.IntegerField()
      overtime = models.IntegerField()
      bonus = models.IntegerField()
      total = models.IntegerField()

      def __str__(self):
            return self.emp_id


class leave(models.Model):
      emp_id = models.CharField(max_length=10, null=True)
      fname = models.CharField(max_length=20, null=True)
      lname = models.CharField(max_length=20, null=True)
      des = models.CharField(max_length=20, null=True)
      dept = models.CharField(max_length=20, null=True)
      reason = models.CharField(max_length=150)
      stdate = models.DateField(null=True)
      enddate = models.DateField(null=True)

      def __str__(self):
            return self.emp_id


class leave_res(models.Model):
      emp_id = models.CharField(max_length=10)
      response = models.CharField(max_length=150, default="no response")

      def __str__(self):
            return self.emp_id