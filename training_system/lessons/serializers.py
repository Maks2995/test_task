from rest_framework import serializers

from .models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Lesson
        fields = "__all__"
