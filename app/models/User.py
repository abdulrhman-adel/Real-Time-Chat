from app import db
from app import bcrypt
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def set_password(self, pwd):
        # Hash the password using bcrypt
        password = bcrypt.generate_password_hash(pwd).decode('utf-8')
        self.password = password

    def check_password(self, user, pwd):
        # Check if the provided password matches the hashed password
        return bcrypt.check_password_hash(user.password, pwd)
        # return bcrypt.check_password_hash(pwd1, pwd2)

    def save(self):
        # Save the user to the database
        db.session.add(self)
        db.session.commit()

    @classmethod
    def create_table(cls):
        # Check if the table exists, and if not, create it
        if not db.engine.dialect.has_table(db.engine, cls.__tablename__):
            cls.__table__.create(db.engine)
