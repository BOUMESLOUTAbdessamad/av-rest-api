# This example sets up an endpoint using the Flask framework.
# Watch this video to get started: https://youtu.be/7Ul1vfmsDck.
import stripe
from flask import jsonify
from config import app


@app.route('/payment-sheet', methods=['POST'])
def payment_sheet():

    # Set your secret key. Remember to switch to your live secret key in production.
    # See your keys here: https://dashboard.stripe.com/apikeys
    stripe.api_key = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'

    # Use an existing Customer ID if this is a returning customer
    customer = stripe.Customer.create()
    ephemeralKey = stripe.EphemeralKey.create(
    customer=customer['id'],
    stripe_version='2023-10-16',
    )
    paymentIntent = stripe.PaymentIntent.create(
    amount=1099,
    currency='eur',
    customer=customer['id'],
    # In the latest version of the API, specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default.
    automatic_payment_methods={
        'enabled': True,
    },
    )
    return jsonify(paymentIntent=paymentIntent.client_secret,
                    ephemeralKey=ephemeralKey.secret,
                    customer=customer.id,
                    publishableKey='pk_test_TYooMQauvdEDq54NiTphI7jx')