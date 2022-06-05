from flask import Flask,redirect,url_for,render_template,request,Response
from flask_mysqldb import MySQL
import io
import xlwt
import datetime
app=Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '******'
app.config['MYSQL_DB'] = 'project'
mysql=MySQL(app)
sec="0000"
@app.route("/")
def home():
    return render_template("home page.html")
@app.route("/about us")
def about_us():
    return render_template("about us.html")
@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        user = request.form["username"]
        pasw = request.form["password"]
        return redirect(url_for("login_check",user=user,pasw=pasw))
    else:
        return render_template("login.html")
@app.route("/<user>,<pasw>")
def login_check(user,pasw):
    cur = mysql.connect.cursor()
    cur.execute("SELECT * FROM teachers WHERE email='"+user+"' AND password='"+pasw+"'")
    data=cur.fetchall()
    cur.close()
    if data==():
        return redirect(url_for("login"))
    else:
        return redirect(url_for("sec_sel"))
@app.route("/security",methods=["POST","GET"])
def security():
    if request.method=="POST":
        security=request.form["security"]
        if security==sec:
            return redirect(url_for("add_teacher"))
        else:
            return redirect(url_for("security"))
    else:
        return render_template("security.html")
@app.route("/add_teacher",methods=["POST","GET"])
def add_teacher():
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        pasw=request.form["pass"]
        try:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO teachers (name,email,password)VALUES('"+name+"','"+email+"','"+pasw+"')")
            mysql.connection.commit()
            cur.close()
            return "<h1>Successfully Added Teacher Record</h1>"
        except Exception as e:
            return render_template("addt.html")
    else:
        return render_template("addt.html")
@app.route("/sec_sel",methods=["POST","GET"])
def sec_sel():
    if request.method == "POST":
        std = request.form["std"]
        div = request.form["div"]
        return redirect(url_for("choose",std=std,div=div))
    else:
        return render_template("class and sec.html")
@app.route("/choose<std>,<div>",methods=["POST","GET"])
def choose(std,div):
    if request.method == "POST":
        chose = request.form["chose"]
        return redirect(url_for("chose_check",std=std,div=div,chose=chose))
    else:
        return render_template("chose.html")
@app.route("/chose<std>,<div>,<chose>")
def chose_check(std,div,chose):
    if chose=="search" or chose=="delete" or chose=="update":
        return redirect(url_for("ask", std=std, div=div, chose=chose))
    if chose=="export":
        return redirect(url_for("export", std=std, div=div))
    if chose=="mark":
        return redirect(url_for("get_date", std=std, div=div))
    if chose=="add":
        return redirect(url_for("add", std=std, div=div))
    if chose == "report":
        return redirect(url_for("report"))
