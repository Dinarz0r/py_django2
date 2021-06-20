from django.contrib import admin
from .models import Comments, News


class CommentsInLine(admin.TabularInline):
    model = Comments


class CommentsAdmin(admin.ModelAdmin):
    """
    Класс административной панели для удобства управления контентом
    связанного с комментариями.
    Attributes:
        list_display: = выводимые столбцы в административной панели
        list_filter: = фильтр поиска (в настоящий момент настроен по параметрам Username и комментариям)
        actions: delete_comments = функцию удаления комментария с заменой текста на "удалено администратором.")

    """
    list_filter = ['username']
    list_display = ['username', Comments.get_comment]
    Comments.get_comment.short_description = "Текст комментария"
    Comments.username.short_description = 'Имя'
    actions = ['delete_comments']

    def delete_comments(self, request, queryset):
        """Функция удаление комментария
        с заменой текста на "удалено администратором." """
        queryset.update(comment='удалено администратором.')

    delete_comments.short_description = 'Удаление комментария (безвозвратно!).'


class NewsAdmin(admin.ModelAdmin):
    """
    Класс административной панели для удобства управления контентом Новостей
    Attributes:
        list_display: = выводимые столбцы в административной панели
        list_filter: = фильтр поиска (в настоящий момент настроен по активности)
        actions: = добавили функцию массового перевод статуса активности новости
        inlines: = удобный редактор комментариев к новости (TabularInline)
    """
    list_display = ['id', 'title', 'create_at', 'update_at', 'activity_flag']
    list_filter = ['activity_flag']
    inlines = [CommentsInLine]
    actions = ['mark_as_active', 'mark_as_inactive']

    def mark_as_active(self, request, queryset):
        """Функция перевода статуса активности новости в "Активный" """
        queryset.update(activity_flag=1)

    def mark_as_inactive(self, request, queryset):
        """Функция перевода статуса активности новости в "Не активный" """

        queryset.update(activity_flag=0)

    mark_as_active.short_description = 'перевод новостей в статус “активно”'
    mark_as_inactive.short_description = 'перевод новостей в статус “неактивно”'


admin.site.register(Comments, CommentsAdmin)
admin.site.register(News, NewsAdmin)
