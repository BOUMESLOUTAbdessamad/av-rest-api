import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from database.models import setup_db, Hike, User, Trip

class AdventureTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client
        self.database_name = "adventure_test"
        self.database_path = "postgresql://{}/{}".format('postgres:123456@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        pass

    ### Tests for All GET requests ###

    def test_get_hikes_with_results(self):
        res = self.client().get('/api/v1/hikes')

        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(data['hikes']), 1)

    def test_get_hikes_without_results(self):
        res = self.client().get('/api/v1/hikes')
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(len(data['hikes']), 0)

    def test_hikes_details_with_results(self):
        res = self.client().get('/api/v1/hikes-detail/1')

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_hikes_details_without_results(self):
        res = self.client().get('/api/v1/hikes-detail/99')

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)


    def test_users_with_results(self):
        res = self.client().get('/api/v1/users')

        data = json.loads(res.data)
        self.assertEqual(len(data['users']), 2) # If 2 users in the db
        self.assertEqual(res.status_code, 200)

    def test_users_without_results(self):
        res = self.client().get('/api/v1/users')

        data = json.loads(res.data)
        self.assertEqual(len(data['users']), 0)
        self.assertEqual(res.status_code, 404)


    def test_get_trips_with_results(self):
        res = self.client().get('/api/v1/trips')

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(data['trips']), 1)

    def test_get_trips_without_results(self):
        res = self.client().get('/api/v1/trips')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(len(data['trips']), 0)


    def test_get_user_trips_with_results(self):
        res = self.client().get('/api/v1/users/1/trips')

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(len(data['trips']), 1)

    def test_get_user_trips_without_results(self):
        res = self.client().get('/api/v1/users/99/trips')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(len(data['trips']), 0)



    ### Tests for ALL POST requests ###
    def test_post_hike_with_results(self):
        res = self.client().post('/api/v1/hikes', 
                                 json={
                                        "available": True,
                                        "departs_from": "REYKJAVIK",
                                        "description": "Come far off the beaten track with us as we take in the natural wonders of Iceland’s best-known attractions in an exhilarating, full day adventure!",
                                        "difficulty": "Easy",
                                        "duration": "8-10 Hours",
                                        "group_max": 8,
                                        "group_min": 4,
                                        "min_age": 18,
                                        "pick_up": True,
                                        "price": 19000,
                                        "title": "GOLDEN CIRCLE TOUR WITH SUPER TRUCK AND SNOWMOBILE"
                                        }
                                 )
        data = json.loads(res.data)
        self.assertEqual(len(data['hikes']), 1)
        self.assertEqual(res.status_code, 200)

    def test_post_hike_without_results(self):
        res = self.client().post('/api/v1/hikes', json={})
        data = json.loads(res.data)
        self.assertEqual(len(data['hikes']), 0)
        self.assertEqual(res.status_code, 422)


    def test_post_trip_with_results(self):
        res = self.client().post('/api/v1/trips', json={ "hike_id": 1, "auth0_user_id": "github|34656913"})
        data = json.loads(res.data)
        self.assertEqual(len(data['trip']), 1)
        self.assertEqual(res.status_code, 200)

    def test_post_trip_without_results(self):
        res = self.client().post('/api/v1/trips', json={ "hike_id": 1, "auth0_user_id": ""})
        data = json.loads(res.data)
        self.assertEqual(len(data['trip']), 0)
        self.assertEqual(res.status_code, 422)


    ### Test for DELETE trip request ###

    def test_delete_trip_with_success(self):
        res = self.client().delete('/api/v1/trips/1')
        data = json.loads(res.data)
        self.assertEqual(data['sucess'], True)
        self.assertEqual(res.status_code, 200)

    def test_delete_trip_with_fail(self):
        res = self.client().delete('/api/v1/trips/99')

        self.assertEqual(res.status_code, 404)

    if __name__ == "__main__":
        unittest.main()
