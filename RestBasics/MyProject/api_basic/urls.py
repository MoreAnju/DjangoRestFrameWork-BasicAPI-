
from django.urls import path, include
from .views import article_list, article_details, ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSetModelView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articleM', ArticleViewSetModelView, basename='articleM')
#router.register('articleG', ArticleViewSetGeneric, basename='articleG')
#router.register('article', ArticleViewSet, basename='article')



urlpatterns = [
    path('viewsetM/', include(router.urls)), #for viewsets modelview
    path('viewsetM/<int:id>/', include(router.urls)),
    #path('viewsetG/', include(router.urls)), for viewsets generic
    #path('viewsetG/<int:id>/', include(router.urls)), for viewsets generic
    #path('viewset/', include(router.urls)),
    #path('viewset/<int:id>/', include(router.urls)),
    #path('viewset/', include(router.urls)),  # in url viewset/article
    #path('articles/', article_list),
    #path('details/<int:pk>/', article_details),
    path('articles/', ArticleAPIView.as_view()),
    path('details/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
]