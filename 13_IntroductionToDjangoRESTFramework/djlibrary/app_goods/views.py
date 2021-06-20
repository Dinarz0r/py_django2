from app_goods.entities import Item
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from app_goods.serializers import ItemSerializer, GroupItemSerializer
from app_goods.models import Item, ItemGroupModel
from rest_framework import generics


class ItemList(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        item_name = self.request.query_params.get('name')
        if item_name:
            queryset = queryset.filter(name__icontains=item_name)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class ItemGroupList(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = ItemGroupModel.objects.all()
    serializer_class = GroupItemSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
