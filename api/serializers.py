from rest_framework import serializers

class TranslationRequestSerializer(serializers.Serializer):
    text = serializers.CharField()
    target_lang = serializers.CharField()