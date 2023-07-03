from django.urls import path
from .views import  UserCreateView, UserRetrieveUpdateDestroyView, \
                      PostCreateView, PostRetrieveUpdateDestroyView, \
                      LikeCreateView, LikeRetrieveUpdateDestroyView

urlpatterns = [
    path('api/user/', UserCreateView.as_view()),
    path('api/user/<int:pk>/', UserRetrieveUpdateDestroyView.as_view()),
    path('api/post/', PostCreateView.as_view()),
    path('api/post/<int:pk>/', PostRetrieveUpdateDestroyView.as_view()),
    path('api/like/', LikeCreateView.as_view()),
    path('api/like/<int:pk>/', LikeRetrieveUpdateDestroyView.as_view()),
]

