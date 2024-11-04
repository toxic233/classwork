# 导入Flask类
from flask import Flask

# 创建一个Flask应用实例
app = Flask(__name__)

# 使用route()装饰器告诉Flask哪个URL应该触发我们的函数
@app.route('/')
def hello_world():
    return 'Hello, World!'

# 判断当前脚本是否作为主程序运行
if __name__ == '__main__':
    # 运行Flask应用
    app.run(debug=True)