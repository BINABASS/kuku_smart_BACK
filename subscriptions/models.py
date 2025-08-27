from django.db import models


class SubscriptionType(models.Model):
	name = models.CharField(max_length=50, unique=True)
	farm_size = models.CharField(max_length=20)
	cost = models.IntegerField()
	description = models.CharField(max_length=200)

	def __str__(self):
		return f'{self.name} | {self.farm_size}'


class Resource(models.Model):
	resource_type_choices = (
		(1, 'Smart Device'),
		(2, 'Software Feature'),
		(3, 'Data Analytics'),
		(4, 'Predictions'),
	)
	name = models.CharField(max_length=50, unique=True)
	resource_type = models.IntegerField(choices=resource_type_choices, default=1)
	unit_cost = models.IntegerField()
	status = models.BooleanField(default=True)

	def __str__(self):
		return self.name


class FarmerSubscription(models.Model):
	farmer = models.ForeignKey('accounts.Farmer', on_delete=models.CASCADE, related_name='subscriptions')
	sub_type = models.ForeignKey('subscriptions.SubscriptionType', on_delete=models.PROTECT, related_name='farmer_subscriptions')
	start_date = models.DateField()
	end_date = models.DateField()
	discount = models.IntegerField(default=0)
	status = models.BooleanField(default=True)


class FarmerSubscriptionResource(models.Model):
	farmer_subscription = models.ForeignKey('subscriptions.FarmerSubscription', on_delete=models.CASCADE, related_name='resources')
	resource = models.ForeignKey('subscriptions.Resource', on_delete=models.PROTECT, related_name='allocations')
	quantity = models.IntegerField(default=1)
	status = models.BooleanField(default=True)

	class Meta:
		unique_together = ('farmer_subscription', 'resource')


class Payment(models.Model):
	farmer_subscription = models.ForeignKey('subscriptions.FarmerSubscription', on_delete=models.CASCADE, related_name='payments')
	amount = models.IntegerField()
	pay_date = models.DateField()
	receipt = models.CharField(max_length=50, default='no_receipt.jpg')
	status = models.BooleanField(default=True)

# Create your models here.
