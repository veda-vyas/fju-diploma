#!/usr/bin/env python
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.ext import blobstore
from google.appengine.ext import ndb
from google.appengine.ext.webapp import blobstore_handlers

import os
import urllib
import jinja2
import webapp2
import datetime
import json
import re
import traceback
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)



allowed_emails = [
            'vy@fju.us',
            'Vedavyas.yeleswarapu@gmail.com'
        ]

class Enrollment(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    email = ndb.StringProperty()
    dob = ndb.StringProperty()
    gender = ndb.StringProperty()
    country = ndb.StringProperty()
    phonenumber = ndb.StringProperty()
    address1 = ndb.StringProperty()
    address2 = ndb.StringProperty()
    state = ndb.StringProperty()
    pincode = ndb.StringProperty()
    graduation_status = ndb.StringProperty()
    college = ndb.StringProperty()
    course = ndb.StringProperty()
    branch = ndb.StringProperty()
    GPA = ndb.StringProperty()
    skype_id = ndb.StringProperty()
    year_of_completion = ndb.StringProperty()
    selected_date = ndb.StringProperty()
    # fname = ndb.StringProperty()
    # email = ndb.StringProperty()
    # lname = ndb.StringProperty()
    # country = ndb.StringProperty()
    # phonenumber = ndb.IntegerProperty()
    # address = ndb.StringProperty()
    # state = ndb.StringProperty()
    # pincode = ndb.IntegerProperty()
    # learningcenter = ndb.StringProperty()


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {"authorized":True}
        template = JINJA_ENVIRONMENT.get_template('landing.html')
        self.response.write(template.render(template_values))

class EnrollmentHandler(webapp2.RequestHandler):
    def get(self):
        # user = users.get_current_user()
        # if user:
        #     url_linktext = 'Sign Out'
        #     url = users.create_logout_url(self.request.uri)
        #     user_email = user.email()
        #     match = Enrollment().query(Enrollment.email==user_email).fetch()
        #     if len(match) == 0: 
        # template_values = {"email":user_email, "authorized":True, "url_linktext": url_linktext, "url":url}
        template_values = {"email":"", "authorized":True, "url_linktext": "", "url":""}
        template = JINJA_ENVIRONMENT.get_template('enrollment.html')
        self.response.write(template.render(template_values))
        #     else:
        #         # self.redirect(users.create_login_url(self.request.uri))
        #         template_values = {"email":user_email, "authorized":True, "url_linktext": url_linktext, "url":url}
        #         template = JINJA_ENVIRONMENT.get_template('index.html')
        #         self.response.write(template.render(template_values))
        # else:
        #     self.redirect(users.create_login_url(self.request.uri))

class ProjectPageHandler(webapp2.RequestHandler):
    def get(self):
        # user = users.get_current_user()
        # if user:
        #     url_linktext = 'Sign Out'
        #     url = users.create_logout_url(self.request.uri)
        #     user_email = user.email()
        #     match = Enrollment().query(Enrollment.email == user_email).fetch()
            # if len(match) != 0:
                # template_values = {"email":user_email, "authorized":True, "url_linktext": url_linktext, "url":url}
        template_values = {"email":"", "authorized":True, "url_linktext": "", "url":""}
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
        #     else:
        #         url_linktext = 'Login with Another Email.'
        #         template_values = {"url_linktext": url_linktext, "url":url}
        #         template = JINJA_ENVIRONMENT.get_template('no_permission.html')
        #         self.response.write(template.render(template_values))

        # else:
        #     self.redirect(users.create_login_url(self.request.uri))

class formSubmitHandler(webapp2.RequestHandler):

    def post(self):
        # user = users.get_current_user()
        # if user:
            # email = user.email()
            # key_a = ndb.Key(Enrollment, email);
        user_email = self.request.get('email')
        match = Enrollment().query(Enrollment.email == user_email).fetch()
        if len(match) == 0:
            enrolled = Enrollment()
            # a = Enrollment.get_or_insert(email)
            enrolled.first_name = self.request.get('first_name')
            enrolled.last_name = self.request.get('last_name')
            enrolled.email = user_email
            enrolled.dob = self.request.get('dob')
            enrolled.gender = self.request.get('gender')
            enrolled.country = self.request.get('country')
            enrolled.phonenumber = self.request.get('phonenumber')
            enrolled.address1 = self.request.get('address1')
            enrolled.address2 = self.request.get('address2')
            enrolled.state = self.request.get('state')
            enrolled.pincode = self.request.get('pincode')
            enrolled.graduation_status = self.request.get('graduation_status')
            enrolled.college = self.request.get('college')
            enrolled.course = self.request.get('course')
            enrolled.branch = self.request.get('branch')
            enrolled.GPA = self.request.get('GPA')
            enrolled.year_of_completion = self.request.get('year_of_completion')

            # enrolled.learningcenter = self.request.get('learningcenter')
            enrolled.put()
            Query = Enrollment().query()
            selected_dates = Query.fetch(projection=[Enrollment.selected_date])
            my_list = []
            for item in selected_dates:
                if item.selected_date != None:
                    my_list.append(item.selected_date)

            obj = {
                'email': user_email, 
                'selected_dates': my_list,
            }
            self.response.write(json.dumps(obj))
        else:
            qry1 = Enrollment().query(Enrollment.email == user_email)
            qry2 = qry1.filter(Enrollment.selected_date != None)
            qry3 = qry2.filter(Enrollment.selected_date != "")
            match1 = qry3.fetch()
            if len(match1) > 0:
                self.response.write("redirect"+match1[0].selected_date+user_email)
            else:
                Query = Enrollment().query()
                selected_dates = Query.fetch(projection=[Enrollment.selected_date])
                my_list = []
                for item in selected_dates:
                    if item.selected_date != None:
                        my_list.append(item.selected_date)

                obj = {
                    'email': user_email, 
                    'selected_dates': my_list,
                }
                self.response.write(json.dumps(obj))

class dateSubmitHandler(webapp2.RequestHandler):
    def post(self):
        user_email = self.request.get('email')
        selected_date = self.request.get('selected_date')
        match = Enrollment().query(Enrollment.email == user_email).fetch()
        if len(match) > 0:
            applicant = match[0]
            applicant.selected_date = selected_date
            applicant.put()
            self.response.write(selected_date+user_email)
        else:
            self.response.write("unregistered user")

app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/enroll', EnrollmentHandler),
    ('/course', ProjectPageHandler),
    ('/formsubmit',formSubmitHandler),
    ('/datesubmit',dateSubmitHandler)
], debug=True)
