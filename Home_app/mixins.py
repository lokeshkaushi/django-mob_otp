# from django.conf import settings
from twilio.rest import Client 

def send_otp_on_phone(mobile,otp):
    client = Client('AC582f5de804d8c9f01690908de074b5ea','6cd9c8d6270fe0daeeca045350619ecb')
    message = client.messages \
                    .create(
                        body=f'Your otp is {otp}',
                        #from_='+1949 998 5801',
                        from_='+1799 622 7784',
                        to=mobile
                    )
    print('otp send to')