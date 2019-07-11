# Django Api Calendar

Django Api Calendar is a Django Iteration of FullCalendar, coupled with a Rest API written with the Django Rest Framework. The calendar uses GET Requests to get events, and POST to create new events. 

## Installation

Strongly recommend using a python3 virtual environment to run this:

```python
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Usage

### Web UI
 ![alt text](https://github.com/hfeixas/DjangoApiCalendar/blob/master/images/FullCalendar.png)

### API

To Get Events make a GET Request to http://127.0.0.1/caldendar/api
```python
    {
        "title": "Event Number 1",
        "start": "2019-06-27T18:00:00Z",
        "end": "2019-06-27T19:00:00Z",
        "allDay": false
    },
    {
        "title": "Event Number 2",
        "start": "2019-06-27T19:00:00Z",
        "end": "2019-06-27T20:00:00Z",
        "allDay": false
    },
```
To Create Event Make a POST request to http://127.0.0.1/caldendar/api

```python
    {
        "title": "Test Event",
        "start": "2019-06-27T18:00:00Z",
        "end": "2019-06-27T19:00:00Z",
        "allDay": true
    },
```

## Contributing
Pull requests are welcome. Free to use, change, and distribute.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
