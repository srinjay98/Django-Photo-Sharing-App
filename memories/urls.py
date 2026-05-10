from django.urls import path

from .views import (

    feed_page,
    login_page,
    register_page,
    logout_page,

    create_post_page,

    like_post,
    delete_post,
)

urlpatterns = [

    # =========================================
    # HOME / FEED
    # =========================================

    path(
        '',
        feed_page,
        name='feed_page'
    ),

    # =========================================
    # AUTHENTICATION
    # =========================================

    path(
        'login/',
        login_page,
        name='login_page'
    ),

    path(
        'register/',
        register_page,
        name='register_page'
    ),

    path(
        'logout/',
        logout_page,
        name='logout_page'
    ),

    # =========================================
    # MEMORY POSTS
    # =========================================

    path(
        'create/',
        create_post_page,
        name='create_post_page'
    ),

    path(
        'like/<int:id>/',
        like_post,
        name='like_post'
    ),

    path(
        'delete/<int:id>/',
        delete_post,
        name='delete_post'
    ),
]