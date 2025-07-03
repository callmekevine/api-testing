from django.db import models

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    method = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Payment {self.payment_id} ({self.status})"