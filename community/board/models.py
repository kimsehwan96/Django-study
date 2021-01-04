from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=128,
                                verbose_name='제목') #verbose_name -> 관리자페이지에서 보기 위한 내용
    contents = models.TextField(verbose_name='내용') #Text Field는 길이 제한 없다.

    writer = models.ForeignKey('user.User', on_delete=models.CASCADE, #관계형 DB. 모델 연결
                                 verbose_name='작성자')
                                 #외래키에 해당하는 사용자가 삭제되면 그 키를 갖고있는 데이터들도 모두 삭제 -> CASCADE
                                 #models.SET_NULL, models.SET_DEFAULT 같은 옵션도 있음.

    registered_dttm = models.DateTimeField(auto_now_add=True, 
                                  verbose_name="등록시간")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'board'
        ##DB에 테이블명 명시 가능
        verbose_name = '게시글'
        verbose_name_plural = '게시글' #관리자 페이지에서 복수형으로 보이는것 이렇게 강제로 바꿈