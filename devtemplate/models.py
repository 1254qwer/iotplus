from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid

# Create your models here.
class DevTemplate(models.Model):
    MQTT = 'MQTT'
    HTTP = 'HTTP'
    CoAP = 'CoAP'
    PROTOCOL_CHOICES = (
        (MQTT, 'MQTT'),
        (HTTP, 'HTTP'),
        (CoAP, 'CoAP'),
    )
    # 唯一标识，uuid是一串几乎不可能重复的唯一编码，uuid4()函数不需要参数，每次都会计算出一个不同的值，这个字段是不允许更改的
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    # 名字，blank=True代表可以在admin管理后台不填,max_length是必须指定的
    title = models.CharField(max_length=80,blank=True)
    # 设备描述，_用于国际化，不同语言的浏览器看到的结果不一样
    description = models.TextField(_(u'Description'),blank=True)
    # 设备图片，定义了上传的位置，数据库中存放的为路径字符串
    img = models.ImageField(upload_to='image',default='upload/none.jpg',blank=True)
    # 设备型号
    device_type = models.CharField(max_length=40,blank=True)
    # 是否允许动态接入设备
    is_custom_registered = models.BooleanField(default=False)
    # 协议类型，从固定的列表中选择
    protocol_type = models.CharField(max_length=200,choices=PROTOCOL_CHOICES,default=HTTP)
    # 更新与创建时间
    updated = models.DateTimeField(_(u'Updated date'),auto_now=True)
    created = models.DateTimeField(_(u'Created date'),auto_now_add=True)
    # 外键
    owner = models.ForeignKey('auth.user', on_delete=models.CASCADE)

    def __str__(self):
        return self.title