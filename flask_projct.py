from flask import Flask, render_template, request, flash, redirect, url_for 
import sqlite3 
from form import RegistrationAdmin , LoginAdmin
from werkzeug.security import generate_password_hash, check_password_hash
import joblib
import numpy as np

app = Flask(__name__) 
app.config['SECRET_KEY'] = 'mariam20032003600'

model = joblib.load(r"Model/college1_model.pkl")
le = joblib.load(r"Model/label1_encoder.pkl")

college_majors = {
    "كلية العلوم الطبية": [
        "الطب", "طب الأسنان", "الصيدلة", "التمريض",
        "العلوم الصحية", "علوم المختبرات الطبية",
        "المعلوماتية الصحية", "التغذية السريرية",
        "العلاج الطبيعي", "الصحة العامة"
    ],

    "كلية علوم وهندسة الحاسب": [
        "علوم الحاسب", "هندسة البرمجيات", "الأمن السيبراني",
        "الذكاء الاصطناعي", "علم البيانات", "تقنية المعلومات",
        "هندسة الحاسب", "الشبكات"
    ],

    "كلية إدارة الأعمال": [
        "إدارة الأعمال", "التسويق", "المحاسبة", "المالية",
        "الموارد البشرية", "التجارة الإلكترونية", "التأمين وإدارة المخاطر",
        "المالية والاستثمار", "نظم المعلومات الإدارية",
        "إدارة سلسلة الإمداد"
    ],

    "كلية العلوم": [
        "الكيمياء", "الفيزياء", "الأحياء", "الرياضيات"
    ],

    "كلية الآداب والعلوم الإنسانية": [
        "التاريخ", "الأدب", "علم النفس", "علم الاجتماع",
        "الخدمة الاجتماعية", "اللغة العربية", "اللغة الإنجليزية",
        "الترجمة", "الإعلام الرقمي", "الفنون الجميلة", "التربية البدنية"
    ],

    "كلية القانون": [
        "القانون", "الشريعة", "الدراسات الإسلامية"
    ],

    "كلية الهندسة": [
        "الهندسة المدنية", "الهندسة الميكانيكية",
        "الهندسة الكهربائية", "الهندسة الصناعية",
        "العمارة", "التصميم الداخلي",
        "هندسة الطاقة المتجددة", "هندسة الأنظمة الميكانيكية"
    ]
}

@app.route("/")
def home():
    conn = sqlite3.connect("dbm1.db")
    cursor = conn.cursor() 
    cursor.execute( "SELECT  visits  FROM counter WHERE id= 1")
    visits = cursor.fetchone() [0]
    conn.close()
    return render_template("Home.html" , visits = visits )


@app.route('/start_test')
def start_test():
    conn = sqlite3.connect("dbm1.db") 
    cursor = conn.cursor()
    cursor.execute("UPDATE counter SET visits = visits + 1 WHERE id=1")
    conn.commit()
    conn.close()

    

@app.route("/radmin", methods=['GET', 'POST'])
def radmin():
    form = RegistrationAdmin()
    if form.validate_on_submit():
        conn = sqlite3.connect("dbm1.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM supervisors WHERE username=? OR email=?", 
                       (form.username.data, form.email.data))
        existing_user = cursor.fetchone()

        if existing_user:  
            if existing_user[3] == form.username.data:
                flash("اسم المستخدم موجود بالفعل. يرجى اختيار اسم آخر")
            elif existing_user[4] == form.email.data:   # العمود الرابع email
                flash("البريد الإلكتروني موجود بالفعل. يرجى استخدام بريد آخر")
            conn.close()
            return redirect(url_for('radmin'))

        hashed_password = generate_password_hash(form.password.data)

        cursor.execute("""
            INSERT INTO supervisors (fname, lname, username, email, password)
            VALUES (?, ?, ?, ?,?)
        """, (
            form.fname.data,
            form.lname.data,
            form.username.data,
            form.email.data,
            hashed_password
        ))

        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))

    return render_template("radmin.html", form=form)

