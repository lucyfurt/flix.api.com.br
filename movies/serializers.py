from rest_framework import serializers
from movies.models import Movie

class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'
    
    def get_rate(self, obj):
        reviews = obj.reviews.all()
        if not reviews.exists():
            return 0
        total_stars = sum(review.stars for review in reviews)
        return total_stars / reviews.count()
    
    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError("O ano de lançamento não pode ser anterior a 1990.")
        return value
    
    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("O resumo não deve ser maior do que 200 caracteres.")
        return value
    