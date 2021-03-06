from django.db import models

from campaign.models import Detail

class Chat(models.Model):
    campaign = models.ForeignKey(Detail, on_delete=models.CASCADE)
    # investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    subject = models.CharField(max_length=32, default='random message')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Chat: ' + self.campaign.name + ' - ' + self.investor.user.username

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    # founder = models.ForeignKey(Founder, on_delete=models.CASCADE)
    message = models.TextField()
    media = models.FileField(upload_to='uploads/')
    link = models.URLField()
    status = models.SmallIntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.chat.campaign.name + ' - ' + self.message
