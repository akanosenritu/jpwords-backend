from django.http import JsonResponse
from rest_framework import viewsets
from api.models import Category, Word, WordNote, WordList
from api.serializers import CategorySerializer, WordSerializer, WordNoteSerializer, WordListSerializer
import datetime


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    
    
class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all().order_by("kana")
    serializer_class = WordSerializer
    
    
class WordNoteViewSet(viewsets.ModelViewSet):
    queryset = WordNote.objects.all().order_by("title")
    serializer_class = WordNoteSerializer
    
    
class WordListViewSet(viewsets.ModelViewSet):
    queryset = WordList.objects.all().order_by("name")
    serializer_class = WordListSerializer


def generate_words_files(request):
    d = dict()
    d["lastEdit"] = datetime.datetime.today().isoformat()
    d["words"] = list()
    for word in Word.objects.all().order_by("kana"):
        w = dict()
        w["uuid"] = word.uuid
        w["kana"] = word.kana
        w["kanji"] = word.kanji
        w["meaning"] = word.meaning
        w["category"] = [cat.name for cat in word.category.all().order_by("name")]
        d["words"].append(w)
    return JsonResponse(data=d, json_dumps_params={"ensure_ascii": False, "indent": 2})
    
    

