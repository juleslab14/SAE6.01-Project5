#test d'un script python
import yaml
from jinja2 import Template
#from pprint import pprint as p

#lire le fichier yaml
with open("exemple.yml") as file:
    info_router = yaml.safe_load(file)

#lire la template jinja
with open("exemple.j2") as file:
    template = Template(file.read())

#utilisation de jinja
for info in info_router["devices"]:
    print(template.render(device=info["name"],interfaces=info["interfaces"],bgpasn=info["bgpasn"],bgp_neighbors=info["bgp_neighbors"]))


#p(info_router)
