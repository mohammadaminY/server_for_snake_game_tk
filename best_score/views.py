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


@api_view(['DELETE'])
def delete_best_score(request, pk):
    query = BestScore.objects.get(pk=pk)
    query.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
# @permission_classes()
def get_my_rank(request, pk):
    query = BestScore.objects.all().order_by('-best_score')
    rank = 1
    for bs in query:
        if bs.user_id == pk:
            break
        rank += 1
    if rank == (len(query) + 1):
        return Response({'error': 'You don\'t set best score. So you don\'t have rank.', 'rank': None},
                        status.HTTP_404_NOT_FOUND)
    return Response({'rank': rank}, status.HTTP_200_OK)
