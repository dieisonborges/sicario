from datetime import datetime
import string
import random

def random_protocol_generate(size=6):
    current_time = datetime.now()
    year = current_time.strftime("%Y")
    chars = string.ascii_uppercase + string.digits
    return year+("".join(random.choice(chars) for x in range(size)))
    