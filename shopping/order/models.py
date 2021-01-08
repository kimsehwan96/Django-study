from django.db import models

# Create your models here.
class Order(models.Model):
    #주문한 사용자
    user = models.ForeignKey(
        'user.User', #앱 안에있는 모델을 지정
        on_delete=models.CASCADE,
        verbose_name="사용자"
        )
    product = models.ForeignKey(
        'product.Product', 
        on_delete=models.CASCADE,
        verbose_name="상품"
        )
    quantity = models.IntegerField(
        verbose_name="수량"
        )
    registered_data = models.DateTimeField(
        auto_now_add=True,
        verbose_name="등록 날짜"
        )

    class Meta:
        db_table = 'shopping_order'
        verbose_name = '주문'
        verbose_name_plural = "주문"