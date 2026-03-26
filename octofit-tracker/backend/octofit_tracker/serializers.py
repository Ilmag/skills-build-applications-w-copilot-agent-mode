from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard
from bson import ObjectId

class ObjectIdField(serializers.Field):
	def to_representation(self, value):
		return str(value)
	def to_internal_value(self, data):
		return ObjectId(data)

class UserSerializer(serializers.ModelSerializer):
	_id = ObjectIdField(read_only=True)
	class Meta:
		model = User
		fields = ['_id', 'username', 'email']

class TeamSerializer(serializers.ModelSerializer):
	_id = ObjectIdField(read_only=True)
	members = UserSerializer(many=True, read_only=True)
	class Meta:
		model = Team
		fields = ['_id', 'name', 'members']

class ActivitySerializer(serializers.ModelSerializer):
	_id = ObjectIdField(read_only=True)
	user = UserSerializer(read_only=True)
	class Meta:
		model = Activity
		fields = ['_id', 'user', 'type', 'duration', 'date']

class WorkoutSerializer(serializers.ModelSerializer):
	_id = ObjectIdField(read_only=True)
	class Meta:
		model = Workout
		fields = ['_id', 'name', 'description']

class LeaderboardSerializer(serializers.ModelSerializer):
	_id = ObjectIdField(read_only=True)
	team = TeamSerializer(read_only=True)
	class Meta:
		model = Leaderboard
		fields = ['_id', 'team', 'score']
