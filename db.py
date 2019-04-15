import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import settings

Base = declarative_base()

class User (Base):
    __tablename__ = 'users'

    id = sa.Column (sa.Integer, primary_key = True)
    user_id = sa.Column (sa.Integer)
    first_name = sa.Column (sa.String)
    last_name = sa.Column (sa.String)
    username = sa.Column (sa.String)
    chat_id = sa.Column (sa.Integer)
    
    def __repr__(self):
        return '<User user_id={}, first_name={}, last_name={}, username={}'.format(self.user_id, self.first_name, self.last_name, self.username)

class Work_table (Base):
    __tablename__ = 'info'

    id = sa.Column (sa.Integer, primary_key=True)
    name = sa.Column (sa.String(25))
    surname = sa.Column (sa.String(35), nullable=False)
    n_phone = sa.Column (sa.String, nullable = True)
    n_mail = sa.Column (sa.String, nullable = False)
    info = sa.Column (sa.Text(200))

    def __repr__(self):
        return '<Work_table name={}, surname={}, n_phone={}, n_mail={}>'.format(self.name, self.surname, self.n_phone, self.n_mail)


engine = sa.create_engine (settings.DATABASE_URI, echo = False)
Base.metadata.create_all (bind=engine)
Session = sessionmaker (bind=engine)

session = Session()


# Функция проверки и добавления данных о пользователе в БД
def get_or_create_user(effective_user, message):
    # Защита от ошибки unique=True (повторения данных)
    new_user = session.query(User).filter(User.user_id == effective_user.id).count()
    if not new_user:
        user_id = effective_user.id
        first_name = effective_user.first_name
        last_name = effective_user.last_name
        username = effective_user.username
        chat_id = message.chat.id
        new_user = User(user_id = user_id, first_name = first_name, last_name = last_name,
                    username = username, chat_id = chat_id)
        session.add (new_user)
        session.commit()
    new_user = session.query(User).filter(User.user_id == effective_user.id).first()
    return new_user 


# Функция добавления данных о человеке в БД полученных из диалога
def get_or_create_info (user_data):
    new_info = Work_table()
    new_info.name = user_data['anketa_name']
    new_info.surname = user_data['anketa_surname']
    new_info.n_phone = user_data['anketa_nomer']
    new_info.n_mail = user_data['anketa_mail']
    new_info.info = user_data['anketa_info']
    session.add (new_info)
    session.commit()
    return new_info

'''# Функция проверки на наличие смайла у пользователя в БД (если нет то сохраняем ее в БД)
def get_user_emo(user):
    if not user.emo:
        user.emo = choice (settings.USER_EMOJI)
        session.add (user)
        session.commit()
    return emojize(user.emo, use_aliases=True)

# Функция замены смайла у пользователя БД
def get_user_emo_change(user):
    user.emo = choice (settings.USER_EMOJI)
    session.add (user)
    session.commit()
    return emojize(user.emo, use_aliases=True)
    '''