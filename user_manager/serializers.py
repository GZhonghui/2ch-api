from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


# 对一个模型声明一个序列化器
class RegisterLoginSerializer(serializers.ModelSerializer):
    # 一些属性还是可以单独重新指定
    # 即使写在fields中，再重新作为类变量声明一遍
    username = serializers.CharField(
        # 针对单个字段的检验
        validators=[
            UniqueValidator(queryset=User.objects.all(), message="username exists")
        ]
    )
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "password")

    # 跨字段的校验
    def validate(self, attrs):
        return super().validate(attrs)

    # 更新数据库中的数据
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    # 在数据库中创建项目
    # validated_data是dict / OrderedDict
    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["username"], password=validated_data["password"]
        )
