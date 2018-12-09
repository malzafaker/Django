from __future__ import unicode_literals
from django.conf import settings


class StatusCodeAssertsMixin(object):

    def assertStatusCode(self, status_code, response):
        msg = "Wrong status code. Expected: %d - Returned: %d" % (status_code, response.status_code)
        self.assertEqual(status_code, response.status_code, msg=msg)

    def assert200(self, response):
        self.assertStatusCode(200, response)

    def assert201(self, response):
        self.assertStatusCode(201, response)

    def assert301(self, response):
        self.assertStatusCode(301, response)

    def assert302(self, response):
        self.assertStatusCode(302, response)

    def assert400(self, response):
        self.assertStatusCode(400, response)

    def assert401(self, response):
        self.assertStatusCode(401, response)

    def assert403(self, response):
        self.assertStatusCode(403, response)

    def assert404(self, response):
        self.assertStatusCode(404, response)

    def assert405(self, response):
        self.assertStatusCode(405, response)

    def assert500(self, response):
        self.assertStatusCode(500, response)

    def assert502(self, response):
        self.assertStatusCode(502, response)

