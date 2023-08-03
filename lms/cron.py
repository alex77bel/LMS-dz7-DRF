import stripe
from stripe.error import InvalidRequestError

from config import settings
from lms.models import Payment


def my_scheduled_job():
    stripe.api_key = settings.STRIPE_API_KEY
    for payment in Payment.objects.all():
        try:
            get_status = stripe.PaymentIntent.retrieve(payment.payment_id, )
        except InvalidRequestError as err:
            print(err)
        else:
            status = get_status.get('status')
            if get_status:
                payment.payment_status = status
                payment.save()
