from flask import Flask,render_template,request
app = Flask(__name__)
@app.route("/show/info")
def index():
    return render_template("index.html")


@app.route("/register/info")
def register():
    return render_template("register.html")
@app.route("/do/reg",methods=["GET","POST"])
def do_reg():
    if request.method == "GET":
        print(request.args)
        return "注册成功"
    else:
        user = request.form.get("user")
        pwd = request.form.get("pwd")
        gender = request.form.get("gender")
        hobby_list = request.form.getlist("hobby")
        city = request.form.get("city")
        more = request.form.get("more")
        print(user, pwd, gender, hobby_list, city, more)
        return "注册成功"
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        usename = request.form.get("usename")
        passward = request.form.get("passward")
        print(usename, passward)
        return "登陆成功"

@app.route("/goods/info")
def goods():
    return render_template("goods.html")


if __name__ == "__main__":
    app.run()