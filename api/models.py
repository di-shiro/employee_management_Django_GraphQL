from django.db import models

# Create your models here.


class Department(models.Model):
    dept_name = models.CharField(max_length=50)

    # このオブジェクトの返り値
    def __str__(self):
        return self.dept_name


class Employee(models.Model):
    name = models.CharField(max_length=50)
    join_year = models.IntegerField()
    # on_delete=models.CASCADEにして、カスケードデリートにする。
    # # Employeeと紐付いているDepartmentデータが削除された時、それに連鎖して自動的にEmployeeデータを削除する。
    # Djangoでは、自動的に逆参照が作成されその名称はデフォルトでは、emploee_setとなる。
    # そこで、related_name="employees"とすると、employeesという任意の名称に変更できる。
    department = models.ForeignKey(Department,
                                    related_name="employees",
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True)
    # 戻り値として employee name を返す
    def __str__(self):
        return self.name



