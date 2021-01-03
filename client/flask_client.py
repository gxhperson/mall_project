######################################################
#        > File Name: flask_client.py
#      > Author: GuoXiaoNao
 #     > Mail: 250919354@qq.com 
 #     > Created Time: Mon 20 May 2019 11:52:00 AM CST
 ######################################################

from flask import Flask, send_file
import sys


app = Flask(__name__)

@app.route('/index')
def index():
    #首页
    return send_file('templates/index.html')

@app.route('/login')
def login():
    #登录
    return send_file('templates/login.html')

@app.route('/register')
def register():
    #注册
    return send_file('templates/register.html')

@app.route('/forget_password')
def forget_password():
    #个人信息
    return send_file('templates/forget_password.html')

@app.route('/info_center')
def info_center():
    #修改个人信息
    return send_file('templates/info_center.html')

@app.route('/product_info')
def product_info():
    #修改密码
    return send_file('templates/product_info.html')


@app.route('/search_product')
def search_product():
    #发表博客
    return send_file('templates/search_product.html')


@app.route('/shopping_cart')
def shopping_cart():
    #个人博客列表
    return send_file('templates/shopping_cart.html')

# @app.route('/<username>/topics/detail/<t_id>')
# def topics_detail(username, t_id):
#     #博客内容详情
#     return send_file('templates/detail.html')
#

# @app.route('/test_api')
# def test_api():
#     #测试
#     return send_file('templates/test_api.html')

if __name__ == '__main__':
    app.run(debug=True)

