from flaskblog import db
from flaskblog.models import User, Post
db.create_all()
user1 = User(username ='Pei',email='ru81o454@gmail.com',password ='gg')
user2 = User(username ='Ted',email='td@gmail.com',password ='gg')
db.session.add(user1,user2)
db.session.add(user2)
db.session.commit()
User.query.all()


post1 = Post(title= 'Blog 1', content='Content 1 ', user_id = 1)

post2 = Post(title= 'Blog 2', content='Content 2', user_id = 1)
Post.query.all()
db.session.add(post2)
db.session.add(post1)

db.session.rollback()

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
bcrypt.generate_password_hash('testing')

hashed_pwd = bcrypt.generate_password_hash('testing').decode('utf-8')
bcrypt.check_password_hash(hashed_pwd,'testing')

## Python Flask Tutorial: Full-Featured Web App Part 10 7:43