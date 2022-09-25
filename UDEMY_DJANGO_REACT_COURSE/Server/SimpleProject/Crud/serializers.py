from rest_framework import serializers
from .models import Book,BookNumber,Character,Author

class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ["id","isbn_10","isbn_13"]


class BasicBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id","title","price"]

class CharacterSerializer(serializers.ModelSerializer):
    book = BasicBookSerializer(many=False)
    class Meta:
        model  = Character
        fields = ["id","name","book"]



class BasicCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Character
        fields = ["id","name"]




## book and author has many to many relationship



class AuthorSerializer(serializers.ModelSerializer):
    ''' This is author to book
        one author -> many books
     '''
    books = BasicBookSerializer(many=True)
    class Meta:
        model = Author
        fields = ["id","name",'books']

class BasicAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id","name"]


class BookSerializer(serializers.ModelSerializer):

    '''This is an Example of the nested serializer'''
    numbers = BookNumberSerializer(many=False) # many false means we get a single record
    characters = BasicCharacterSerializer(many=True)
    authors = BasicAuthorSerializer(many=True)
    class Meta:
        ''' Remember numers is a releted field and without BookNumber
            Serializer we only get the primary key of numbers
            we need separate serializer then we need to pass the serializer
            in this serializer
        '''
        model  = Book
        fields = ["id","title","description","price","cover","is_published","published","numbers","characters","authors"]


