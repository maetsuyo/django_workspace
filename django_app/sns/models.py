from django.db import models
from django.contrib.auth.models import User

# Create your models here.
## Messageテーブル
# 投稿されたメッセージを管理する
class Message(models.Model):
    # 投稿者ID
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_owner")

    #投稿内容
    contents = models.TextField(max_length=1000)
    # Goodの数
    good_count = models.IntegerField(default=0)
    # 投稿日時
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-pub_date",)


## Goodテーブル
# Goodされた情報を管理する
class Good(models.Model):
    # goodしたユーザー
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="good_owner")
    # goodしたコメント
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    # goodした日時
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '"' + str(self.message) + '" (by ' + str(self.owner) + ')'

    class Meta:
        ordering = ("-pub_date",)