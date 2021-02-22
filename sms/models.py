from django.db import models


class Kurs(models.Model):
    title = models.CharField(verbose_name="Имя курс", max_length=20)

    def __str__(self):
        return self.title


class Students(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=20)
    sirname = models.CharField(verbose_name="Фамилия", max_length=20)
    kurs = models.ForeignKey (Kurs, on_delete=models.CASCADE)
    timeOfKurs = models.IntegerField(verbose_name='Время урок', null=True)
    dayOfDate = models.CharField(verbose_name="Дни в недели", max_length=20)
    telParents = models.IntegerField(verbose_name='Телефон родители', null=True)
    telMe = models.IntegerField(verbose_name='Мой телефон')
    group = models.IntegerField(verbose_name='Группа')

    def __str__(self):
        return self.name


class SaveMessage(models.Model):
    id_name = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
    data = models.DateTimeField(verbose_name='Время')
    typeOfMessage = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.id_name