@app.route("/report",methods=["POST","GET"])
def report():
    if request.method=="POST":
        e=0
        lis_dat=[]
        attendance=[]
        count_eleven_a=0
        count_eleven_b=0
        count_eleven_c=0
        count_twelve_a=0
        count_twelve_b=0
        count_twelve_c=0
        tdays=request.form["tdays"]
        working=request.form["work"]
        working=int(working)
        year=[]
        month=[]
        c=1
        for i in tdays:
            if i=='-':
                c=0
            if c==1 and i!='-':
                year.append(i)
            if c==0 and i!='-':
                month.append(i)
        c=0
        month=str(month)
        year=str(year)
        month=month.replace("'","")
        month=month.replace("[","")
        month=month.replace("]","")
        month=month.replace(",","")
        month=month.replace(" ","")
        year=year.replace("'","")
        year=year.replace("[","")
        year=year.replace("]","")
        year=year.replace(",","")
        year=year.replace(" ","")
        tdays=month+'-'+year
        year=int(year)
        if month=="01" or month=="03" or month=="05" or month=="07" or month=="08" or month=="10" or month=="12":
            e=32
        if month=="04" or month=="06" or month=="09" or month=="11":
            e=31
        if month=="02" and year%4==0:
            e=30
        if month=="02" and year%4!=0:
            e=29
        for i in range(1,e):
            if i<10:
                i=str(i)
                i="0"+i
            else:
                i=str(i)
            date=i+"-"+tdays
            lis_dat.append(date)
            cur=mysql.connect.cursor()
            cur.execute("SELECT attendance FROM eleven_a_attendance WHERE date='"+date+"' AND attendance='Present'")
            eleven_a=cur.fetchall()
            count_eleven_a+=len(eleven_a)
            cur.execute("SELECT attendance FROM eleven_b_attendance WHERE date='"+date+"' AND attendance='Present'")
            eleven_b=cur.fetchall()
            count_eleven_b+=len(eleven_b)
            cur.execute("SELECT attendance FROM eleven_c_attendance WHERE date='"+date+"' AND attendance='Present'")
            eleven_c=cur.fetchall()
            count_eleven_c+=len(eleven_c)
            cur.execute("SELECT attendance FROM twelve_a_attendance WHERE date='"+date+"' AND attendance='Present'")
            twelve_a=cur.fetchall()
            count_twelve_a+=len(twelve_a)
            cur.execute("SELECT attendance FROM twelve_b_attendance WHERE date='"+date+"' AND attendance='Present'")
            twelve_b=cur.fetchall()
            count_twelve_b+=len(twelve_b)
            cur.execute("SELECT attendance FROM twelve_c_attendance WHERE date='"+date+"' AND attendance='Present'")
            twelve_c=cur.fetchall()
            count_twelve_c+=len(twelve_c)
            cur.close()
        eleven=count_eleven_a+count_eleven_b+count_eleven_c
        twelve=count_twelve_a+count_twelve_b+count_twelve_c
        eleven/=3
        per_eleven=100*eleven/working
        twelve/=3
        per_twelve=100*twelve/working
        per_eleven_a=100*count_eleven_a/working
        per_eleven_b=100*count_eleven_b/working
        per_eleven_c=100*count_eleven_c/working
        per_twelve_a=100*count_twelve_a/working
        per_twelve_b=100*count_twelve_b/working
        per_twelve_c=100*count_twelve_c/working
        per_eleven=str(per_eleven)
        per_eleven=per_eleven+"%"
        per_twelve=str(per_twelve)
        per_twelve=per_twelve+"%"
        per_eleven_a=str(per_eleven_a)
        per_eleven_a=per_eleven_a+"%"
        per_eleven_b=str(per_eleven_b)
        per_eleven_b=per_eleven_b+"%"
        per_eleven_c=str(per_eleven_c)
        per_eleven_c=per_eleven_c+"%"
        per_twelve_a=str(per_twelve_a)
        per_twelve_a=per_twelve_a+"%"
        per_twelve_b=str(per_twelve_b)
        per_twelve_b=per_twelve_b+"%"
        per_twelve_c=str(per_twelve_c)
        per_twelve_c=per_twelve_c+"%"
        output = io.BytesIO()
        workbook = xlwt.Workbook()
        sh=workbook.add_sheet("Report")
        sh.write(0,0,"Eleven A")
        sh.write(0,1,"Eleven B")
        sh.write(0,2,"Eleven C")
        sh.write(0,3,"Eleven")
        sh.write(0,4,"Twelve A")
        sh.write(0,5,"Twelve B")
        sh.write(0,6,"Twelve C")
        sh.write(0,7,"Twelve")
        sh.write(1,0,per_eleven_a)
        sh.write(1,1,per_eleven_b)
        sh.write(1,2,per_eleven_c)
        sh.write(1,3,per_eleven)
        sh.write(1,4,per_twelve_a)
        sh.write(1,5,per_twelve_b)
        sh.write(1,6,per_twelve_c)
        sh.write(1,7,per_twelve)
        workbook.save(output)
        output.seek(0)
        cur = mysql.connect.cursor()
        cur.execute("SELECT roll_no FROM eleven_a")
        roll_no = cur.fetchall()
        cur.execute("SELECT name FROM eleven_a")
        name = cur.fetchall()
        cur.execute("SELECT GR_No FROM eleven_a")
        grn = cur.fetchall()
        cur.execute("SELECT Gender FROM eleven_a")
        ge = cur.fetchall()
        cur.close()
        sh=workbook.add_sheet("Eleven A")
        sh.write(0,0,'GR No')
        sh.write(0,1,'Roll No')
        sh.write(0,2,'Name')
        sh.write(0,3,'Gender')
        idx=4
        for i in range(1,e):
            i=str(i)
            date=i+"-"+tdays
            sh.write(0,idx,date)
            idx+=1
        sh.write(0,idx,"Percentage")
        idx=1
        for i in range(len(roll_no)):
            gn = str(grn[i])
            gn = gn.replace(",", "")
            gn = gn.replace("(", "")
            gn = gn.replace(")", "")
            gn = gn.replace("'", "")
            gn = int(gn)
            roll_noin = str(roll_no[i])
            roll_noin = roll_noin.replace(",", "")
            roll_noin = roll_noin.replace("(", "")
            roll_noin = roll_noin.replace(")", "")
            roll_noin = roll_noin.replace("'", "")
            roll_noin = int(roll_noin)
            namein = str(name[i])
            namein = namein.replace(",", "")
            namein = namein.replace("(", "")
            namein = namein.replace(")", "")
            namein = namein.replace("'", "")
            for j in lis_dat:
                cur=mysql.connect.cursor()
                cur.execute("SELECT attendance FROM eleven_a_attendance WHERE name='"+namein+"' AND date='"+j+"'")
                result=cur.fetchall()
                if result==():
                    result="Holiday"
                else:
                    result=str(result)
                    result=result.replace(",","")
                    result=result.replace("(","")
                    result=result.replace(")","")
                    result=result.replace("'","")
                    if result=="Present":
                        result="P"
                        c+=1
                    else:
                        result="A"
                attendance.append(result)
            g = str(ge[i])
            g = g.replace(",", "")
            g = g.replace("(", "")
            g = g.replace(")", "")
            g = g.replace("'", "")
            sh.write(idx,0,gn)
            sh.write(idx,1,roll_noin)
            sh.write(idx,2,namein)
            sh.write(idx,3,g)
            idy=4
            for j in attendance:
                sh.write(idx,idy,j)
                idy+=1
            per=100*c/working
            per=str(per)
            per=per+"%"
            sh.write(idx,idy,per)
            c=0
            attendance=[]
            idx+=1
        workbook.save(output)
        output.seek(0)
        cur = mysql.connect.cursor()
        cur.execute("SELECT roll_no FROM eleven_b")
        roll_no = cur.fetchall()
        cur.execute("SELECT name FROM eleven_b")
        name = cur.fetchall()
        cur.execute("SELECT GR_No FROM eleven_b")
        grn = cur.fetchall()
        cur.execute("SELECT Gender FROM eleven_b")
        ge = cur.fetchall()
        cur.close()
        sh = workbook.add_sheet("Eleven B")
        sh.write(0, 0, 'GR No')
        sh.write(0, 1, 'Roll No')
        sh.write(0, 2, 'Name')
        sh.write(0, 3, 'Gender')
        idx = 4
        for i in range(1, e):
            i = str(i)
            date = i + "-" + tdays
            sh.write(0, idx, date)
            idx += 1
        sh.write(0, idx, "Percentage")
        idx = 1
        for i in range(len(roll_no)):
            gn = str(grn[i])
            gn = gn.replace(",", "")
            gn = gn.replace("(", "")
            gn = gn.replace(")", "")
            gn = gn.replace("'", "")
            gn = int(gn)
            roll_noin = str(roll_no[i])
            roll_noin = roll_noin.replace(",", "")
            roll_noin = roll_noin.replace("(", "")
            roll_noin = roll_noin.replace(")", "")
            roll_noin = roll_noin.replace("'", "")
            roll_noin = int(roll_noin)
            namein = str(name[i])
            namein = namein.replace(",", "")
            namein = namein.replace("(", "")
            namein = namein.replace(")", "")
            namein = namein.replace("'", "")
            for j in lis_dat:
                cur = mysql.connect.cursor()
                cur.execute("SELECT attendance FROM eleven_b_attendance WHERE name='" + namein + "' AND date='" + j + "'")
                result = cur.fetchall()
                if result == ():
                    result = "Holiday"
                else:
                    result = str(result)
                    result = result.replace(",", "")
                    result = result.replace("(", "")
                    result = result.replace(")", "")
                    result = result.replace("'", "")
                    if result == "Present":
                        result = "P"
                        c += 1
                    else:
                        result = "A"
                attendance.append(result)
            g = str(ge[i])
            g = g.replace(",", "")
            g = g.replace("(", "")
            g = g.replace(")", "")
            g = g.replace("'", "")
            sh.write(idx, 0, gn)
            sh.write(idx, 1, roll_noin)
            sh.write(idx, 2, namein)
            sh.write(idx, 3, g)
            idy = 4
            for j in attendance:
                sh.write(idx, idy, j)
                idy += 1
            per = 100 * c / working
            per = str(per)
            per = per + "%"
            sh.write(idx, idy, per)
            c = 0
            attendance = []
            idx += 1
        workbook.save(output)
        output.seek(0)
        cur = mysql.connect.cursor()
        cur.execute("SELECT roll_no FROM eleven_c")
        roll_no = cur.fetchall()
        cur.execute("SELECT name FROM eleven_c")
        name = cur.fetchall()
        cur.execute("SELECT GR_No FROM eleven_c")
        grn = cur.fetchall()
        cur.execute("SELECT Gender FROM eleven_c")
        ge = cur.fetchall()
        cur.close()
        sh = workbook.add_sheet("Eleven C")
        sh.write(0, 0, 'GR No')
        sh.write(0, 1, 'Roll No')
        sh.write(0, 2, 'Name')
        sh.write(0, 3, 'Gender')
        idx = 4
        for i in range(1, e):
            i = str(i)
            date = i + "-" + tdays
            sh.write(0, idx, date)
            idx += 1
        sh.write(0, idx, "Percentage")
        idx = 1
        for i in range(len(roll_no)):
            gn = str(grn[i])
            gn = gn.replace(",", "")
            gn = gn.replace("(", "")
            gn = gn.replace(")", "")
            gn = gn.replace("'", "")
            gn = int(gn)
            roll_noin = str(roll_no[i])
            roll_noin = roll_noin.replace(",", "")
            roll_noin = roll_noin.replace("(", "")
            roll_noin = roll_noin.replace(")", "")
            roll_noin = roll_noin.replace("'", "")
            roll_noin = int(roll_noin)
            namein = str(name[i])
            namein = namein.replace(",", "")
            namein = namein.replace("(", "")
            namein = namein.replace(")", "")
            namein = namein.replace("'", "")
            for j in lis_dat:
                cur = mysql.connect.cursor()
                cur.execute("SELECT attendance FROM eleven_c_attendance WHERE name='" + namein + "' AND date='" + j + "'")
                result = cur.fetchall()
                if result == ():
                    result = "Holiday"
                else:
                    result = str(result)
                    result = result.replace(",", "")
                    result = result.replace("(", "")
                    result = result.replace(")", "")
                    result = result.replace("'", "")
                    if result == "Present":
                        result = "P"
                        c += 1
                    else:
                        result = "A"
                attendance.append(result)
            g = str(ge[i])
            g = g.replace(",", "")
            g = g.replace("(", "")
            g = g.replace(")", "")
            g = g.replace("'", "")
            sh.write(idx, 0, gn)
            sh.write(idx, 1, roll_noin)
            sh.write(idx, 2, namein)
            sh.write(idx, 3, g)
            idy = 4
            for j in attendance:
                sh.write(idx, idy, j)
                idy += 1
            per = 100 * c / working
            per = str(per)
            per = per + "%"
            sh.write(idx, idy, per)
            c = 0
            attendance = []
            idx += 1
        workbook.save(output)
        output.seek(0)
        cur = mysql.connect.cursor()
        cur.execute("SELECT roll_no FROM twelve_a")
        roll_no = cur.fetchall()
        cur.execute("SELECT name FROM twelve_a")
        name = cur.fetchall()
        cur.execute("SELECT GR_No FROM twelve_a")
        grn = cur.fetchall()
        cur.execute("SELECT Gender FROM twelve_a")
        ge = cur.fetchall()
        cur.close()
        sh = workbook.add_sheet("Twelve A")
        sh.write(0, 0, 'GR No')
        sh.write(0, 1, 'Roll No')
        sh.write(0, 2, 'Name')
        sh.write(0, 3, 'Gender')
        idx = 4
        for i in range(1, e):
            i = str(i)
            date = i + "-" + tdays
            sh.write(0, idx, date)
            idx += 1
        sh.write(0, idx, "Percentage")
        idx = 1
        for i in range(len(roll_no)):
            gn = str(grn[i])
            gn = gn.replace(",", "")
            gn = gn.replace("(", "")
            gn = gn.replace(")", "")
            gn = gn.replace("'", "")
            gn = int(gn)
            roll_noin = str(roll_no[i])
            roll_noin = roll_noin.replace(",", "")
            roll_noin = roll_noin.replace("(", "")
            roll_noin = roll_noin.replace(")", "")
            roll_noin = roll_noin.replace("'", "")
            roll_noin = int(roll_noin)
            namein = str(name[i])
            namein = namein.replace(",", "")
            namein = namein.replace("(", "")
            namein = namein.replace(")", "")
            namein = namein.replace("'", "")
            for j in lis_dat:
                cur = mysql.connect.cursor()
                cur.execute("SELECT attendance FROM twelve_a_attendance WHERE name='" + namein + "' AND date='" + j + "'")
                result = cur.fetchall()
                if result == ():
                    result = "Holiday"
                else:
                    result = str(result)
                    result = result.replace(",", "")
                    result = result.replace("(", "")
                    result = result.replace(")", "")
                    result = result.replace("'", "")
                    if result == "Present":
                        result = "P"
                        c += 1
                    else:
                        result = "A"
                attendance.append(result)
            g = str(ge[i])
            g = g.replace(",", "")
            g = g.replace("(", "")
            g = g.replace(")", "")
            g = g.replace("'", "")
            sh.write(idx, 0, gn)
            sh.write(idx, 1, roll_noin)
            sh.write(idx, 2, namein)
            sh.write(idx, 3, g)
            idy = 4
            for j in attendance:
                sh.write(idx, idy, j)
                idy += 1
            per = 100 * c / working
            per = str(per)
            per = per + "%"
            sh.write(idx, idy, per)
            c = 0
            attendance = []
            idx += 1
        workbook.save(output)
        output.seek(0)
        cur = mysql.connect.cursor()
        cur.execute("SELECT roll_no FROM twelve_b")
        roll_no = cur.fetchall()
        cur.execute("SELECT name FROM twelve_b")
        name = cur.fetchall()
        cur.execute("SELECT GR_No FROM twelve_b")
        grn = cur.fetchall()
        cur.execute("SELECT Gender FROM twelve_b")
        ge = cur.fetchall()
        cur.close()
        sh=workbook.add_sheet("Twelve B")
        sh.write(0, 0, 'GR No')
        sh.write(0, 1, 'Roll No')
        sh.write(0, 2, 'Name')
        sh.write(0, 3, 'Gender')
        idx = 4
        for i in range(1, e):
            i = str(i)
            date = i + "-" + tdays
            sh.write(0, idx, date)
            idx += 1
        sh.write(0, idx, "Percentage")
        idx = 1
        for i in range(len(roll_no)):
            gn = str(grn[i])
            gn = gn.replace(",", "")
            gn = gn.replace("(", "")
            gn = gn.replace(")", "")
            gn = gn.replace("'", "")
            gn = int(gn)
            roll_noin = str(roll_no[i])
            roll_noin = roll_noin.replace(",", "")
            roll_noin = roll_noin.replace("(", "")
            roll_noin = roll_noin.replace(")", "")
            roll_noin = roll_noin.replace("'", "")
            roll_noin = int(roll_noin)
            namein = str(name[i])
            namein = namein.replace(",", "")
            namein = namein.replace("(", "")
            namein = namein.replace(")", "")
            namein = namein.replace("'", "")
            for j in lis_dat:
                cur = mysql.connect.cursor()
                cur.execute("SELECT attendance FROM twelve_b_attendance WHERE name='" + namein + "' AND date='" + j + "'")
                result = cur.fetchall()
                if result == ():
                    result = "Holiday"
                else:
                    result = str(result)
                    result = result.replace(",", "")
                    result = result.replace("(", "")
                    result = result.replace(")", "")
                    result = result.replace("'", "")
                    if result == "Present":
                        result = "P"
                        c += 1
                    else:
                        result = "A"
                attendance.append(result)
            g = str(ge[i])
            g = g.replace(",", "")
            g = g.replace("(", "")
            g = g.replace(")", "")
            g = g.replace("'", "")
            sh.write(idx, 0, gn)
            sh.write(idx, 1, roll_noin)
            sh.write(idx, 2, namein)
            sh.write(idx, 3, g)
            idy = 4
            for j in attendance:
                sh.write(idx, idy, j)
                idy += 1
            per = 100 * c / working
            per = str(per)
            per = per + "%"
            sh.write(idx, idy, per)
            c = 0
            attendance = []
            idx += 1
        workbook.save(output)
        output.seek(0)
        cur = mysql.connect.cursor()
        cur.execute("SELECT roll_no FROM twelve_c")
        roll_no = cur.fetchall()
        cur.execute("SELECT name FROM twelve_c")
        name = cur.fetchall()
        cur.execute("SELECT GR_No FROM twelve_c")
        grn = cur.fetchall()
        cur.execute("SELECT Gender FROM twelve_c")
        ge = cur.fetchall()
        cur.close()
        sh = workbook.add_sheet("Twelve C")
        sh.write(0, 0, 'GR No')
        sh.write(0, 1, 'Roll No')
        sh.write(0, 2, 'Name')
        sh.write(0, 3, 'Gender')
        idx = 4
        for i in range(1, e):
            i = str(i)
            date = i + "-" + tdays
            sh.write(0, idx, date)
            idx += 1
        sh.write(0, idx, "Percentage")
        idx = 1
        for i in range(len(roll_no)):
            gn = str(grn[i])
            gn = gn.replace(",", "")
            gn = gn.replace("(", "")
            gn = gn.replace(")", "")
            gn = gn.replace("'", "")
            gn = int(gn)
            roll_noin = str(roll_no[i])
            roll_noin = roll_noin.replace(",", "")
            roll_noin = roll_noin.replace("(", "")
            roll_noin = roll_noin.replace(")", "")
            roll_noin = roll_noin.replace("'", "")
            roll_noin = int(roll_noin)
            namein = str(name[i])
            namein = namein.replace(",", "")
            namein = namein.replace("(", "")
            namein = namein.replace(")", "")
            namein = namein.replace("'", "")
            for j in lis_dat:
                cur = mysql.connect.cursor()
                cur.execute("SELECT attendance FROM twelve_c_attendance WHERE name='" + namein + "' AND date='" + j + "'")
                result = cur.fetchall()
                if result == ():
                    result = "Holiday"
                else:
                    result = str(result)
                    result = result.replace(",", "")
                    result = result.replace("(", "")
                    result = result.replace(")", "")
                    result = result.replace("'", "")
                    if result == "Present":
                        result = "P"
                        c += 1
                    else:
                        result = "A"
                attendance.append(result)
            g = str(ge[i])
            g = g.replace(",", "")
            g = g.replace("(", "")
            g = g.replace(")", "")
            g = g.replace("'", "")
            sh.write(idx, 0, gn)
            sh.write(idx, 1, roll_noin)
            sh.write(idx, 2, namein)
            sh.write(idx, 3, g)
            idy = 4
            for j in attendance:
                sh.write(idx, idy, j)
                idy += 1
            per = 100 * c / working
            per = str(per)
            per = per + "%"
            sh.write(idx, idy, per)
            c = 0
            attendance = []
            idx += 1
        workbook.save(output)
        output.seek(0)
        return Response(output,mimetype="application/ms-excel",headers={"Content-Disposition": "attachment;filename=Students Report.xls"})
    else:
        x=datetime.date.today()
        m=x.strftime("%m")
        y=x.strftime("%Y")
        d=x.strftime("%d")
        y=int(y)
        if m=='01' and d!='31':
            y-=1
            y=str(y)
            m='12'
        elif d!='31' and (m=="03" or m=="05" or m=="07" or m=="08" or m=="10" or m=="12"):
            m=int(m)
            m-=1
            if m<10:
                m=str(m)
                m="0"+m
            else:
                m=str(m)
        elif d!='30' and (m=="04" or m=="06" or m=="09" or m=="11"):
            m=int(m)
            m-=1
            if m<10:
                m=str(m)
                m="0"+m
            else:
                m = str(m)
        elif d!='29' and m=="02" and y%4==0:
            m=int(m)
            m-=1
            m=str(m)
            m="0"+m
        elif d!='28' and m=="02" and y%4!=0:
            m=int(m)
            m-=1
            m=str(m)
            m="0"+m
        y=str(y)
        dat=y+"-"+m
        return render_template("get days.html",data=dat)
