from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    class Meta:
        ordering = '-tag'

    def clean(self):
        count = 0
        for form in self.forms:
            if self.deleted_forms and self._should_delete_form(form):
                continue
            if form.cleaned_data.get('is_main'):
                count += 1
        if count > 1:
            raise ValidationError('Основной раздел, - может быть только один.')
        elif count == 0:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 3


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
