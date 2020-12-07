from rest_framework import serializers
from api.models import Category, Word, WordList, WordNote, PracticeHistory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["uuid", "name", "description"]


class WordSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())
    
    class Meta:
        model = Word
        fields = ["uuid", "kanji", "kana", "category", "meaning"]


class WordListSerializer(serializers.ModelSerializer):
    words = serializers.PrimaryKeyRelatedField(many=True, queryset=Word.objects.all())
    
    class Meta:
        model = WordList
        fields = ["uuid", "name", "language", "words", "description"]


class WordNoteSerializer(serializers.ModelSerializer):
    associated_words = serializers.PrimaryKeyRelatedField(many=True, queryset=Word.objects.all())
    associated_categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())
    
    class Meta:
        model = WordNote
        fields = ["uuid", "title", "associated_words", "associated_categories", "is_published"]
        
        
class PracticeHistorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    
    class Meta:
        model = PracticeHistory
        fields = ["uuid", "last_update_date", "version", "data", "user"]