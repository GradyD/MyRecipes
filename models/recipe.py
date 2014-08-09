#!/usr/bin/env python

from google.appengine.ext import db

class Recipe(db.Model):
  num = db.IntegerProperty()
