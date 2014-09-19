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
from notification_controller import NotificationController


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')





app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/test', handler= 'notification_controller.NotificationController',  handler_method='test')
], debug=True)
