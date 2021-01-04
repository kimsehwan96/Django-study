from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>/', views.board_detail), #숫자형인 변수명 Pk인 놈을 받겠다. 뷰에 전달됨
    path('list/', views.board_list),
    path('write/', views.board_write),
]
