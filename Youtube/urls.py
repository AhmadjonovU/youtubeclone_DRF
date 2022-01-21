from django.contrib import admin
from django.urls import path
from userapp.views import CreateKanal, CreateUser, DelateKanal, KanalList, UserList, anKanal
from youtubeapp.views import(
    CommentList, CreateComment, CreatePlaylist,CreateVideo,
    DelateComment, DelatePlaylist, DelateVideo,
    PlaylistList, VideoList, anComment, anPlaylist, anVideo,
    
) 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


doc_view = get_schema_view(
    openapi.Info(
        title = "Youtube",
        default_version = "v1",
        description="( REST API) Clone of Youtube using Django Rest Framework",
        contact = openapi.Contact("Umidjon Ahmadjonov <ahmadjonovumidjon782@gmail.com>"),

    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("list1/",PlaylistList.as_view()),
    path("list2/<int:pk>",anPlaylist.as_view()),
    path("list3/",CreatePlaylist.as_view()),
    path('list4/<int:pk>',DelatePlaylist.as_view()),
    path("com1/",CommentList.as_view()),
    path("com2/<int:pk>",anComment.as_view()),
    path("com3/",CreateComment.as_view()),
    path("com4/<int:pk>",DelateComment.as_view()),
    path("vid1/",VideoList.as_view()),
    path("vid2/<int:pk>",anVideo.as_view()),
    path("vid3/",CreateVideo.as_view()),
    path("vid4/<int:pk>",DelateVideo.as_view()),
    path("kanal1/",KanalList.as_view()),
    path("kanal2/<int:pk>",anKanal.as_view()),
    path("kanal3/",CreateKanal.as_view()),
    path("kanal4/<int:pk>",DelateKanal.as_view()),
    path("user1/",UserList.as_view()),
    path("user2/",CreateUser.as_view()),
     path('doc/',doc_view.with_ui("swagger", cache_timeout=0), name="swagger_doc"),
    path('redoc/',doc_view.with_ui("redoc", cache_timeout=0), name="redoc_doc"),
]

