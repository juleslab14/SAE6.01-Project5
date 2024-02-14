#test d'un script python
import yaml
from jinja2 import Template
from pprint import pprint as p

#lire le fichier yaml
with open("exemple.yml") as file:
    info_router = yaml.safe_load(file)

#lire la template jinja
with open("exemple.j2") as file:
    template = Template(file.read())


#p(info_router)
