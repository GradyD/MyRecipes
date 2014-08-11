#!/usr/bin/env python

from google.appengine.ext import ndb

class Ingredient(ndb.Model):
  name = ndb.StringProperty()
  price = ndb.FloatProperty()
