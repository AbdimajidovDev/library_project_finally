from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.utils.representation import serializer_repr
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializers
from rest_framework import generics, status


# class BookListAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers

class BookListAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializers(books, many=True).data

        data = {
            'stastus': f'Returned {len(books)} books',
            'message': serializer
        }
        return Response(data)

# class BookDetailAPIView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers

class BookDetailAPIView(APIView):
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        serializers = BookSerializers(book).data

        date = {
            'status': 'Successfull',
            'book': serializers
        }
        return Response(date)


# class BookDeleteAPIView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers

class BookDeleteAPIView(APIView):
    def delete(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        book.delete()
        data = {
            'status': True,
            'message': "malumot o'chirilid"
        }
        return Response(data)


# class BookUpdateAPIView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers

class BookUpdateAPIView(APIView):
    def put(self, request, pk):
        data = request.data
        book = get_object_or_404(Book.objects.all(), id=pk)
        serializer = BookSerializers(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_save = serializer.save()
            res = {
                'status': True,
                'message': f'Updated {book_save} succesfull'
            }
            return Response(res)



# class BookCreateAPIView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers

class BookCreateAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializers(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                'status': 'Creates save database',
                'books': data}
            return Response(data)



class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class BookUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class BookViewSet(ModelViewSet):   #  CRUD -> create, post, update, delete
    queryset = Book.objects.all()
    serializer_class = BookSerializers

