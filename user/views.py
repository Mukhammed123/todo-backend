from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['POST'])
def userLogin(request):
  data = request.data
  user = authenticate(request, username=data['username'], password=data['password'])
  print(data)
  if user is not None:
    login(request, user)
    return Response({'message': 'Successfully logged in'})
  else:
    return Response({'message': 'Failed to login'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def testToken(request):
  return Response({"Message": "Token is still valid"}) 