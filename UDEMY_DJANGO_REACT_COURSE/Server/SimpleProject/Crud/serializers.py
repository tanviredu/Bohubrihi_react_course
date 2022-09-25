from rest_framework import serializers
from .models import Book,BookNumber

class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ["id","isbn_10","isbn_13"]



class BookSerializer(serializers.ModelSerializer):

    '''This is an Example of the nested serializer'''
    numbers = BookNumberSerializer(many=False) # many false means we get a single record
    class Meta:
        ''' Remember numers is a releted field and without BookNumber
            Serializer we only get the primary key of numbers
            we need separate serializer then we need to pass the serializer
            in this serializer
        '''
        model  = Book
        fields = ["id","title","description","price","cover","is_published","published","numbers"]