@app.route("/ladmin", methods=['GET', 'POST'])
def ladmin():
    form = LoginAdmin()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        conn = sqlite3.connect("dbm1.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM supervisors WHERE email=?", (email,))
        admin = cursor.fetchone()
        conn.close()

        if admin and check_password_hash(admin[5], password): 
            return redirect(url_for('dashboard'))
        else:
            flash("البريد الإلكتروني أو كلمة المرور غير صحيحة")

    return render_template("ladmin.html", form=form)



@app.route("/dashboard")
def dashboard():
    conn = sqlite3.connect("dbm1.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM resulte")
    total_results = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM student_feedback")
    total_feedbacks = cursor.fetchone()[0]

    cursor.execute("""
        SELECT resulte_text, COUNT(*) as count 
        FROM resulte 
        GROUP BY resulte_text 
        ORDER BY count DESC
    """)
    result_stats = cursor.fetchall()

    top_college = result_stats[0][0] if result_stats else "—"

    cursor.execute("""
        SELECT resulte_text, COUNT(*) as count
        FROM resulte
        GROUP BY resulte_text
        ORDER BY count ASC
        LIMIT 1
    """)
    lowest_college = cursor.fetchone()
    lowest_college = lowest_college[0] if lowest_college else "—"

    cursor.execute("""
        SELECT feedback_text, date 
        FROM student_feedback  
        ORDER BY date DESC 
        LIMIT 5
    """)
    feedbacks = cursor.fetchall()

    conn.close()

    return render_template(
        "dashboard.html",
        total_results=total_results,
        total_feedbacks=total_feedbacks,
        result_stats=result_stats,
        top_college=top_college,
        lowest_college=lowest_college,
        feedbacks=feedbacks
    )
    
@app.route("/informtion")
def informtion():
    return render_template("informtion.html")


@app.route("/Forms", methods=['GET'])
def form():
    return render_template("form.html")



@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        feedback_text = request.form.get("message")

        conn = sqlite3.connect("dbm1.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO student_feedback (feedback_text, date) VALUES (?, DATE('now'))",
            (feedback_text,)
        )
        conn.commit()
        conn.close()
        flash("تم ارسال ردك بنجاح") 
    return render_template("feedback.html")



college_mapping = {
    "College of Medical Sciences": "كلية العلوم الطبية",
    "College of Computer Science and Engineering": "كلية علوم وهندسة الحاسب",
    "College of Business Administration": "كلية إدارة الأعمال",
    "College of Sciences": "كلية العلوم",
    "College of Humanities and Arts": "كلية الآداب والعلوم الإنسانية",
    "College of Law": "كلية القانون",
    "College of Engineering": "كلية الهندسة"
}




@app.route("/predict", methods=["POST"])
def predict(): 
    text_to_int = {
        "Never": 1, 
        "Rarely": 2,
        "Sometimes": 3,
        "Often": 4,
        "Always": 5
    }
    answers = []
    for i in range(20):
        value = request.form.get(f"q{i}") # q  من 0 حتئ 19
        if value is None:
            value = "Sometimes"  
        answers.append(text_to_int[value])

    X = np.array([answers]) 

    probs = model.predict_proba(X)[0] 
    top3_idx = np.argsort(probs)[-3:][::-1]  
    top3_encoded = model.classes_[top3_idx]  
    top3_colleges = le.inverse_transform(top3_encoded) 
    
    top3_colleges_ar = [college_mapping.get(i, i) for i in top3_colleges]
    
    results = []
    for i in top3_colleges:
          college_ar = college_mapping.get(i, i)
          results.append({
            "college": college_ar,
             "majors": college_majors.get(college_ar, [])
    })

    conn = sqlite3.connect("dbm1.db")
    cursor = conn.cursor()
    for college_ar in top3_colleges_ar:
       cursor.execute(
        "INSERT INTO resulte (resulte_text, date) VALUES (?, DATE('now'))",
        (college_ar,)
    )


    conn.commit()
    conn.close()
    return render_template("result.html", results=results)

if __name__ == "__main__":  
    app.run(debug=True) 


