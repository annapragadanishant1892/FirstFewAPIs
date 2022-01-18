from rest_framework import serializers

from myapi.models import Person, Species




class SpeciesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    classification = serializers.CharField(max_length=100)
    language = serializers.CharField(max_length=10)

    def create(self, validated_data):
        return Species.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.classification = validated_data.get('classification', instance.classification)
        instance.language = validated_data.get('language', instance.language)
        instance.save()
        return instance


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    birth = serializers.DateField()
    eye_color = serializers.CharField(max_length=10)
    species = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.birth = validated_data.get('birth', instance.birth)
        instance.eye_color = validated_data.get('eye_color', instance.eye_color)
        instance.species = validated_data.get('species', instance.species)
        instance.save()
        return instance

