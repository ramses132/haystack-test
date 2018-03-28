from django.db import models
from tenant_schemas.models import TenantMixin
from core.models import TimestampMixin
from django.utils.translation import ugettext_lazy as _


class Client(TenantMixin, TimestampMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    on_trial = models.BooleanField()

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

    class Meta:
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')
