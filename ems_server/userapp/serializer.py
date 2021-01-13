from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from userapp.models import User, Employee


class UserModelSerializer(ModelSerializer):
    class Meta:

        model = User
        fields = "__all__"
        # fields=('id','username','password','real_name','gender','re_pwd')

        extra_kwargs = {
            "username": {
                "required": True,
                "min_length": 2,
            },
        }

    def validate(self, attrs):
        """对重复密码进行校验"""
        # TODO 对重复密码进行校验
        # print(attrs)
        # pwd=attrs.get('password')
        # print(pwd)
        # re_pwd=attrs.pop('re_pwd')
        # print(pwd,re_pwd)
        # if pwd!=re_pwd or len(pwd)<6:
        #     raise serializers.ValidationError("密码不正确")
        return attrs

    def validate_username(self, value):
        """校验用户名是否重复"""
        # TODO 校验用户名是否重复
        return value


class EmployeeModelSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "emp_name", "salary", "full_img", "age", "img")

        extra_kwargs = {
            "full_img": {
                "read_only": True,
            },
            "img": {
                "write_only": True
            }
        }
