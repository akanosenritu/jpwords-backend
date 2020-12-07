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
    path("practice-history/", views.PracticeHistoryView.as_view())
]

urlpatterns += router.urls
