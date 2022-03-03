from django.db import models

# Create your models here.
class Member(models.Model):
    id = models.BigAutoField(primary_key=True)
    emailid = models.EmailField(max_length=255)
    fullname = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def register(self):
        self.save()
    
    @staticmethod
    def get_member_by_email(emailid):
        try:
            return Member.objects.get(emailid=emailid)
        except:
            return False
    
    @staticmethod
    def get_member_by_password(password):
        try:
            return Member.objects.get(password=password)
        except:
            return False