from app import app, db
from models import User
from forms import RegistrationForm

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return 'User registered successfully'
    return 'Register page'