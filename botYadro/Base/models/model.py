from sqlalchemy import (
    Column,
    Integer,
    String, ForeignKey, DateTime, Boolean, BigInteger, Text, LargeBinary,CHAR,exists
)
from datetime import datetime
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()
class TelegramProfile(Base):
    __tablename__ = 'accounts_telegramprofile'
    id_telegram = Column(Integer, unique=True, nullable=False, primary_key=True)
    chat_id = Column(Integer, nullable=False)  # Поле chat_id, айди чата с ботом

class TelegramPostsWithBot(Base):
    __tablename__ = 'accounts_telegrampostswithbot'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Primary key
    thumbnail = Column(Text, nullable=True)  # Путь к изображению, аналог ImageField
    text = Column(Text, nullable=False)  # Основной текст
    button_text = Column(Text, nullable=True)  # Текст кнопки, аналог blank=True
    button_link = Column(Text, nullable=True)  # Ссылка для кнопки, аналог blank=True







