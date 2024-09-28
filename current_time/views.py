from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime

# Create your views here.
class CurrentTimeView(APIView):
    def get(self, request):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return Response({'current_time': current_time})