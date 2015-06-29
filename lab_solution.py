#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))



class MainHandler(webapp2.RequestHandler):
    def get(self):
    	template = jinja_environment.get_template('templates/main.html')
    	self.response.out.write(template.render())
    def post(self):
    	correct_msg = 'Correct!'
    	incorrect_msg = 'You must be a transplant!'
    	graded_messages= []
    	answer_count = 0
    	user_answers = [self.request.get('stanley'), self.request.get('willis')]
    	correct_answers = ['chicago', 'sears']
    	for i in range(len(correct_answers)):
	    	if user_answers[i].lower() == correct_answers[i]:
	    		answer_count += 1
	    		msg = correct_msg
	    	else:
	    		msg = incorrect_msg
	    	graded_messages.append(msg)
    	list = zip(user_answers, graded_messages)
    	template = jinja_environment.get_template('templates/results.html')
    	self.response.out.write(template.render({'answer_msg_list': list, 'count': answer_count}))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
