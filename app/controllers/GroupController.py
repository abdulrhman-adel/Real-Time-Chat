from flask import redirect, url_for, render_template, flash, session
from app.models.Group import Group
from app import db
import secrets
import string

class GroupController:

    @staticmethod
    def generate_random_code(length=6):
        # Define the characters to use for generating the code
        characters = string.ascii_letters + string.digits
        # Generate a random code with the specified length
        random_code = ''.join(secrets.choice(characters) for _ in range(length))
        return random_code

    @staticmethod
    def create_group(name, description):
        code = GroupController.generate_random_code()
        group = Group(code=code, name=name, description=description)
        db.session.add(group)
        db.session.commit()
        return group

    @staticmethod
    def get_group_by_id(group_id):
        return Group.query.get(group_id)

    def get_group_by_code(code):
        return Group.query.filter_by(code=code).first()

    @staticmethod
    def get_groups_names():
        groups = Group.query.all()
        groups_names = []
        for group in groups:
            groups_names.append(group.name)
        return groups_names

    @staticmethod
    def get_all_groups():
        return Group.query.all()

    @staticmethod
    def update_group(group, name, description):
        group.name = name
        group.description = description
        db.session.commit()

    @staticmethod
    def delete_group(group):
        db.session.delete(group)
        db.session.commit()

