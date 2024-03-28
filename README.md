# STEPS TO FOLLOW FOR RUNNING  THE APPLICATION:

Install Requirements:

```pip install -r requirements.txt```

Migrate Database:

```python manage.py migrate```

Create a superuser:

```python manage.py createsuperuser```

To initiate the application run this:

```python manage.py runserver```


# COMPONENTS:

The application components and flow are as follows:

    +-----------------------------------+
    |           Django Project          |
    +-----------------------------------+
                  |
                  v
    +-------------------------------+
    |         settings.py           |
    |  - Configure Django Settings  |
    +-------------------------------+
                  |
                  v
    +-------------------------------+
    |           urls.py             |
    | - Define Project URL Patterns |
    +-------------------------------+
                  |
                  v
    +-------------------------------+
    |          wsgi.py              |
    |  - WSGI Configuration for     |
    |    Production Servers         |
    +-------------------------------+
                  |
                  v
    +-------------------------------+
    |          asgi.py              |
    |  - ASGI Configuration for     |
    |    Channels and Websockets    |
    +-------------------------------+
                  |
                  v
    +-------------------------------+
    |           orders              |
    |  - Django App for Managing    |
    |    Orders and Transactions    |
    +-------------------------------+
                  |         
                  v         
    +-------------------------------+
    |          models.py            |
    |  - Define Order and Product   |
    |    Database Models            |
    +-------------------------------+
                  |
                  v
    +-------------------------------+
    |          views.py             |
    | - Views for Order Processing, |
    |    Cart Management, Checkout, |
    |    and Order History          |
    +-------------------------------+
                  |
                  v
    +-------------------------------+
    |          urls.py              |
    | - URL Routing for Orders App  |
    +-------------------------------+
                 |
                 v
    +-------------------------------+
    |          admin.py             |
    |  - Admin Panel Registration   |
    |    for Order Management       |
    +-------------------------------+
                 |
                 v
    +-------------------------------+
    |          forms.py             |
    |  - Forms for Order Creation,  |
    |    Payment Information,       |
    |    and Shipping Details       |
    +-------------------------------+
                 |
                 v
    +-------------------------------+
    |       consumers.py            |
    |  - Websocket Consumers for    |
    |    Real-Time Order Tracking   |
    +-------------------------------+
