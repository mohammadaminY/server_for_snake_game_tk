from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from best_score.serializers import BestScoreModelSerializer
from best_score.models import BestScore


@api_view(['GET'])
def get_all_best_score(request):
    query = BestScore.objects.all()
    serializer = BestScoreModelSerializer(query, many=True)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def set_best_score(request, pk):
    query = BestScore.objects.get(pk=pk)
    serializer = BestScoreModelSerializer(query, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_best_score(request):
    serializer = BestScoreModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
