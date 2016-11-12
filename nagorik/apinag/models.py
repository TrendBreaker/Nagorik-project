from django.db import models
import datetime


class Issues(models.Model):
    issue_name = models.TextField()
    description = models.TextField()
    status = models.CharField(max_length=22)

    def __str__(self):
    	return self.issue_name


class SubCategory(models.Model):
	name = models.CharField(max_length=54)
	timestamp = models.DateTimeField()
	problems = models.ForeignKey('Issues', on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Category(models.Model):
    problem_name = models.CharField(max_length=54)
    sub_category = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    
    def __str__(self):
    	return self.problem_name


