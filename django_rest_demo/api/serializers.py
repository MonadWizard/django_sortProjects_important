from rest_framework import serializers

from example.models import Industry, Company, Person

# today we use Model serializers , cause It's so easy and sort script

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ['id', 'name', 'code']


# for backlink we can use Hyper
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'industry')

# for backlink we can use Hyper
class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

