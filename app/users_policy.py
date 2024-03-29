from flask_login import current_user


class UsersPolicy:
    def __init__(self, id_book=None):
        self.id_book = id_book

    def create_book(self):
        return current_user.is_admin

    def read_book(self):
        return current_user.is_authenticated

    def update_book(self):
        return current_user.is_admin or current_user.is_moderator

    def delete_book(self):
        return current_user.is_admin

    def moderate_comment(self):
        return current_user.is_admin or current_user.is_moderator

    def comment_book(self):
        from models import Comment
        return Comment.query.filter(Comment.id_book == self.id_book).filter(Comment.id_users == current_user.id).first() is None and current_user.is_authenticated
    def nastya(self):
        return current_user.login == "nastya"