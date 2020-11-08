import string, random, os
from datetime import datetime

def rand_gen(size=100):
    current_time = datetime.now()
    current_time = current_time.strftime("%Y%m%d%H%M%S")
    chars = string.ascii_uppercase + string.digits
    return current_time+("".join(random.choice(chars) for x in range(size)))

def path_and_rename(instance, filename):
    upload_to = 'accounts/'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(rand_gen(), ext)
    return os.path.join(upload_to, filename)