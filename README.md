
# Capstone Project | Adventure Vibe API v1.1.0 Documentation  [![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

After a busy week of hardwork, you may go out for a weekend alone or with your awesome friends, to walk, relax and feel the energy of nature. Adventure Vibe is a travel app for hikers. It allows you book a trip in one click.

(This project is similar to [Adventures.com](https://adventures.com))

With Adventure Vibe App you can:

- Display hikes.
- Delete hikes (dev)
- Add hikes
- Create trips
- Delete trips
- Users CRUD

Application URL: [adventure-vibes.onrender.com](https://adventure-vibes.onrender.com/) Hosted in Render Cloud Platform


Login Page : [Login](https://dev-aib6p7npbv32c4ov.us.auth0.com/authorize?audience=https://127.0.0.1:5000/&response_type=token&client_id=QGj5Sw2KpPZnDHpij5blTxiT4It5swSU&redirect_uri=https://adventure-vibes.onrender.com/api/v1/user-details)


# Get started

## Installation

Clone the project repository to your machine.

### Backend
Install python requirements.

```bash
  $ cd src
  $ pip install -r requirements.txt
```

### Frontend
Clone the React Native app project repository to your machine.
Install npm Pacakges

Plugins or plugin presets will be loaded automatically from `package.json`
```bash
  $ npm install
```

## Running Tests

To run tests, run the following commands

1 - Setup ENV variables

```bash
cd src

$ export FLASK_APP=api
$ export FLASK_DEBUG=True
```

2 - Run the flask App

```bash
$ flask run
```

3 - Run the React Native App

```bash
cd adventure-mobile
$ npx react-native run android
```

## API Reference

### Get all hikes

```http
GET /api/v1/hikes
```
Example
```http
$ curl http://127.0.0.1:5000/api/v1/hikes
```
Results (json)

```http
{
    "hikes": [
        {
            "available": true,
            "departs_from": "Oran",
            "description": "On this super jeep excursion, we take you off the beaten track and chase one of the world's most mysterious phenomena. Leave the city's bright lights behind to see the Northern Lights while your guide tells you about this natural wonder!",
            "difficulty": "Hard",
            "duration": "5 Hours",
            "group_max": 20,
            "group_min": 10,
            "id": 1,
            "min_age": "18",
            "pick_up": true,
            "price": 1500.0,
            "title": "SUPER JEEP NORTHERN LIGHTS HUNT - FREE PHOTOS INCLUDED"
        }
    ],
    "success": true
}
```


### Get hike detail

```http
GET /api/v1/hikes-detail/<int:hike_id>
```
Example
```http
$ curl http://127.0.0.1:5000/api/v1/hikes-detail/1
```
Results (json)

```http
{
    "hikes":
        {
            "available": true,
            "departs_from": "Oran",
            "description": "On this super jeep excursion, we take you off the beaten track and chase one of the world's most mysterious phenomena. Leave the city's bright lights behind to see the Northern Lights while your guide tells you about this natural wonder!",
            "difficulty": "Hard",
            "duration": "5 Hours",
            "group_max": 20,
            "group_min": 10,
            "id": 1,
            "min_age": "18",
            "pick_up": true,
            "price": 1500.0,
            "title": "SUPER JEEP NORTHERN LIGHTS HUNT - FREE PHOTOS INCLUDED"
        }
    ,
    "success": true
}
```

### Add a hike

```http
POST /api/v1/hikes
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`       | `string`  | **Required**. Hike title |
| `description` | `string`  | Hike description |
| `available`   | `boolean` | **Required**. Hike availability |
| `departs_from`| `string`  | **Required**. The trip start point |
| `difficulty`  | `string`  | **Required**. Difficulty level of the trip  |
| `duration`  | `string`  | **Required**. Duration of the trip  |
| `group_max`  | `int`  | **Required**. Maximum number of persons on the group of hikers |
| `group_min`  | `int`  | **Required**. Minimum number of persons on the group of hikers |
| `min_age`  | `string`  | **Required**. Minimum age of the hikers  |
| `price`  | `string`  | **Required**. Total Price of the trip  |


Example

```http
$ curl -X POST  -H "Content-Type: application/json" -d
 '{
    "available": true,
    "departs_from": "Oran",
    "description": "On this super jeep excursion, we take you off the beaten track and chase one of the world's most mysterious phenomena. Leave the city's bright lights behind to see the Northern Lights while your guide tells you about this natural wonder!",
    "difficulty": "Medium",
    "duration": "5 Hours",
    "group_max": 20,
    "group_min": 14,
    "min_age": "18",
    "pick_up": true,
    "price": 1500.0,
    "title": "SUPER JEEP NORTHERN LIGHTS HUNT - FREE PHOTOS INCLUDED"
}' http://127.0.0.1:5000/api/v1/hikes

```

### Delete a hike

```http
DELETE /api/v1/hikes/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. id of hike to delete |

Example
```http
$ curl -X DELETE http://127.0.0.1:5000/api/v1/hikes/3 
```

### Edit a hike

```http
PATCH /api/v1/hikes/<int:hike_id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`       | `string`  | **Required**. Hike title |
| `description` | `string`  | Hike description |
| `available`   | `boolean` | **Required**. Hike availability |
| `departs_from`| `string`  | **Required**. The trip start point |
| `difficulty`  | `string`  | **Required**. Difficulty level of the trip  |
| `duration`  | `string`  | **Required**. Duration of the trip  |
| `group_max`  | `int`  | **Required**. Maximum number of persons on the group of hikers |
| `group_min`  | `int`  | **Required**. Minimum number of persons on the group of hikers |
| `min_age`  | `string`  | **Required**. Minimum age of the hikers  |
| `price`  | `string`  | **Required**. Total Price of the trip  |


Example

```http
$ curl -X PATCH  -H "Content-Type: application/json" -d
 '{
    "available": true,
    "departs_from": "Oran",
    "description": "On this super jeep excursion, we take you off the beaten track and chase one of the world's most mysterious phenomena. Leave the city's bright lights behind to see the Northern Lights while your guide tells you about this natural wonder!",
    "difficulty": "Medium",
    "duration": "5 Hours",
    "group_max": 20,
    "group_min": 14,
    "min_age": "18",
    "pick_up": true,
    "price": 2500.0,
    "title": "SUPER JEEP NORTHERN LIGHTS HUNT - FREE PHOTOS INCLUDED"
}' http://127.0.0.1:5000/api/v1/hikes/1

```

### Get trips by User id

```http
GET /api/v1/users/<auth0_user_id>/trips
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `auth0_user_id`      | `string` | **Required**. id of the user |

Example
```http
$ curl http://127.0.0.1:5000/api/v1/users/github|34656913/trips
```
Results (json)

```http
{
    "hikes": [
        {
            "available": true,
            "departs_from": "Oran",
            "description": "On this super jeep excursion, we take you off the beaten track and chase one of the world's most mysterious phenomena. Leave the city's bright lights behind to see the Northern Lights while your guide tells you about this natural wonder!",
            "difficulty": "Hard",
            "duration": "5 Hours",
            "group_max": 20,
            "group_min": 10,
            "id": 1,
            "min_age": "18",
            "pick_up": true,
            "price": 1500.0,
            "title": "SUPER JEEP NORTHERN LIGHTS HUNT - FREE PHOTOS INCLUDED"
        }
    ],
    "success": true
}
```

### Get all trips

```http
GET /api/v1/trips
```
Example
```http
$ curl http://127.0.0.1:5000/api/v1/trips
```
Results (json)

```http
{
    "trip": {
        "auth0_user_id": "github|34656913",
        "booking_date": "Sat, 04 Mar 2023 18:40:19 GMT",
        "hike_id": 1,
        "id": 1,
        "status": "ordered",
        "user_id": null
    }
}
```

### Create a Trip

```http
POST /api/v1/trips
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `hike_id`       | `int`  | **Required**. Hike id |
| `auth0_user_id` | `string`  | **Required**. User id |


Example

```http
$ curl -X POST  -H "Content-Type: application/json" -d
 '{
    "hike_id": 1,
    "auth0_user_id": "github|34656913"
}' http://127.0.0.1:5000/api/v1/trips

```


### Get trips by user

```http
GET /api/v1/users/<user_id>/trips
```
Example
```http
$ curl http://127.0.0.1:5000/api/v1/users/github|34656913/trips
```
Results (json)

```http
{
    "trips": [
        {
            "auth0_user_id": "github|34656913",
            "booking_date": "Sat, 04 Mar 2023 20:19:40 GMT",
            "hike_id": 1,
            "id": 1,
            "status": "ordered",
            "user_id": null
        },
        {
            "auth0_user_id": "github|34656913",
            "booking_date": "Sat, 04 Mar 2023 20:19:43 GMT",
            "hike_id": 1,
            "id": 2,
            "status": "ordered",
            "user_id": null
        }
    ]
}
```

### Delete a trip

```http
DELETE /api/v1/users/<user_id>/trips/<trip_id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `user_id`      | `string` | **Required**. id of user |
| `trip_id`      | `int` | **Required**. id of trip to delete |

Example
```http
$ curl -X DELETE http://127.0.0.1:5000/api/v1/users/github|34656913/trips/1 
```

## Response Codes
We use standard HTTP codes to denote successful execution or indicate when errors occur. For some errors, the response will include
additional information about the error, including an application error
code and human readable error description.

### On successful execution

| Operation | HTTP Response Code | Response body                       |
| :-------- | :------- | :-------------------------------- |
| `GET`      | `200` | The requested data (order, document, etc) as JSON |
| `POST`     | `201` | Sucess message as JSON |

### Error Handling

| Error Condition | HTTP Response Code | Response body|
| :-------- | :------- | :-------------------------------- |
| `If the submitted data was invalid or the request was bad.` | `400` | Error entity, in JSON |
| `The user/client was not authorised` | `401` | Error entity, in JSON  |
| `If the resource requested is not found`  | `404` | Error entity, in JSON  |
| `Unprocessable Entity`| `422` | Error entity, in JSON  |

## Authors

- [@AbdessamadB](https://github.com/BOUMESLOUTAbdessamad)


## License

[MIT](https://choosealicense.com/licenses/mit/)

