from django.db import models

class Payment(models.Model):
    order_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
