from django.db import models

class User(models.Model):
    username = models.CharField(max_length=32,
                                verbose_name='사용자명') #verbose_name -> 관리자페이지에서 보기 위한 내용
    useremail = models.EmailField(max_length=128,
                                  verbose_name='사용자 이메일')
    password = models.CharField(max_length=256,
                                 verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
        ##DB에 테이블명 명시 가능
        verbose_name = '사용자'
        verbose_name_plural = '사용자' #관리자 페이지에서 복수형으로 보이는것 이렇게 강제로 바꿈
