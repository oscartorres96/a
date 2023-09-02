from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def login_view(request):
    # Obtiene las credenciales del usuario desde la solicitud
    username = request.data.get('username')
    password = request.data.get('password')

    # Autentica al usuario
    user = authenticate(request, username=username, password=password)

    if user is not None:
        # Inicia sesión en el usuario
        login(request, user)
        return Response({'detail': 'Login exitoso'}, status=status.HTTP_200_OK)
    else:
        return Response({'detail': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    pass

def login_view(request):
    return render(request, 'login_app_vue.html')