@app.route("/ask<std>,<div>,<chose>",methods=["POST","GET"])
def ask(std,div,chose):
    if request.method == "POST":
        name=request.form["name"]
        roll_no=request.form["roll_no"]
        if std=="11" and div=="a" and chose=="search":
            return redirect(url_for("search",tname="eleven_a",roll_no=roll_no,name=name))
        if std=="11" and div=="b" and chose=="search":
            return redirect(url_for("search",tname="eleven_b",roll_no=roll_no,name=name))
        if std=="11" and div=="c" and chose=="search":
            return redirect(url_for("search",tname="eleven_c",roll_no=roll_no,name=name))
        if std=="12" and div=="a" and chose=="search":
            return redirect(url_for("search",tname="twelve_a",roll_no=roll_no,name=name))
        if std=="12" and div=="b" and chose=="search":
            return redirect(url_for("search",tname="twelve_b",roll_no=roll_no,name=name))
        if std=="12" and div=="c" and chose=="search":
            return redirect(url_for("search",tname="twelve_c",roll_no=roll_no,name=name))
        if std=="11" and div=="a" and chose=="delete":
            return redirect(url_for("delete",tname="eleven_a",roll_no=roll_no,name=name))
        if std=="11" and div=="b" and chose=="delete":
            return redirect(url_for("delete",tname="eleven_b",roll_no=roll_no,name=name))
        if std=="11" and div=="c" and chose=="delete":
            return redirect(url_for("delete",tname="eleven_c",roll_no=roll_no,name=name))
        if std=="12" and div=="a" and chose=="delete":
            return redirect(url_for("delete",tname="twelve_a",roll_no=roll_no,name=name))
        if std=="12" and div=="b" and chose=="delete":
            return redirect(url_for("delete",tname="twelve_b",roll_no=roll_no,name=name))
        if std=="12" and div=="c" and chose=="delete":
            return redirect(url_for("delete",tname="twelve_c",roll_no=roll_no,name=name))
        if std=="11" and div=="a" and chose=="update":
            return redirect(url_for("update",tname="eleven_a",roll_no=roll_no,name=name))
        if std=="11" and div=="b" and chose=="update":
            return redirect(url_for("update",tname="eleven_b",roll_no=roll_no,name=name))
        if std=="11" and div=="c" and chose=="update":
            return redirect(url_for("update",tname="eleven_c",roll_no=roll_no,name=name))
        if std=="12" and div=="a" and chose=="update":
            return redirect(url_for("update",tname="twelve_a",roll_no=roll_no,name=name))
        if std=="12" and div=="b" and chose=="update":
            return redirect(url_for("update",tname="twelve_b",roll_no=roll_no,name=name))
        if std=="12" and div=="c" and chose=="update":
            return redirect(url_for("update",tname="twelve_c",roll_no=roll_no,name=name))
    else:
        return render_template("ask.html")
