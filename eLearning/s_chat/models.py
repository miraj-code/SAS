from email.headerregistry import Group
import imp
from django.db import models
from django.contrib.auth.models import Group
from a_user.models import Student
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatGroup(Group):
    description = models.TextField()
    profile_picture = models.ImageField(upload_to='Chat Group Profile Pictures')
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Chat Group'
        verbose_name_plural = 'Chat Groups'

#chat group messages
class ChatGroupMessage(models.Model):
    group = models.ForeignKey(ChatGroup, on_delete=models.CASCADE)
    sender = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.message

    class Meta:
        verbose_name = 'Chat Group Message'
        verbose_name_plural = 'Chat Group Messages'

