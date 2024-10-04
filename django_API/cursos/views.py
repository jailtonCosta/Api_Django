from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import  Curso,Avaliacao
from .serializers import CursoSerializer,AvaliacaoSerializer

class CursoAPView(APIView):
    '''
    API de Cursos
    '''
    def get(self, request):
        print(request.user)
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



class AvaliacaoAPView(APIView):

    def get(self, request):
        avaliacao = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacao, many=True)
        return Response(serializer.data)

