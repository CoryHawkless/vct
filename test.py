try:
    import os
    import unittest
    import json
    from flask_migrate import Migrate, MigrateCommand
    from flask_script import Manager
    import datetime
    from app import blueprint
    from app.main import create_app, db
    from app.main.model import user, blacklist, volume

    app = create_app('test')        # set config env here
except Exception as e:
    print("Exception occur:", str(e))

from flask_testing import TestCase
from manage import app


def register(self):
    """Register new user"""
    tester = app.test_client(self)
    response = tester.post(
        '/users/',
        data=json.dumps(dict(
            email="pradeep.farthyal@oodles.io",
            username="pradeep",
            password="password"
        )),
        content_type='application/json'
    )
    # from app.main.model.user import User
    # if response.status_code==201:
    #     user = User(
    #         email="pradeep.farthyal@oodles.io",
    #         password="password",
    #         registered_on=datetime.datetime.utcnow()
    #     )
    #     db.session.add(user)
    #     db.session.commit()
    return response


def login_anonymous_user(self):
    """login anonymous user"""
    tester = app.test_client(self)
    response = tester.post(
        '/auth/login',
        data=json.dumps(dict(
            email="pradeep.farthyal+7@oodles.io",
            password="password"
        )),
        content_type='application/json'
    )
    return response


"""Login Registered User"""
def login_registered_user(self):
    tester = app.test_client(self)
    response = tester.post(
        '/auth/login',
        data=json.dumps(dict(
            email="pradeep.farthyal@oodles.io",
            password="password"
        )),
        content_type='application/json'
    )
    return response


"""Show User Info"""
def show_user_info(self, res):
    tester = app.test_client(self)
    url = "/auth/user"
    payload = {}
    headers = {
        'Authorization': json.loads(res.data)['Authorization']
    }

    response = tester.post(url, headers=headers, data=payload)
    return response


"""Project Not Created"""
def project_creation(self, res):
    tester = app.test_client(self)
    url = "/projects/"
    data = {
        "name" : "user10Project123",
        "description" : "description10Project123"
    }

    headers = {
        'Authorization': json.loads(res.data)['Authorization']
    }
    response = tester.post(url, headers=headers, data=data)
    return response


"""Project Not Created"""
def get_project_details(self, res):
    tester = app.test_client(self)
    url = "/projects/"
    data = {}

    headers = {
        'Authorization': json.loads(res.data)['Authorization']
    }
    response = tester.get(url, headers=headers, data=data)
    return response


"""Project Delete"""
def get_project_deletion(self, res):
    tester = app.test_client(self)
    url = "/projects/"+json.loads(res.data)['id']
    data = {}

    headers = {
        'Authorization': json.loads(res.data)['Authorization']
    }
    response = tester.delete(url, headers=headers, data=data)
    return response


"""Create volume"""
def create_volumes(self, res):
    tester = app.test_client(self)
    url = "/volumes/"
    data = {
        "name": "NewVolumeName2",
        "size": 10,
        "description": "Some Descriptsion2",
        "type_id": json.loads(res.data)['type_id'],
        "project_id": json.loads(res.data)['id']
    }

    headers = {
        'Authorization': json.loads(res.data)['Authorization']
    }
    response = tester.delete(url, headers=headers, data=data)
    return response


"""Get volume by id"""
def get_volume_by_id(self, res):
    tester = app.test_client(self)
    url = "/volumes/"+json.loads(res.data)['id']
    data = {}
    headers = {
        'Authorization': json.loads(res.data)['Authorization']
    }
    response = tester.delete(url, headers=headers, data=data)
    return response


"""List of Volumes"""
def list_of_volumes(self, res):
    tester = app.test_client(self)
    url = "/volumes/"
    data = {
        "project_id": json.loads(res.data)['id']
    }
    headers = {
        'Authorization': json.loads(res.data)['Authorization']
    }
    response = tester.get(url, headers=headers, data=data)
    return response


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestAuthBlueprint(BaseTestCase):
    """New User Register"""
    def test_new_user_register(self):
        response = register(self)
        statuscode = response.status_code
        self.assertEqual(statuscode, 201)

    """login anonymous user"""
    def test_login_anonymous_user(self):
        response = login_anonymous_user(self)
        statuscode = response.status_code
        self.assertEqual(statuscode, 401)

    """login registered user"""
    def test_login_registered_user(self):
        response = register(self)
        new_response = login_registered_user(self)
        statuscode = new_response.status_code
        self.assertEqual(statuscode, 200)

    """Show User Info"""
    def test_login_user_details(self):
        response = register(self)
        login_response = login_registered_user(self)
        user_info_response = show_user_info(self,login_response)
        statuscode = user_info_response.status_code
        self.assertEqual(statuscode, 200)

    """Project Not Created"""
    def test_project_not_created(self):
        response = register(self)
        login_response = login_registered_user(self)
        project_info_response = project_creation(self, login_response)
        statuscode = project_info_response.status_code
        self.assertEqual(statuscode, 400)

    """Project Creation"""
    def test_project_creation(self):
        response = register(self)
        login_response = login_registered_user(self)
        project_info_response = project_creation(self, login_response)
        statuscode = project_info_response.status_code
        self.assertEqual(statuscode, 200)

    # """Get Project Details"""
    def test_project_creation(self):
        response = register(self)
        login_response = login_registered_user(self)
        project_info_response = project_creation(self, login_response)
        statuscode = project_info_response.status_code
        self.assertEqual(statuscode, 200)
    #
    # """Delete Project Details"""
    def test_project_deletion(self):
        response = register(self)
        login_response = login_registered_user(self)
        project_info_response = project_creation(self, login_response)
        if project_info_response.status_code == 200:
            delete_project_response = get_project_deletion(self, project_info_response)
            statuscode = delete_project_response.status_code
            self.assertEqual(statuscode, 200)
        else:
            statuscode = project_info_response.status_code
            self.assertEqual(statuscode, 400)
    #
    # """Create Volumes for Project"""
    def test_volume_creation(self):
        response = register(self)
        login_response = login_registered_user(self)
        project_info_response = project_creation(self, login_response)
        if project_info_response.status_code == 200:
            volume_response = create_volumes(self, project_info_response)
            statuscode = volume_response.status_code
            self.assertEqual(statuscode, 200)
        else:
            statuscode = project_info_response.status_code
            self.assertEqual(statuscode, 400)
    #
    # """Get Volumes by id"""
    def test_get_volume_id(self):
        response = register(self)
        login_response = login_registered_user(self)
        project_info_response = project_creation(self, login_response)
        if project_info_response.status_code == 200:
            volume_response = create_volumes(self, project_info_response)
            volume_by_id_res = get_volume_by_id(self, volume_response)
            statuscode = volume_by_id_res.status_code
            self.assertEqual(statuscode, 200)
        else:
            statuscode = project_info_response.status_code
            self.assertEqual(statuscode, 400)
    #
    # """List all Volumes"""
    def test_list_all_volume(self):
        response = register(self)
        login_response = login_registered_user(self)
        project_info_response = project_creation(self, login_response)
        list_volumes_response = list_of_volumes(self, project_info_response)
        # volume_response = create_volumes(self, project_info_response)
        # volume_by_id_res = get_volume_by_id(self, volume_response)
        statuscode = list_volumes_response.status_code
        self.assertEqual(statuscode, 200)


if __name__ == '__main__':
    unittest.main()
