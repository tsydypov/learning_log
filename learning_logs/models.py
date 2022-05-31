from django.db import models


class Topic(models.Model):
    """What is user learning"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of model"""
        return self.text


class Entry(models.Model):
    """What did user learn"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) >= 50:
            return self.text[:50] + "..."
        else:
            return self.text[:50]