@app.route("/add<std>,<div>",methods=["POST","GET"])
def add(std,div):
    if std=="11":
        tname="eleven_"+div
    else:
        tname="twelve_"+div
    if request.method == "POST":
        name = request.form["name"]
        roll_no = request.form["roll_no"]
        gr = request.form["gr"]
        gender = request.form["gender"]
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO "+tname+"(GR_No,Roll_No,Name,Gender)VALUES('"+gr+"','"+roll_no+"','"+name+"','"+gender+"')")
        mysql.connection.commit()
        cur.close()
        return "<h1>Successfully Added Student Record</h1>"
    else:
        return render_template("add.html")
@app.route("/search<tname>,<roll_no>,<name>")
def search(tname,roll_no,name):
    cur = mysql.connect.cursor()
    cur.execute("SELECT * FROM "+tname+" WHERE Roll_No='" + roll_no + "' AND Name='" + name + "'")
    data = cur.fetchall()
    cur.close()
    if data==():
        return redirect(url_for("ask", std="11", div="a", chose="search"))
    else:
        return f"<h1>{data}</h1>"
@app.route("/delete<tname>,<roll_no>,<name>")
def delete(tname,roll_no,name):
    cur = mysql.connect.cursor()
    cur.execute("SELECT * FROM "+tname+" WHERE Roll_No='" + roll_no + "' AND Name='" + name + "'")
    data = cur.fetchall()
    cur.close()
    if data == ():
        return redirect(url_for("ask", std="11", div="a", chose="delete"))
    else:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM "+tname+" WHERE Roll_No='" + roll_no + "' AND Name='" + name + "'")
        mysql.connection.commit()
        cur.close()
        return "<h1>Successfully Deleted Student Record</h1>"
