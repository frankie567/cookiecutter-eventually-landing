import unittest
from collections import namedtuple
from unittest.mock import patch

from flask import json

from {{cookiecutter.project_slug}}.app import app


class AppTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_get_app(self):
        response = self.app.get('/')

        self.assertEqual(response.status_code, 200)

    def test_post_email_not_provided(self):
        response = self.app.post('/', data={})

        self.assertEqual(response.status_code, 400)

    def test_post_email_invalid(self):
        response = self.app.post('/', data={'email': 'not-an-email'})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['detail'], 'The email address you provided is invalid.')

    @patch('requests.post')
    def test_post_email_valid(self, mocked_post):
        MockedRequestsResponse = namedtuple('MockedResponse', 'status_code')
        mocked_post.return_value = MockedRequestsResponse(status_code=201)

        email = 'test-email@cookiecutter.com'
        response = self.app.post('/', data={'email': email})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['detail'], 'Thank you!')

        self.assertEqual(mocked_post.call_count, 1)
        mocked_post_args, mocked_post_kwargs = mocked_post.call_args
        self.assertIn('{{cookiecutter.mailjet_contactslist_id}}', mocked_post_args[0])
        self.assertEqual(json.loads(mocked_post_kwargs['data']), {'Email': email, 'Action': 'addnoforce'})
