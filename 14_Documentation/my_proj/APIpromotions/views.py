from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin, \
    CreateModelMixin
from rest_framework.generics import GenericAPIView
from APIpromotions.serializers import PromotionSerializer
from APIpromotions.models import PromotionsModel


class PromotionListView(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Представление для получения списка акция и создания новой акции"""
    serializer_class = PromotionSerializer

    def get_queryset(self):
        queryset = PromotionsModel.objects.all()
        return queryset

    def get(self, request):
        if not request.user.has_perm('APIpromotions.view_promotionsmodel'):
            print('У вас нет прав')
            raise PermissionDenied(detail='У вас нет прав для просмотра', code=403)
        return self.list(request)

    def post(self, request):
        return self.create(request)


class PromotionsDetailView(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    """Представление для получения детальной информации о скидке, а так же для его редактирования"""

    queryset = PromotionsModel.objects.all()
    serializer_class = PromotionSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if not request.user.has_perm('APIpromotions.delete_promotionsmodel'):
            print('У вас нет прав')
            raise PermissionDenied(detail='У вас нет прав', code=403)
        return self.destroy(request, *args, **kwargs)
