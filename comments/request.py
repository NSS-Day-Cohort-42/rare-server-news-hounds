import sqlite3
import json
from models import Comment, User, Post

def create_post(post):
    with sqlite3.connect("./rare.db")