import re
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, URLValidator, RegexValidator, ValidationError

def number_only(value):
    if (re.match(r'^[0-9]*$', value) == None):
        raise ValidationError(
            '%(value)s is not Number!',
            params={'value': value},
        )

# Create your models here.
# ユーザー管理
class Friend(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField()
    birthday = models.DateField()


# メッセージ管理
class Message(models.Model):
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('pub_date',)

# class Friend(models.Model):
#     # name = models.CharField(max_length=100, validators=[MinLengthValidator(10)])
#     name = models.CharField(max_length=100, validators=[RegexValidator(r'^[a-z]*$')])
#     # name = models.CharField(max_length=100, validators=[URLValidator()])
#     mail = models.EmailField(max_length=200, validators=[MinLengthValidator(10)])
#     gender = models.BooleanField()
#     age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)])
#     birthday = models.DateField()

    # def __str__(self):
    #     return '<Friend:id=' + str(self.id) + ',' + self.name + '(' + str(self.age) + ')>'