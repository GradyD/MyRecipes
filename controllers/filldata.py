#!/usr/bin/env python
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'models'))

import webapp2
from recipe import Recipe
from ingredient import Ingredient
from google.appengine.ext import ndb


class FillData(webapp2.RequestHandler):
  def get(self):
    recname = "Fried Chicken"
    rec = Recipe(id=recname, name=recname, totalprice=8.50, totaltime=0.5, healthrating=2, notes="Don't cook on high heat!")
    rec_key = rec.put()

    ingred = Ingredient(parent=rec.key, id="Chicken", name="Chicken", price=2.50)
    ingred.put()

    ingred1 = Ingredient(parent=rec.key, id="Flour", name="Flour", price=0.10)
    ingred1.put()

    ##key = ndb.Key("Recipe", "Fried Chicken")
    ##key.delete()

    self.response.write("Data filled!")
