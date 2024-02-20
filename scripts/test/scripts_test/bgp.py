import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler

def render_template_jinja(template_path, yaml_data):
    #Chargement de la template Jinja2
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_path)
    #Mise en place de la configuration avec les données du fichier yaml
    render_config = template.render(bgp_config=yaml_data)
    return render_config

def apply_config(device, config):
    #Connection au routeur en SSH
    with ConnectHandler(**device) as ssh:
        #envoie des commandes pour la configuration
        ssh.send_config_set(config)

def configure_bgp(yaml_file, jinja2_template, device):
    #chargement des données du fichier yaml
    with open(yaml_file, 'r') as f:
        bgp_data = yaml.safe_load(f)
    #rendu de la template jinja2
    render_config = render_template_jinja(jinja2_template, bgp_data['bgp_config'])
    #mise en place de la configuration
    apply_config(device, render_config)

if __name__ == '__main__':
    #paramètres des routeurs
    device = {
        'device_type': 'cisco_ios',
        'host': 'R3',
        'username': 'admin',
        'password': 'admin',
        'secret': 'admin',
    }

    #chemin des fichiers
    yaml_file = './bgp_config.yml'
    jinja2_template = './bgp_template.j2'

    #mise en place de conf sur les routeurs
    configure_bgp(yaml_file, jinja2_template, device)