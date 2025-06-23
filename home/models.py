# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    phone = models.CharField(max_length=255, null=True, blank=True)
    balance = models.CharField(max_length=255, null=True, blank=True)
    parent_user = models.IntegerField(null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Product(models.Model):

    #__Product_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField()

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Package(models.Model):

    #__Package_FIELDS__
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    duration_days = models.IntegerField(null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    features = models.TextField(max_length=255, null=True, blank=True)

    #__Package_FIELDS__END

    class Meta:
        verbose_name        = _("Package")
        verbose_name_plural = _("Package")


class License(models.Model):

    #__License_FIELDS__
    user = models.CharField(max_length=255, null=True, blank=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    hwid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    expires_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__License_FIELDS__END

    class Meta:
        verbose_name        = _("License")
        verbose_name_plural = _("License")


class Invoice(models.Model):

    #__Invoice_FIELDS__
    user = models.CharField(max_length=255, null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    payment_method = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Invoice_FIELDS__END

    class Meta:
        verbose_name        = _("Invoice")
        verbose_name_plural = _("Invoice")


class Server(models.Model):

    #__Server_FIELDS__
    status = models.IntegerField(null=True, blank=True)
    ip_address = models.CharField(max_length=255, null=True, blank=True)
    port = models.IntegerField(null=True, blank=True)

    #__Server_FIELDS__END

    class Meta:
        verbose_name        = _("Server")
        verbose_name_plural = _("Server")


class Ticket(models.Model):

    #__Ticket_FIELDS__
    description = models.TextField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    priority = models.CharField(max_length=255, null=True, blank=True)

    #__Ticket_FIELDS__END

    class Meta:
        verbose_name        = _("Ticket")
        verbose_name_plural = _("Ticket")



#__MODELS__END
