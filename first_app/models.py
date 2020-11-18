from django.db import models

class bookManager(models.Manager):
    def bookValidator(self, postData):
        errors = {}
        if len(postData['form_title']) == 0:
            errors['titleReq']="What is the Title?"
        if len(postData['form_desc']) < 10:
            errors['descReq']= "Book description must have at least 10 characters!"
        return errors
        



class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at= models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    objects=bookManager()

class Authors(models.Model):
    first_name = models.CharField( max_length=45)
    last_name = models.CharField(max_length=45)
    books = models.ManyToManyField(Books, related_name= "authors" )
    notes= models.TextField()
    created_at= models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=False, auto_now_add=True)



