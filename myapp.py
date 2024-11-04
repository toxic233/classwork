from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 用于保护session

@app.route('/')
def index():
    return render_template('myindex.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 这里应该添加验证逻辑
        username = request.form['username']
        password = request.form['password']
        # 假设所有输入都是正确的，实际应用中需要验证用户名和密码
        flash('You were successfully logged in')
        return redirect(url_for('protected'))
    return render_template('mylogin.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 这里应该添加注册逻辑
        username = request.form['username']
        password = request.form['password']
        # 假设注册成功，实际应用中需要添加用户到数据库
        flash('You were successfully registered')
        return redirect(url_for('login'))
    return render_template('myregister.html')

@app.route('/protected')
def protected():
    return 'Logged in successfully!'

if __name__ == '__main__':
    app.run(debug=True)