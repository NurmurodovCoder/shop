import http.client
import random
from django.core.cache import cache

"""
 * Send an sms message by using Infobip API.
 *
 * This example is already pre-populated with your account data:
 * 1. Your account Base URL
 * 2. Your account API key
 * 3. Your recipient phone number
 *
 * THIS CODE EXAMPLE IS READY BY DEFAULT. HIT RUN TO SEND THE MESSAGE!
 *
 * Send sms API reference: https://www.infobip.com/docs/api#channels/sms/send-sms-message
 * See Readme file for details.
"""


def send_sms(phone_number):
    
    code = random.randint(1000, 9999)

    BASE_URL = "xld4lg.api.infobip.com"
    API_KEY = "App c32bd4415e46ad17d806ab4139b59743-122229f6-2bd5-46cb-bca6-1feb50402883"

    SENDER = "NR-tech"
    RECIPIENT = str(phone_number)
    MESSAGE_TEXT = f"Sizning SMS codeing -- { code }"

    conn = http.client.HTTPSConnection(BASE_URL)

    payload1 = "{\"messages\":" \
            "[{\"from\":\"" + SENDER + "\"" \
            ",\"destinations\":" \
            "[{\"to\":\"" + RECIPIENT + "\"}]," \
            "\"text\":\"" + MESSAGE_TEXT + "\"}]}"

    headers = {
        'Authorization': API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    cache.set(phone_number, code, 300)
    print(cache.get(phone_number),'---====')
    return conn.request("POST", "/sms/2/text/advanced", payload1, headers)

    # res = conn.getresponse()
    # data = res.read()

    

# print(data.decode("utf-8"))
