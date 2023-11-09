from werkzeug.security import generate_password_hash, check_password_hash
from api import sql


class User(sql.Model):
    """
    The User model to hold info about the user
    """

    __tablename__ = "User"
    id = sql.Column(sql.Integer, primary_key=True)
    username = sql.Column(sql.String(64), unique=True, nullable=False)
    password_hash = sql.Column(sql.String(128), nullable=False)

    @property
    def password(self):
        raise AttributeError("Password  is not an accessible property")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __str__(self):
        return f"id: {self.id}, username: {self.username}"

    # @staticmethod
    # def create_user(username, password):
    # user = User(username=username, password=password)
    # sql.session.add(user)
    # sql.session.commit()
    # return user
