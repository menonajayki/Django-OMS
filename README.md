To initiate the application run this:

```python manage.py runserver```

The application components and flow are as follows:

    +-----------------------------------+
    |           Django Project           |
    +-----------------------------------+
                  |
                  v
    +-------------------------------+
    |         settings.py            |
    |  - Configure Django Settings   |
    +-------------------------------+
                  |
                  v
    +-------------------------------+
    |           urls.py              |
    |  - Define Project URL Patterns |
    +-------------------------------+
                  |
                  v
    +-------------------------------+
    |          wsgi.py               |
    |  - WSGI Configuration for      |
    |    Production Servers          |
    +-------------------------------+
                  |
                  v
    +-------------------------------+
    |          asgi.py               |
    |  - ASGI Configuration for      |
    |    Channels and Websockets     |
    +-------------------------------+
                  |
                  v
    +-------------------------------+
    |           orders               |
    |  - Django App for Managing     |
    |    Orders and Transactions     |
    +-------------------------------+
        |         |         |
        v         v         v
    +-------------------------------+
    |          models.py             |
    |  - Define Order and Product    |
    |    Database Models             |
    +-------------------------------+
        |         |
        v         v
    +-------------------------------+
    |          views.py              |
    |  - Views for Order Processing, |
    |    Cart Management, Checkout,  |
    |    and Order History           |
    +-------------------------------+
        |         |
        v         v
    +-------------------------------+
    |          urls.py               |
    |  - URL Routing for Orders App  |
    +-------------------------------+
        |         |
        v         v
    +-------------------------------+
    |          admin.py              |
    |  - Admin Panel Registration    |
    |    for Order Management        |
    +-------------------------------+
        |         |
        v         v
    +-------------------------------+
    |          forms.py              |
    |  - Forms for Order Creation,   |
    |    Payment Information,        |
    |    and Shipping Details        |
    +-------------------------------+
        |         |
        v         v
    +-------------------------------+
    |       consumers.py             |
    |  - Websocket Consumers for     |
    |    Real-Time Order Tracking    |
    +-------------------------------+
