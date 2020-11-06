from datetime import datetime
import string
import random

def random_protocol_generate(size=6):
    current_time = datetime.now()
    year = current_time.strftime("%Y")
    chars = string.ascii_uppercase + string.digits
    return year+("".join(random.choice(chars) for x in range(size)))

def path_and_rename(instance, filename):
    upload_to = 'uploads'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)
    