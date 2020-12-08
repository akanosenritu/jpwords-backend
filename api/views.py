from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Category, Word, WordNote, WordList, PracticeHistory
from api.serializers import CategorySerializer, WordSerializer, WordNoteSerializer, WordListSerializer, PracticeHistorySerializer
from user.models import MyUser
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
    
    
class PracticeHistoryView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        queryset = PracticeHistory.objects.all()
        practice_history = get_object_or_404(queryset, user=request.user)
        serializer = PracticeHistorySerializer(practice_history)
        return Response(serializer.data)
    
    def post(self, request):
        try:
            old_practice_history = PracticeHistory.objects.get(user=request.user)
            serializer = PracticeHistorySerializer(old_practice_history, data=request.data,
                                                   context={"request": request})
        except PracticeHistory.DoesNotExist:
            serializer = PracticeHistorySerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

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
    
    
@ensure_csrf_cookie
def set_csrf_token(request):
    return JsonResponse({"details": "CSRF cookie set"})


@require_POST
def login_view(request, *args):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    if username is None or password is None:
        return JsonResponse({
            "errors": {
                "__all__": "Please enter both username and password"
            }
        }, status=400)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        print(f"User {username} logged in.")
        return JsonResponse({"detail": "Success"})
    return JsonResponse(
        {"detail": "Invalid credentials"},
        status=400,
    )


@require_POST
@login_required
def logout_view(request):
    print(f"User {request.user.username} is logging out.")
    logout(request)
    return JsonResponse(
        {"detail": "success"}
    )
