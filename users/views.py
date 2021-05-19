from users.serializers import *
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import *
from rest_framework_simplejwt.tokens import *
from rest_framework import status
from rest_framework.views import APIView

class MyObtainTokenPairView(TokenObtainPairView):
    # Pairing username and password as a login function
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(MyObtainTokenPairView, self).dispatch(request, *args, **kwargs)


class RegisterView(CreateAPIView):
    # Create new user for newcommers user
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

class UserDetail(ListAPIView):
    # get user detail
    permission_classes = (IsAuthenticated,)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserDetail, self).dispatch(request, *args, **kwargs)

    def get(self, request, format=None):
        id =request.user.pk
        queryset = User.objects.get(pk=id)
        serializer = UserSerializer(queryset)
        return Response(serializer.data)

class ChangePasswordView(UpdateAPIView):
    # Function for change password
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ChangePasswordView, self).dispatch(request, *args, **kwargs)


class UpdateProfileView(UpdateAPIView):
    # Function for update and edit the profile
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UpdateProfileView, self).dispatch(request, *args, **kwargs)


class LogoutView(APIView):
    # Function for logout account and delete the session
    permission_classes = (IsAuthenticated,)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LogoutView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutAllView(APIView):
    # Function for admin to logout all active user
    permission_classes = (IsAuthenticated,)

    def dispatch(self, request, *args, **kwargs):
        return super(LogoutAllView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)
