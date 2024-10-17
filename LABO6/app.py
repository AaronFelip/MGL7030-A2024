from flask import Flask, render_template,request, g, url_for, redirect
from database import Database
from datetime import date
import re
import hashlib
import uuid
import secrets


app = Flask(__name__,static_url_path="",static_folder="static")

app.config['SECRET_KEY'] = secrets.token_hex(16) # nous y reviendrons

regex = r"[A-Za-z0-9#$%&'*+/=?@]{8,}" #possiblement incomplet
mdp_existant = re.compile(regex).match


def get_db():
    database = getattr(g, "_database", None)
    if database is None:
        g._database = Database()
    return g._database


def deconnection():
    database = getattr(g, "_database", None)
    if database is not None:
        database.deconnection()

