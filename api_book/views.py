from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Book
from .serializer import BookModelSerializer


# Create your views here.

class ListApiBooks(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = Book.objects.all().order_by('-id')
        serializer = BookModelSerializer(books, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        book = {
            'title': request.data.get('title'),
            'price': request.data.get('price'),
            'short_description': request.data.get('short_description'),
            'description': request.data.get('description'),
            'is_active': request.data.get('is_active'),
            'is_delete': request.data.get('is_delete')
        }

        serializer = BookModelSerializer(data=book)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def book_api_view_detail(request, id):
    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookModelSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = BookModelSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
