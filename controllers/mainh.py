#!/usr/bin/env python

import os
import webapp2

from google.appengine.ext.webapp import template
from recipe import Recipe
from ingredient import Ingredient
from google.appengine.ext import ndb

class MainHandler(webapp2.RequestHandler):

  def get(self):
    rec_key = ndb.Key("Recipe", "Fried Chicken")
    q = Ingredient.query(ancestor=rec_key)

    rec = rec_key.get()
    recipes = [rec.name]

    path = os.path.join(os.path.dirname(__file__) + '../../views', 'index.html')
    self.response.write(template.render(path, {"recipes": recipes}))
