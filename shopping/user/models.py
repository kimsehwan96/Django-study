from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(
        verbose_name="이메일"
    )
    password = models.CharField(max_length=64,
        verbose_name="비밀번호"
    )
    registered_data = models.DateTimeField(
        auto_now_add=True,
        verbose_name="사용자 등록 날짜"
    )

    class Meta:
        db_table = 'shopping_user'
        verbose_name = '유저'
        verbose_name_plural = "유저"