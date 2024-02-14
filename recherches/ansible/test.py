#test d'un script python
import yaml
from pprint import pprint as p

with open("exemple.yml") as file:
    info_router = yaml.safe_load(file)

p(info_router)
