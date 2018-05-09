import datetime

from mongoengine import (
    DateTimeField,
    Document,
    EmbeddedDocument,
    EmbeddedDocumentListField,
    StringField,
)


class Letter(Document):
    letter = StringField(required=True)
    
    meta = {
        'db_alias': 'core',
        'collection': 'letters',
    }
    
    def __str__(self):
        return 'Letter(letter="{}")'.format(self.letter)


class PartOfSpeech(Document):
    pos = StringField(required=True)
    
    meta = {
        'db_alias': 'core',
        'collection': 'parts',
    }
    
    def __str__(self):
        return 'PartOfSpeech(pos="{}")'.format(self.pos)


class Deriative(EmbeddedDocument):
    entry = StringField(required=True)
    
    def __str__(self):
        return 'Deriative(entry="{}")'.format(self.entry)


class Meaning(EmbeddedDocument):
    meaning = StringField(required=True)
    example = StringField(required=False)
    
    def __str__(self):
        return 'Meaning(meaning="{}", example="{}")'.format(self.meaning,
                                                            self.example)


class Word(Document):
    entry = StringField(required=True)
    cleaned_entry = StringField(required=True)
    pos = StringField(required=False)
    pronunciation = StringField(required=False)
    alt_pronunciation = StringField(required=False)
    deriatives = EmbeddedDocumentListField(Deriative)
    meanings = EmbeddedDocumentListField(Meaning)
    html = StringField()
    created_date = DateTimeField(default=datetime.datetime.now)
    
    meta = {
        'db_alias': 'core',
        'collection': 'words',
    }
    
    def __str__(self):
        return 'Word(entry="{}")'.format(self.entry)
