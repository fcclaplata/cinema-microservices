from project.repo import booking_repo
from bson.json_util import dumps
from apistar import http, schema
import requests
from os import environ

PAYMENTSERVICE = environ.get('PAYMENTSERVICE')
NOTIFICATIONSERVICE = environ.get('NOTIFICATIONSERVICE')

class Booking(schema.Object):
    properties = {
        'city': schema.String,
        'schedule': schema.String,
        'movie': schema.String,
        'cinemaRoom': schema.Integer,
        'seats': schema.String,
        'totalAmount': schema.Number
    }

class Ticket(schema.Object):
    properties = {
        'cinema': schema.String,
        'schedule': schema.String,
        'movie': schema.String,
        'seat': schema.String,
        'cinemaRoom': schema.Integer,
        'orderId': schema.Integer
    }

class User(schema.Object):
    properties = {
        'name': schema.String,
        'lastName': schema.String,
        'email': schema.String,
        'phoneNumber': schema.String,
        'creditCard': schema.String,
        'membership': schema.Number
    }

def booking(user: User, booking: Booking):
    payment = {
        "userName": user["name"] + ' ' + user["lastName"],
        "currency": 'mxn',
        "number": user["creditCard"]["number"],
        "cvc": user["creditCard"]["cvc"],
        "exp_month": user["creditCard"]["exp_month"],
        "exp_year": user["creditCard"]["exp_year"],
        "amount": booking["amount"],
        "description": "Tickect(s) for movie " + booking["movie"] + " ,with seat(s)" + str(booking["seats"]) + " at time " + booking["schedule"]
    }

    # TODO: post request to pyment service
    #
    # payment_response = requests.post(PAYMENTSERVICE, data=payment)
    #

    # mock paid
    paid = {
        "id": "123"
    }

    booking = booking_repo.make_booking(user, booking)
    ticket = booking_repo.generate_ticket(paid, booking)

    # TODO: post request to notification service
    #
    # notification_response = requests.post(NOTIFICATIONSERVICE, data={bookin, ticket})
    #

    return {'data': dumps(ticket)}

def verify_booking(orderId: str):
    return {'data': dumps(booking_repo.get_order_by_id(orderId))}
