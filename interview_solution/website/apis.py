from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import check_password
from rest_framework import viewsets, permissions, generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.utils import json

# Create your api here.

@api_view(['POST'])
def signup(request):
    if request.method == "POST":
        serializer = SignupUserSerializer(data = request.data)
        if(serializer.validated_data['password']!=serializer.validated_data['passwordChk']):
            return Response({"message":"Password Error"})

from .models import User
from .serializers import (
    SignupUserSerializer,
    SigninUserSerializer,
)

class SigninUserAPI(generics.GenericAPIView):
    serializer_class = SigninUserSerializer
    renderer_classes = (TemplateHTMLRenderer,)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        user = User.objects.get(userID=data['userID'])

        if check_password(data['password'], user.password):
            return Response({"message": "로그인에 성공하셨습니다."}, template_name='signin.html')
        else:
            return Response({'message' : '실패'}, template_name='signin.html')
