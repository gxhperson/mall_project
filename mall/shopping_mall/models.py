

# Create your models here.
from django.db import models
from django.db.models import ForeignKey


class Image(models.Model):
    brand=models.CharField('品牌名称',max_length=30) #作为外键
    product_img=models.ImageField('种类名称',upload_to='avatar',null=True)
    img=models.ImageField('轮播图图片',upload_to='avatar',null=True)

    class Meta:
        db_table = 'image'  # 可改变当前模型类对应的表名

class Commodity(models.Model):

    name=models.CharField('商品名称',max_length=30)
    description=models.CharField('商品描述',max_length=30)
    original_price=models.FloatField('原价')
    price=models.FloatField('售价')
    amount=models.IntegerField('购买数量')
    quantity=models.IntegerField('库存')
    sales_volumes=models.IntegerField('销量')
    status=models.CharField('状态',max_length=30,default='O') # o（on sale在售） s（sale out 售空）
    type=models.CharField('笔记本类型',max_length=30,default='轻薄笔记本')
    brand_id=ForeignKey(Image, on_delete=models.CASCADE)  #外键
    GPU_brand=models.CharField('显卡品牌',max_length=30)
    GPU_type=models.CharField('显卡类型',max_length=30)
    CPU_brand=models.CharField('处理器品牌',max_length=30)
    CPU_type=models.CharField('处理器类型',max_length=30)
    RAM=models.CharField('内存大小',max_length=30)
    hard_disk=models.CharField('硬盘大小',max_length=30)
    size=models.CharField('电脑尺寸',max_length=30)
    resolution_ratio=models.CharField('屏幕分辨率',max_length=30)
    operating_system=models.CharField('电脑操作系统',max_length=30)
    weight=models.CharField('重量',max_length=30)
    color=models.CharField('颜色',max_length=30)
    product_from=models.CharField('产地',max_length=30)
    purpose=models.CharField('用途',max_length=30) #办公/商务/影音多媒体
    level=models.CharField('档次',max_length=30) # 高档/普通
    group=models.CharField('用户群体',max_length=30) #儿童/青年/中年/老人

    class Meta:
        db_table = 'commodity'  # 可改变当前模型类对应的表名
