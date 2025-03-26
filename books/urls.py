from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (BookListAPIView,
                    BookDetailAPIView,
                    BookDeleteAPIView,
                    BookUpdateAPIView,
                    BookCreateAPIView,
                    BookListCreateAPIView,
                    BookUpdateDeleteAPIView,
                    BookViewSet,)

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')


urlpatterns = [
    # path('books/', BookListAPIView.as_view(), name='home'),
    #
    # path('books/list-create/', BookListCreateAPIView.as_view(), name='list-create'),
    # path('books/updatedelete/', BookUpdateDeleteAPIView.as_view(), name='list-update-delete'),
    #
    # path('books/create/', BookCreateAPIView.as_view(), name='create'),
    # path('books/<int:pk>/', BookDetailAPIView.as_view(), name='detail'),
    # path('books/<int:pk>/update', BookUpdateAPIView.as_view(), name='update'),
    # path('books/<int:pk>/delete/', BookDeleteAPIView.as_view(), name='delete'),
]

urlpatterns += router.urls