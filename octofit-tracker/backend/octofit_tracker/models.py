from djongo import models

class User(models.Model):
	_id = models.ObjectIdField()
	username = models.CharField(max_length=150, unique=True)
	email = models.EmailField(unique=True)
	# Add additional user fields as needed
	def __str__(self):
		return self.username

class Team(models.Model):
	_id = models.ObjectIdField()
	name = models.CharField(max_length=100, unique=True)
	members = models.ArrayReferenceField(to=User, on_delete=models.CASCADE)
	def __str__(self):
		return self.name

class Activity(models.Model):
	_id = models.ObjectIdField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	type = models.CharField(max_length=100)
	duration = models.IntegerField()  # in minutes
	date = models.DateField()
	def __str__(self):
		return f"{self.type} by {self.user}"

class Workout(models.Model):
	_id = models.ObjectIdField()
	name = models.CharField(max_length=100)
	description = models.TextField()
	def __str__(self):
		return self.name

class Leaderboard(models.Model):
	_id = models.ObjectIdField()
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	score = models.IntegerField()
	def __str__(self):
		return f"{self.team} - {self.score}"
