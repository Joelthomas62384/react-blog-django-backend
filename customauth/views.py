from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterUserSerializer
from .models import UserProfile
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterUserListCreateView(APIView):
    def get(self, request):
        users = UserProfile.objects.all()
        serializer = RegisterUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            serializer = RegisterUserSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({'status':404, 'message':serializer.errors})
            serializer.save()
            return Response({'status':200,'message':'An otp has been send to your mobile and email address'})
            
        except Exception as e:
            return Response({'status':404, 'error':str(e)})   
            

