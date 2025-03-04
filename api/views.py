from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # @authentication_classes([])
    #@permission_classes([])
    @action(detail=False, methods=['get'])
    def like(self, request, pk=None):
        # user = self.get_object()
        # Add logic to like the blog post
        return Response({'status': 'blog post liked'})
