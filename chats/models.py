from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return str(self.username)


class Chatroom(models.Model):
    name = models.CharField(max_length=100, unique=True)
    max_members = models.IntegerField()
    members = models.ManyToManyField(User, related_name='chatrooms')
    
    def __str__(self):
        return str(self.name)


class Message(models.Model):
    text = models.TextField()
    attachment = models.FileField(
        upload_to='attachments/', null=True, blank=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.text)