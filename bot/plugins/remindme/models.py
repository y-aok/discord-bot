from django.db import models
from django.utils.translation import ugettext_lazy as _


class Message(models.Model):
    member = models.ForeignKey('users.Member', on_delete=models.CASCADE)
    text = models.TextField()
    deliver_at = models.DateTimeField()
    delivered = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('message')
        verbose_name_plural = _('messages')

    def __str__(self):
        return _("Message for {}").format(self.member)
