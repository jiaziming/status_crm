#!/usr/bin/python
# -*-coding:utf-8-*-


from django.forms import Form,ModelForm
from CRM import models


class CustomerModelForm(ModelForm):
    class Meta:
        model = models.Customer
        exclude = ()