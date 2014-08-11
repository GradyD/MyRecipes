#!/usr/bin/env python

from google.appengine.ext import ndb

class Recipe(ndb.Model):
  name = ndb.StringProperty()
  totalprice = ndb.FloatProperty()
  totaltime = ndb.FloatProperty()
  healthrating = ndb.IntegerProperty()
  notes = ndb.StringProperty()
