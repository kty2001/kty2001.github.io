from django.db import models

# Create your models here.
class ChatMessage(models.Model):
    session_id = models.CharField(max_length=255, db_index=True)
    message_type = models.CharField(max_length=10, choices=[
        ('human', 'Human'),
        ('ai', 'AI')
    ])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.session_id} - {self.message_type}: {self.content[:50]}...'

    class Meta:
        ordering = ['created_at']