@app.route("/update<tname>,<roll_no>,<name>")
def update(tname,roll_no,name):
    cur = mysql.connect.cursor()
    cur.execute("SELECT * FROM "+tname+" WHERE Roll_No='" + roll_no + "' AND Name='" + name + "'")
    data = cur.fetchall()
    cur.close()
    if data == ():
        return redirect(url_for("ask", std="11", div="a", chose="update"))
    else:
        return redirect(url_for("get_update",tname=tname,proll_no=roll_no,pname=name))
@app.route("/get_update<tname>,<proll_no>,<pname>",methods=["POST","GET"])
def get_update(tname,proll_no,pname):
    if request.method == "POST":
        name = request.form["name"]
        roll_no = request.form["roll_no"]
        gr = request.form["gr"]
        gender = request.form["gender"]
        cur = mysql.connection.cursor()
        cur.execute("UPDATE "+tname+" SET Roll_No="+roll_no+" WHERE Roll_No='"+proll_no+"' AND Name='"+pname+"'")
        mysql.connection.commit()
        cur.execute("UPDATE "+tname+" SET Name='"+name+"' WHERE Roll_No='"+roll_no+"' AND Name='"+pname+"'")
        mysql.connection.commit()
        cur.execute("UPDATE "+tname+" SET GR_No='"+gr+"' WHERE Roll_No='"+roll_no+"' AND Name='"+name+"'")
        mysql.connection.commit()
        cur.execute("UPDATE "+tname+" SET Gender='"+gender+"' WHERE Roll_No='"+roll_no+"' AND Name='"+name+"'")
        mysql.connection.commit()
        cur.close()
        return "<h1>Successfully Updated Student Record</h1>"
    else:
        return render_template("update.html")
