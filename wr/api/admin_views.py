from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.core.validators import validate_email
import ipdb


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "email"]


class UserManagementView(APIView):
    permission_classes = [IsSuperUser]

    @csrf_exempt
    # READ
    def get(self, request, user_id=None):
        if user_id:
            all_users = get_user_model().objects.filter(id=user_id).all()
        else:
            all_users = get_user_model().objects.filter().all()
        user_serializer = UserSerializer(all_users, many=True)
        return Response(user_serializer.data, status=200)

    @csrf_exempt
    # CREATE
    def post(self, request):
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        if not email or not password:
            return Response(
                {"status": "error", "message": "No valid data!"}, status=403
            )

        try:
            validate_email(email)
        except Exception:
            return Response(
                {"status": "error", "message": "Plese provide correct email"},
                status=400,
            )

        if get_user_model().objects.filter(email=email).exists():
            return Response({"status": "error", "message": "User exists!"}, status=400)

        user = get_user_model().objects.create_user(email=email)
        user.set_password(password)
        user.save()
        return Response({"status": "ok", "user_id": user.id}, status=200)

    @csrf_exempt
    # UPDATE
    def put(self, request, user_id):
        if not get_user_model().objects.filter(id=user_id).exists():
            return Response(
                {"status": "error", "message": "User doesn't exists!"}, status=400
            )
        user = get_user_model().objects.get(id=user_id)

        email = request.POST.get("email", "")
        password = request.POST.get("password", "")

        if email:
            try:
                validate_email(email)
            except Exception:
                return Response(
                    {"status": "error", "message": "Plese provide correct email"},
                    status=400,
                )
            user.email = email
            user.save()
        if password:
            user.set_password(password)
            user.save()

        return self.get(request, user_id)

    @csrf_exempt
    # DELETE
    def delete(self, request, user_id):
        if not get_user_model().objects.filter(id=user_id).exists():
            return Response(
                {"status": "error", "message": "User doesn't exists!"}, status=400
            )
        user = get_user_model().objects.get(id=user_id)
        user.delete()
        return Response(
            {"status": "ok", "message": f"User with id '{user_id}' deleted!"},
            status=200,
        )
