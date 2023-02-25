from django.db import models
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _


class PaymentStatus:
    SUCCESS = "Success"
    FAILURE = "Failure"
    PENDING = "Pending"


class Order(models.Model):
    name = CharField(_("Customer Name"), max_length=254)
    amount = models.FloatField(_("Amount"), null=False, blank=False)
    status = CharField(_("Payment Status"), default=PaymentStatus.PENDING, max_length=254)
    provider_order_id = models.CharField(_("Order ID"), max_length=40)
    payment_id = models.CharField(_("Payment ID"), max_length=36)
    signature_id = models.CharField(_("Signature ID"), max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}-{self.name}-{self.status}"