@app.route("/export<std>,<div>")
def export(std,div):
    if std=="11":
        tname="eleven_"+div+"_attendance"
    else:
        tname="twelve_"+div+"_attendance"
    cur=mysql.connect.cursor()
    cur.execute("SELECT date FROM "+tname+"")
    date = cur.fetchall()
    cur.execute("SELECT roll_no FROM "+tname+"")
    roll_no = cur.fetchall()
    cur.execute("SELECT name FROM "+tname+"")
    name = cur.fetchall()
    cur.execute("SELECT attendance FROM "+tname+"")
    attendance = cur.fetchall()
    cur.execute("SELECT GR_No FROM " + tname + "")
    grn = cur.fetchall()
    cur.execute("SELECT Gender FROM " + tname + "")
    ge = cur.fetchall()
    cur.close()
    # output in bytes
    output = io.BytesIO()
    # create WorkBook object
    workbook = xlwt.Workbook()
    # add a sheet
    sh = workbook.add_sheet('Students Report')
    # add headers
    sh.write(0,0,'Date')
    sh.write(0,1,'GR No.')
    sh.write(0,2,'Roll No.')
    sh.write(0,3,'Name')
    sh.write(0,4,'Gender')
    sh.write(0,5,'Attendance')
    idx=0
    for i in range(len(date)):
        datein=str(date[i])
        datein=datein.replace(",","")
        datein=datein.replace("(","")
        datein=datein.replace(")","")
        datein=datein.replace("'","")
        gn=str(grn[i])
        gn=gn.replace(",","")
        gn=gn.replace("(","")
        gn=gn.replace(")","")
        gn=gn.replace("'","")
        gn=int(gn)
        roll_noin=str(roll_no[i])
        roll_noin=roll_noin.replace(",","")
        roll_noin=roll_noin.replace("(","")
        roll_noin=roll_noin.replace(")","")
        roll_noin=roll_noin.replace("'","")
        roll_noin=int(roll_noin)
        namein=str(name[i])
        namein=namein.replace(",","")
        namein=namein.replace("(","")
        namein=namein.replace(")","")
        namein=namein.replace("'","")
        g=str(ge[i])
        g=g.replace(",","")
        g=g.replace("(","")
        g=g.replace(")","")
        g=g.replace("'","")
        attendancein=str(attendance[i])
        attendancein=attendancein.replace(",","")
        attendancein=attendancein.replace("(","")
        attendancein=attendancein.replace(")","")
        attendancein=attendancein.replace("'","")
        sh.write(idx+1,0,datein)
        sh.write(idx+1,1,gn)
        sh.write(idx+1,2,roll_noin)
        sh.write(idx+1,3,namein)
        sh.write(idx+1,4,g)
        sh.write(idx+1,5,attendancein)
        idx+=1
        workbook.save(output)
        output.seek(0)
    return Response(output,mimetype="application/ms-excel",headers={"Content-Disposition": "attachment;filename=Students Report.xls"})
