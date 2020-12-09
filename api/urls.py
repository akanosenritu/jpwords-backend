from django.urls import path
from api import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"categories", views.CategoryViewSet)
router.register(r"words", views.WordViewSet)
router.register(r"word-lists", views.WordListViewSet)
router.register(r"word-notes", views.WordNoteViewSet)

urlpatterns = [
    path("generate-words-file/", views.generate_words_files),
    path("set-csrf-token/", views.set_csrf_token),
    path("login/", views.login_view),
    path("check-login/", views.is_logged_in),
    path("logout/", views.logout_view),
    path("registration/", views.registration_view),
    path("reset-password/", views.password_reset_view),
    path("practice-history/", views.PracticeHistoryView.as_view())
]

urlpatterns += router.urls
