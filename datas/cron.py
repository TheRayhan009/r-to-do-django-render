from .models import cronProxy
import random

def numm():
    x=random.randint(1,100)
    data = cronProxy(
        rendom_num=x,
    )
    data.save()