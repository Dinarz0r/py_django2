from rest_framework import serializers
from APIpromotions.models import PromotionsModel


class PromotionSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора Автора
    """
    discount_percentage = serializers.IntegerField(max_value=100, min_value=0)

    class Meta:
        model = PromotionsModel
        fields = ('id', 'title', 'discount_percentage', 'start_promotions_date', 'end_promotions_date')
