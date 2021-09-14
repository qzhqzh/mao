""" Models for good """

from django.db import models
from django.utils.translation import gettext_lazy as _


class Notice(models.Model):
    """ mao notices """
    name = models.CharField(max_length=128, verbose_name=_('Good name'))
    platform = models.CharField(max_length=128, verbose_name=_('Sale platform'))
    appointment_at = models.TimeField(verbose_name=_('Good appointment at'))
    remind_at = models.TimeField(verbose_name=_('Good remind at'))
    sale_at = models.TimeField(verbose_name=_('Good sale at'))
