from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.author_name
    
class About(models.Model):
    id = models.AutoField(primary_key=True)
    about_description = models.CharField(max_length=200)
    profession_title = models.CharField(max_length=200)
    profession_description = models.CharField(max_length=200)
    birthday = models.DateField()
    website = models.CharField(max_length=50)
    age = models.IntegerField()
    degree = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    email = models.EmailField()
    freelance = models.CharField(max_length=50)
    profession_details = models.CharField(max_length=200)
    about_pic = models.ImageField()

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.about_pic.url))

    def __str__(self):
        return self.profession_title
    

class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    SKILL_TAGS = (
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('django', 'django'),
    )  
    skill_details = models.CharField(max_length=200,null=True)
    skill_tags = models.CharField(max_length=10, choices=SKILL_TAGS,null=True)
    skill_value = models.IntegerField()

    def __str__(self):
        return self.skill_tags


class Fact(models.Model):
    id = models.AutoField(primary_key=True)
    fact = models.CharField(max_length=50,null=True)
    fact_value = models.IntegerField(null=True) 

    def __str__(self):
        return str(self.fact)

class Testimonials(models.Model):
    id = models.AutoField(primary_key=True)
    profile_pic = models.ImageField()
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    testimonial_details = models.CharField(max_length=250)

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.profile_pic.url))    

    def __str__(self):
        return self.name


class Summary(models.Model):
    id = models.AutoField(primary_key=True)
    person_name = models.CharField(max_length=50)
    about_person =  models.TextField()
    person_address = models.CharField(max_length=50)
    person_phone = models.CharField(max_length=50)
    person_email = models.EmailField(max_length=50)

    def __str__(self):
        return self.person_name
    

class Education(models.Model):
    id = models.AutoField(primary_key=True)
    education_degree = models.CharField(max_length=50)
    education_year = models.CharField(max_length=50)
    education_university = models.CharField(max_length=50)
    about_education =  models.TextField()

    def __str__(self):
        return self.education_degree


class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    experience_degree = models.CharField(max_length=50)
    experience_year = models.CharField(max_length=50)
    experience_university = models.CharField(max_length=50)
    about_experience  = models.TextField()

    def __str__(self):
        return self.experience_degree

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    service_images = models.ImageField()
    service_title = models.CharField(max_length=50)
    service_details = models.TextField()

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.service_images.url))   

    def __str__(self):
        return self.service_title

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    album_user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    album_image = models.ImageField(null=True,blank=True)
    album_title = models.CharField(max_length=50,null=True)
    album_subtitle = models.CharField(max_length=50,null=True)

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.album_image.url))       

    def __str__(self):
        return self.album_subtitle


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    conatact_name = models.CharField(max_length=50)
    contact_email = models.EmailField()
    contact_subject = models.CharField(max_length=50)
    contact_message = models.TextField()


    def __str__(self):
        return self.conatact_name



    




