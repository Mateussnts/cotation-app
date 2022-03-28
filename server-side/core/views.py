from datetime import datetime

import datetime
import jwt
import requests
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


# Create your views here.

# registro de usuarios

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

# endpoint para login no sistema e autenticando usuario com jwt

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('Usuario não encontrado!')

        elif not user.check_password(password):
            raise AuthenticationFailed('Senha Incorreta!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response

# endpoit para logout da usuario

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'sucsess'
        }

        return response

# authenticando usuario no sistema

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Não Autenticado!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Não Autenticado')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class DashboardAPI(APIView):
    def get_cotacaoDolar(self):
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"
        retorno = requests.get(url)
        if retorno.status_code==200:
            cotacaoDolar = retorno.json()
            self.valor = cotacaoDolar['USD']['bid']
        else:
            self.valor = 0

    def get_cotacaoEuro(self):
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"
        retorno = requests.get(url)
        if retorno.status_code==200:
            cotacaoEuro = retorno.json()
            self.valor = cotacaoEuro['EUR']['bid']
        else:
            self.valor = 0

    def get_cotacaoBTC(self):
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"
        retorno = requests.get(url)
        if retorno.status_code==200:
            cotacaoBTC = retorno.json()
            self.valor = cotacaoBTC['BTC']['bid']
        else:
            self.valor = 0