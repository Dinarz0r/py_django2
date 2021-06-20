from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from .models import Vacancy


def vacancy_list(request):
    # проверка прав в представлении
    # в has_perm <app>.<action>_<object_name>
    # (view - права для просмотра)
    # (edit - для редактирования)
    # @permission_required('app_employment.view_vacancy') - декоратор аналог данной вьюхи
    if not request.user.has_perm('app_employment.view_vacancy'):
        raise PermissionDenied()
    vacancies = Vacancy.objects.all()
    return render(request, 'employment/vacancy_list.html', {'vacancy_list': vacancies})
