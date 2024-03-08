from django.contrib import admin
from .models import TodoModel

# Register your models here.
#admin.pyはadminサイトの管理画面にどのような情報を表示するか決めるファイル

#管理画面に対して何を登録するか
admin.site.register(TodoModel)
