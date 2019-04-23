#!/usr/bin/python
# -*-coding:utf-8-*-


from django import template
from django.utils.html import format_html,format_html_join


register = template.Library()






@register.filter   # filter只能对一个参数传入有效,调用到时候这样用  {{ xx.line  | ljf_power}}
def jia_lower(val):    #将数据库字段变成大写
    return val.lower()


@register.simple_tag()     # simple_tag能够对传入多个参数有效
def guess_page(current_page,loop_num):
    '''

    :param current_page:  当前页
    :param loop_num:     页数范围
    :return:
    '''


    offset = abs(current_page - loop_num)
    if offset < 3:   # 表示取当前页的前后三页
        if current_page == loop_num :
            page_element = '''       
            <li class="active"><a href="?page=%s">%s</a></li>
            '''%(loop_num,loop_num)                 # 拼html代码
        else:
            page_element = '''
            <li><a href="?page=%s">%s</a></li>
            '''%(loop_num,loop_num)
        return format_html(page_element)
    else:
        return ''




    # 前端页面
    # { % if page_num == customers_list.number %}
    #     <li class="active"><a href="?page= {{ page_num }}"> {{page_num}} </a> </li>
    # { % else %}
    #     <li class=""><a href="?page= {{ page_num }}">{{page_num}}</a> </li>
    # { % endif %}
    #
    #
    #
    # 前端页面 将前端 更换为python 写法
    # if current_page == loop_num:
    #     page_ele = ''' <li class="active"><a href="?page=%s">%s</a></li>'''' %(loop_num,loop_num)
    # else:
    #     page_ele = ''' <li class=""><a href="?page=%s">%s</a></li>'''' %%(loop_num,loop_num)