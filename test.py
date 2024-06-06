import instalic
from instalic.utils import random_useragent

TARGET = 'aihkw'

x = instalic.Client()
print(random_useragent())
# print(vars(x.get_id_from_username(TARGET)))