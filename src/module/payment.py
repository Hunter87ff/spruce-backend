import random
import config
import string
from cashfree_pg.models.create_order_request import CreateOrderRequest
from cashfree_pg.api_client import Cashfree
from cashfree_pg.models.customer_details import CustomerDetails
from cashfree_pg.models.order_meta import OrderMeta

Cashfree.XClientId = config.XCLIENT_ID
Cashfree.XClientSecret = config.XCLIENT_SECRET
Cashfree.XEnvironment = Cashfree.PRODUCTION
x_api_version = "2023-08-01"

def create_token(range:int=16):
    return ''.join(random.choices(
        string.ascii_letters + string.digits, 
        k=range
    ))



def create_order(
        customer_id:str=create_token(), 
        customer_ph:str="8474090589", 
        order_id:str=create_token(), 
        amount:int=1, currency:str="INR"):
    customerDetails = CustomerDetails(customer_id=customer_id, customer_phone=customer_ph)

    createOrderRequest = CreateOrderRequest(
        order_id=order_id, 
        order_amount=amount, 
        order_currency=currency, 
        customer_details=customerDetails
    )
    orderMeta = OrderMeta()
    orderMeta.return_url = f"https://{config.DOMAIN}/payment_checkout"
    orderMeta.notify_url = f"https://{config.DOMAIN}/api/webhook"
    createOrderRequest.order_meta = orderMeta
    try:
        api_response = Cashfree().PGCreateOrder(x_api_version, createOrderRequest, None, None)
        return dict(api_response.data)

    except Exception as e:
        print(e)
        return None

