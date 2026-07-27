from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp


class RegistrationAdmin(FlaskForm):
    fname = StringField(
        'الاسم الاول', 
        validators=[
            DataRequired(message="هذا الحقل مطلوب"),
            Length(min=2, max=25, message="الاسم يجب أن يكون بين 2 و 25 حرفاً")
        ]
    )

    lname = StringField(
        'الاسم الاخير', 
        validators=[
            DataRequired(message="هذا الحقل مطلوب"),
            Length(min=2, max=25, message="الاسم يجب أن يكون بين 2 و 25 حرفاً")
        ]
    )

    username = StringField(
        'اسم المستخدم', 
        validators=[
            DataRequired(message="هذا الحقل مطلوب"),
            Length(min=2, max=25, message="اسم المستخدم يجب أن يكون بين 2 و 25 حرفاً")
        ]
    )

    email = StringField(
        'الايميل', 
        validators=[
            DataRequired(message="هذا الحقل مطلوب."),
            Email(message="الرجاء إدخال بريد إلكتروني صالح")
        ]
    )

    password = PasswordField(
        'كلمة السر',
        validators=[
            DataRequired(message="هذا الحقل مطلوب."),
            Regexp(
                r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_\-])[A-Za-z\d@$!%*?&_\-]{8,32}$",
                message="يجب أن تحتوي كلمة السر على حرف صغير وكبير ورقم ورمز، وأن تكون بين 8 و 32 حرفاً"
            )
        ]
    )

    submit = SubmitField('سجل')
class LoginAdmin(FlaskForm):
    email = StringField(
        'الايميل',
        validators=[
            DataRequired(message="هذا الحقل مطلوب."),
            Email(message="الرجاء إدخال بريد إلكتروني صالح")
        ]
    )

    password = PasswordField(
        'كلمة السر',
        validators=[
            DataRequired(message="هذا الحقل مطلوب")
        ]
    )

    submit = SubmitField('الدخول')
