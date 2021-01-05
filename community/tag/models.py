from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name="태그명")
    registered_dttm = models.DateTimeField(
        auto_now_add=True,
        verbose_name="등록시간"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tag'
        ##DB에 테이블명 명시 가능
        verbose_name = '게시글 태그'
        verbose_name_plural = '게시글 태그' #관리자 페이지에서 복수형으로 보이는것 이렇게 강제로 바꿈
