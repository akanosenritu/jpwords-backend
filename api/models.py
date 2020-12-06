from django.db import models
import uuid


class Category(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"Category: {self.name}"
    

class Word(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kanji = models.CharField(max_length=200, blank=True)
    kana = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    meaning = models.TextField()
    
    
class WordList(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    words = models.ManyToManyField(Word)
    description = models.TextField()
    
    
class WordNote(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    associated_words = models.ManyToManyField(Word)
    associated_categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)
    

class PracticeHistory(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
