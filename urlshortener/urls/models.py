from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class URL(TimeStampedModel):
    url = models.URLField(verbose_name=_("URL"), null=True, blank=True)

    class Meta:
        ordering = ("-created",)
        verbose_name_plural = _("URL")
