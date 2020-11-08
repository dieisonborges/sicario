from datetime import datetime
import string, random, os

def rand_gen(size=100):
    current_time = datetime.now()
    current_time = current_time.strftime("%Y%m%d%H%M%S")
    chars = string.ascii_uppercase + string.digits
    return current_time+("".join(random.choice(chars) for x in range(size)))

def path_and_rename(instance, filename):
    upload_to = 'tickets/'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(rand_gen(), ext)
    return os.path.join(upload_to, filename)


def random_protocol_generate(size=6):
    current_time = datetime.now()
    year = current_time.strftime("%Y")
    chars = string.ascii_uppercase + string.digits
    return year+("".join(random.choice(chars) for x in range(size)))

"""
def path_and_rename(instance, filename):
    upload_to = 'tickets'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)
"""