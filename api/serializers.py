from rest_framework import serializers

class TranslationRequestSerializer(serializers.Serializer):
    text = serializers.CharField()
    target_language = serializers.CharField()