from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimestampMixin(models.Model):
    """
    Adds created, modified
    """
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
        verbose_name = _('timestamp mixin')
        verbose_name_plural = _('timestamp mixins')
