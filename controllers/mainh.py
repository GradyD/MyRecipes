#!/usr/bin/env python

import os
import webapp2

from google.appengine.ext.webapp import template
from recipe import Recipe
from google.appengine.ext import db

class MainHandler(webapp2.RequestHandler):

  def get(self):

    query = db.GqlQuery("SELECT * FROM Recipe")
    results = query.fetch(limit=100)

    nums = ""
    for recipe in results:
      nums += ", " + str(recipe.num)

    path = os.path.join(os.path.dirname(__file__) + '../../views', 'index.html')
    self.response.write(template.render(path, {"test": "test", "number": nums}))
