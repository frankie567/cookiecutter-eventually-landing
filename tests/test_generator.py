import importlib.util
import os.path
import pytest
import shutil
import unittest

from cookiecutter.main import cookiecutter


def load_module_from_path(module_name, path):
    module_spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module


class TestGenerator(unittest.TestCase):

    cookiecutter_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def setUp(self):
        # Generate test project with Cookiecutter
        cookiecutter(
            self.cookiecutter_path,
            no_input=True,
            extra_context={
                'title': 'Test project',
                'mailjet_apikey_public': 'public_key',
                'mailjet_apikey_private': 'private_key',
                'mailjet_contactslist_id': 'contactslist_id'
            }
        )
        self.test_project_path = os.path.join(self.cookiecutter_path, 'test_project')

    def tearDown(self):
        # Remove test project files
        shutil.rmtree(self.test_project_path, ignore_errors=True)

    def test_project_generated(self):
        # Project directory
        self.assertTrue(os.path.exists(self.test_project_path))

        # Flask app directory
        flask_app_path = os.path.join(self.test_project_path, 'test_project')
        self.assertTrue(os.path.exists(flask_app_path))

    def test_config_values_copied(self):
        config = load_module_from_path('test_project.config', os.path.join(self.test_project_path, 'test_project', 'config.py'))

        self.assertEqual(config.Config.MJ_APIKEY_PUBLIC, 'public_key')
        self.assertEqual(config.Config.MJ_APIKEY_PRIVATE, 'private_key')
        self.assertEqual(config.Config.MJ_CONTACTSLIST_ID, 'contactslist_id')

    def test_app(self):
        # Run the tests generated in test project
        return_code = pytest.main([os.path.join(self.test_project_path, 'test_project')])
        self.assertEqual(return_code, 0)
