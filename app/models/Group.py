from app import db

class Group(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.TIMESTAMP(timezone=True), server_default=db.func.now())
    updated_at = db.Column(db.TIMESTAMP(timezone=True), server_default=db.func.now(), onupdate=db.func.now())
