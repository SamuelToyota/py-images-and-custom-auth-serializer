from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from cinema.models import Movie
from cinema.serializers import MovieImageSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    @action(
        methods=["POST"],
        detail=True,
        url_path="upload-image",
    )
    def upload_image(self, request, pk=None):
        movie = self.get_object()
        serializer = MovieImageSerializer(movie, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
