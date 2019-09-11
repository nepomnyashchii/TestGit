from django.urls import path

from.import views
app_name = 'articles'
urlpatterns = [
    path('', views.index, name = 'index'),
    # path('test/', views.test, name = 'test')
    path('<int:article_id>/', views.detail, name = 'detail'),
    path('<int:article_id>/leave_comment/', views.detail, name = 'leave_comment'),
]

# /articles/1
# /articles/1/leave_comment/