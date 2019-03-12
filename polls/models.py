from django.db import models

#this is the parent class
class Poll(models.Model):#define fields and behaviors
    form = models.CharField(max_length=255)
    pub_date = models.DateField()
    text = models.CharField(max_length=255, null='DEFAULT VALUE')
    #text is used as a keyword, which is useful for categorising

    def __str__(self):
        return str(self.text) #convert to string to avoid any errors

#this is the child class
class Options(models.Model):
    question = models.ForeignKey(Poll, on_delete=models.CASCADE) #many to one relationship, relating to the Poll class
    option = models.CharField(max_length=255) #choice_text
    votes = models.IntegerField(default=0) #0 votes on the choice to start off with

    def __str__(self):
        return "{} - {}".format(self.question.text[:25], self.option[:25]) #slicing

#points to object, views the object