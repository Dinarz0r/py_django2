from rest_framework import serializers
from app_goods.models import Item, ItemGroupModel


class GroupItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemGroupModel
        fields = ['id', 'group_name']


class ItemSerializer(serializers.ModelSerializer):
    # group_name = GroupItemSerializer(many=True)

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'group_name', 'weight']
        # depth = 1
