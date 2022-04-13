from django.contrib import admin


# Register your models here.

# models.pyから、EmployeeモデルとDepartmentモデルをインポートしておく
from .models import Employee, Department

# 以下の記述により、AdminダッシュボードからEmployeeとDepartmentが利用できるようになった。
admin.site.register(Employee)
admin.site.register(Department)