@app.route("/get_date<std>,<div>",methods=["POST","GET"])
def get_date(std,div):
    if request.method=="POST":
        date=request.form["date"]
        day=[]
        month=[]
        year=[]
        c=0
        for i in date:
            if i=="-":
                c+=1
            elif c==0:
                year.append(i)
            elif c==1:
                month.append(i)
            elif c==2:
                day.append(i)
        day = str(day)
        month = str(month)
        year = str(year)
        day = day.replace("'", "")
        day = day.replace("[", "")
        day = day.replace("]", "")
        day = day.replace(",", "")
        day = day.replace(" ", "")
        month = month.replace("'", "")
        month = month.replace("[", "")
        month = month.replace("]", "")
        month = month.replace(",", "")
        month = month.replace(" ", "")
        year = year.replace("'", "")
        year = year.replace("[", "")
        year = year.replace("]", "")
        year = year.replace(",", "")
        year = year.replace(" ", "")
        date=day+"-"+month+"-"+year
        return redirect(url_for("mark_attendance",std=std,div=div,date=date))
    else:
        return render_template("get date.html")
@app.route("/mark_attendance<std>,<div>,<date>",methods=["POST","GET"])
def mark_attendance(std,div,date):
    if std == "11":
        tname = "eleven_" + div
        tnamea = "eleven_" + div + "_attendance"
    else:
        tname = "twelve_" + div
        tnamea = "twelve_" + div + "_attendance"
    if request.method == "POST":
        info=request.form
        for roll_no,status in info.items():
            roll=str(roll_no)
            roll=roll.replace(",","")
            roll=roll.replace("(","")
            roll=roll.replace("'","")
            sta=str(status)
            cur = mysql.connection.cursor()
            cur.execute("UPDATE "+tnamea+" SET attendance='"+sta+"' WHERE GR_No='"+roll+"'AND date='"+date+"'")
            mysql.connection.commit()
            cur.close()
        cur=mysql.connect.cursor()
        cur.execute("SELECT * FROM "+tnamea+" WHERE date='"+date+"'")
        mydata=cur.fetchall()
        cur.close()
        return render_template("see.html",data=mydata)
    else:
        cur = mysql.connect.cursor()
        cur.execute("SELECT Roll_No FROM "+tname+"")
        roll_no = cur.fetchall()
        cur.execute("SELECT Name FROM "+tname+"")
        name = cur.fetchall()
        cur.execute("SELECT GR_No FROM " + tname + "")
        gr = cur.fetchall()
        cur.execute("SELECT Gender FROM " + tname + "")
        gender = cur.fetchall()
        cur.execute("SELECT * FROM "+tname+"")
        result = cur.fetchall()
        cur.close()
        for i in range(len(roll_no)):
            roll=str(roll_no[i])
            roll=roll.replace(",","")
            roll=roll.replace("(","")
            roll = roll.replace(")","")
            n=str(name[i])
            n=n.replace(",","")
            n=n.replace("(","")
            n=n.replace(")","")
            gn=str(gr[i])
            gn=gn.replace(",","")
            gn=gn.replace("(","")
            gn=gn.replace(")","")
            g=str(gender[i])
            g=g.replace(",","")
            g=g.replace("(","")
            g=g.replace(")","")
            cur=mysql.connection.cursor()
            cur.execute("INSERT INTO "+tnamea+"(date,GR_No,roll_no,name,Gender)VALUES('"+date+"',"+gn+","+roll+","+n+","+g+")")
            mysql.connection.commit()
            cur.close()
        return render_template("mark attendance.html",data=result,date=date)
if __name__=="__main__":
    app.run(debug=True)
