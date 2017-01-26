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
import random
import socket
import string

from google.appengine.api import app_identity
from google.appengine.api import mail


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
    selected_time = ndb.StringProperty()
    # fname = ndb.StringProperty()
    # email = ndb.StringProperty()
    # lname = ndb.StringProperty()
    # country = ndb.StringProperty()
    # phonenumber = ndb.IntegerProperty()
    # address = ndb.StringProperty()
    # state = ndb.StringProperty()
    # pincode = ndb.IntegerProperty()
    # learningcenter = ndb.StringProperty()

class AvailableDates(ndb.Model):
    date = ndb.StringProperty()
    time = ndb.StringProperty(repeated=True)

def populateDates():
    datearr = ["22/12/2016 (Thursday)","23/12/2016 (Friday)","24/12/2016 (Saturday)","25/12/2016 (Sunday)","26/12/2016 (Monday)","27/12/2016 (Tuesday)","28/12/2016 (Wednesday)"]
    # timearr = ["09:00 AM - 11:00 AM","11:00 AM - 01:00 PM","01:00 PM - 03:00 PM","03:00 PM - 05:00 PM"]
    timearr = ["09:00 AM - 1:00 PM"]
    for i in datearr:
        data = AvailableDates()
        data.date = i
        data.time = timearr
        data.put()

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        # populateDates()
        template_values = {"authorized":True}
        template = JINJA_ENVIRONMENT.get_template('templates/landing.html')
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
        template = JINJA_ENVIRONMENT.get_template('templates/enrollment.html')
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
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
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
            enrolled.skype_id = self.request.get('skype_id')
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
        selected_time = self.request.get('selected_time')
        match = Enrollment().query(Enrollment.email == user_email).fetch()
        if len(match) > 0:
            applicant = match[0]
            applicant.selected_date = selected_date
            applicant.selected_time = selected_time
            applicant.put()
            self.response.write(selected_date+selected_time+user_email)
        else:
            self.response.write("unregistered user")

class SlotsHandler(webapp2.RequestHandler):
    def post(self):
        dataobj = {}
        match = AvailableDates().query().fetch()
        for i in match:
            dataobj[i.date] = i.time
        self.response.write(json.dumps(dataobj))

class ProgrammingDiploma(webapp2.RequestHandler):
    def get(self):
        template_values = {"authorized":True}
        template = JINJA_ENVIRONMENT.get_template('templates/programming_diploma.html')
        self.response.write(template.render(template_values))

class Navbar(webapp2.RequestHandler):
    def get(self):
        template_values = {"authorized":True}
        template = JINJA_ENVIRONMENT.get_template('templates/navbar_responsive.html')
        self.response.write(template.render(template_values))

# class SendEmailHandler(webapp2.RequestHandler):
#     """Serves the email address sign up form."""

#     def post(self):
#         user_address = self.request.get('email')
#         user_address = user_address.replace("%40","@")

#         if mail.is_email_valid(user_address):
#             confirmation_url = create_new_user_confirmation(user_address)
#             sender_address = (
#                 'FJU Support <{}@appspot.gserviceaccount.com>'.format(
#                     app_identity.get_application_id()))
#             subject = 'Confirm your registration'
#             body = """Thank you for creating an account!
# Please confirm your email address by clicking on the link below:
# {}
# """.format(confirmation_url)
#             mail.send_mail(sender_address, user_address, subject, body)
# # [END send-confirm-email]
#             self.response.content_type = 'text/plain'
#             self.response.write('An email has been sent to {}.'.format(
#                 user_address))


# class UserConfirmationRecord(ndb.Model):
#     """Datastore record with email address and confirmation code."""
#     user_address = ndb.StringProperty(indexed=False)
#     confirmed = ndb.BooleanProperty(indexed=False, default=False)
#     timestamp = ndb.DateTimeProperty(indexed=False, auto_now_add=True)


# def create_new_user_confirmation(user_address):
#     """Create a new user confirmation.
#     Args:
#         user_address: string, an email addres
#     Returns: The url to click to confirm the email address."""
#     id_chars = string.ascii_letters + string.digits
#     rand = random.SystemRandom()
#     random_id = ''.join([rand.choice(id_chars) for i in range(42)])
#     record = UserConfirmationRecord(user_address=user_address,
#                                     id=random_id)
#     record.put()
#     return 'https://{}/user/confirm?code={}'.format(
#         socket.getfqdn(socket.gethostname()), random_id)


# class ConfirmEmailHandler(webapp2.RequestHandler):
#     """Invoked when the user clicks on the confirmation link in the email."""

#     def get(self):
#         code = self.request.get('code')
#         if code:
#             record = ndb.Key(UserConfirmationRecord, code).get()
#             # 2-hour time limit on confirming.
#             if record and (datetime.datetime.now() - record.timestamp <
#                            datetime.timedelta(hours=2)):
#                 record.confirmed = True
#                 record.put()
#                 self.response.content_type = 'text/plain'
#                 self.response.write('Confirmed {}.'
#                                     .format(record.user_address))
#                 return
#         self.response.status_int = 404

app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/enroll', EnrollmentHandler),
    ('/course', ProjectPageHandler),
    ('/formsubmit',formSubmitHandler),
    ('/datesubmit',dateSubmitHandler),
    ('/getavailableslots',SlotsHandler),
    ('/programming_diploma', ProgrammingDiploma),
    ('/navbar', Navbar)
    # ('/sendmail', SendEmailHandler)
    # ('/user/confirm', ConfirmEmailHandler),
], debug=True)
