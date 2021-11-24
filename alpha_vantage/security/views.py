import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_api_key.models import APIKey


# Create your views here.


class GetAPIKeyView(APIView):
    def post(self, request):
        try:
            if 'email' in request.data:
                api_key, key = APIKey.objects.create_key(name="my-remote-service")
                return Response({
                    'has_expired': api_key.has_expired,
                    'created': api_key.created,
                    'revoked': api_key.revoked,
                    'key': key
                })
            return Response({'message': "email required"}, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)
