from flask import Flask,render_template,request,session
app=Flask(__name__)
app.secret_key="010-5035-9396"
@app.route("/login/")
def login_page():
    return render_template("active_login.html")

@app.route("/user_info/")
def page_info():
    return render_template("login_page.html")

@app.route("/save_info/", methods=["GET","POST"])
def user_info():
    tmp_u_name=request.form["u_name"]
    tmp_u_number=request.form["u_number"]
    tmp_u_addr=request.form["u_addr"]
    tmp_u_age=request.form["u_age"]
    import mysql.connector
    dbconfig={'host':'localhost','user':'root','password':'','database':'login_info'}
    conn=mysql.connector.connect(**dbconfig)
    cursor=conn.cursor()
    SQL="INSERT INTO user_info (u_name,u_number,u_age,u_addr) VALUES(%s,%s,%s,%s);"
    cursor.execute(SQL,(tmp_u_name,tmp_u_number,tmp_u_age,tmp_u_addr))
    conn.commit()
    








    return render_template("login_info.html", html_u_name=tmp_u_name,
    html_u_number=tmp_u_number, html_u_addr=tmp_u_addr,html_u_age=tmp_u_age)



@app.route("/complete_login/", methods=["GET","POST"])
def login_complete():
    tmp_u_name = request.form["L_name"]
    tmp_u_number = request.form["L_number"]
    import mysql
    import mysql.connector
    dbconfig={'host':'localhost','user':'root','password':'','database':'login_info'}
    conn=mysql.connector.connect(**dbconfig)
    cursor=conn.cursor()
    SQL="SELECT * FROM user_info WHERE u_name=%s and u_number=%s ;"
    cursor.execute(SQL,(tmp_u_name,tmp_u_number))
    alldata=cursor.fetchall()

    session.clear()
    session["L_name"]=tmp_u_name
    session["L_number"]=tmp_u_number

    for rec in alldata:
        print(rec[0])
        print(rec[1])
        print(rec[2])
    cursor.close()
    conn.close()
    
    
    return render_template("complete_login.html", html_name=tmp_u_name, html_number=tmp_u_number)


app.run(debug=True)