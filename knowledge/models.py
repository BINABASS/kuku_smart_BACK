from django.db import models


class PatientHealth(models.Model):
	description = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.description


class Recommendation(models.Model):
	reco_type_choices = (
		('Temperature', 'Temperature'),
		('Spo2', 'Spo2'),
		('Heart', 'Heart'),
		('Respiration', 'Respiration'),
		('Pressure', 'Pressure'),
	)
	context_choices = (
		('Home', 'Home'),
		('Hospital', 'Hospital'),
		('Ambulatory', 'Ambulatory'),
		('Any', 'Any'),
	)
	description = models.CharField(max_length=200, unique=True)
	reco_type = models.CharField(max_length=20, choices=reco_type_choices)
	context = models.CharField(max_length=20, choices=context_choices, default='Any')

	def __str__(self):
		return self.description


class ExceptionDisease(models.Model):
	recommendation = models.ForeignKey('knowledge.Recommendation', on_delete=models.CASCADE, related_name='exceptions')
	health = models.ForeignKey('knowledge.PatientHealth', on_delete=models.CASCADE, related_name='exceptions')

	class Meta:
		unique_together = ('recommendation', 'health')


class Anomaly(models.Model):
	hr_id = models.IntegerField()
	sp_id = models.IntegerField()
	pr_id = models.IntegerField()
	bt_id = models.IntegerField()
	resp_id = models.IntegerField()
	status = models.BooleanField(default=True)

	class Meta:
		indexes = [models.Index(fields=['hr_id', 'sp_id', 'pr_id', 'bt_id', 'resp_id'])]


class Medication(models.Model):
	diagnosis = models.ForeignKey('knowledge.Anomaly', on_delete=models.CASCADE, related_name='medications')
	recommendation = models.ForeignKey('knowledge.Recommendation', on_delete=models.PROTECT, related_name='medications')
	user = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='medications')
	sequence_no = models.IntegerField(default=1)

	class Meta:
		unique_together = ('diagnosis', 'recommendation')
		indexes = [models.Index(fields=['diagnosis', 'sequence_no'])]

# Create your models here.
