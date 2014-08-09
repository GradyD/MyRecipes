#!/usr/bin/env python
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'models'))

import webapp2
from recipe import Recipe
from google.appengine.ext import db


class FillData(webapp2.RequestHandler):
  def get(self):
    Recipe(num = 1).put()

    self.response.write("Data filled! " + nums)
