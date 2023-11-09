from sqlalchemy.orm import identity
from werkzeug.security import generate_password_hash, check_password_hash
from api import sql, jwt


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


@jwt.user_identity_loader
def user_identity_lookup(user):
    """
    Register a callback function that takes whatever object is passed in as the
    identity when creating JWTs and converts it to a JSON serializable format.
    """
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    """
    Register a callback function that loads a user from your database whenever
    a protected route is accessed. This should return any python object on a
    successful lookup, or None if the lookup failed for any reason (for example
    if the user has been deleted from the database).
    """
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()
