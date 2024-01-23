from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
import ipdb

# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/creating_tokens_manually.html


class GetTokenView(APIView):
    @csrf_exempt
    def post(self, request):
        email = request.data.get("email", "")
        password = request.data.get("password", "")
        user = authenticate(
            username=email,
            password=password,
        )
        if user:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "status": "ok",
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                status=200,
            )

        return Response({"status": "error", "message": "Login failed!"}, status=403)


class ValidateTokenView(APIView):
    @csrf_exempt
    def get(self, request):
        token = request.GET.get("token", "")
        jwt_authentication = JWTAuthentication()
        validated_token = jwt_authentication.get_validated_token(token)
        user = jwt_authentication.get_user(validated_token)

        if user:
            return Response({"status": "ok", "email": user.email}, status=200)
        return Response(
            {"status": "error", "message": "Token wrong or not valid"}, status=403
        )
