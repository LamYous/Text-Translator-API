from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .service import TranslationSrevice
from .serializers import TranslationRequestSerializer


class TranslateTextView(APIView):
    def post(self, request):
        data = request.data
        serializer = TranslationRequestSerializer(data=data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            target_lang = serializer.validated_data['target_lang']

            try:
                translated_data = TranslationSrevice.translate_text[text, target_lang]
                return Response(translated_data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": f"Error Mappened: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
        
        
