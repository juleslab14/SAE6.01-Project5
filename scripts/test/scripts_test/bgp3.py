import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
from ansible.module_utils.basic import AnsibleModule

def render_template(template_path, yaml_data):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_path)
    render_config = template.render(bgp_config=yaml_data)
    return render_config

def configure_bgp(yaml_data, jinja2_template, device):
    render_config = render_template(jinja2_template, yaml_data)
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        ssh.send_config_set(render_config)

if __name__ == '__main__':
    module_args = dict(
        yaml_file=dict(type='str', required=True),
        jinja2_template=dict(type='str', required=True),
        host=dict(type='str', required=True),
        username=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        secret=dict(type='str', required=True, no_log=True),
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    yaml_file = module.params['yaml_file']
    jinja2_template = module.params['jinja2_template']
    host = module.params['192.168.100.254']
    username = module.params['admin']
    password = module.params['admin']
    secret = module.params['admin']

    device = {
        'device_type': 'cisco_ios',
        'host': '192.168.100.254',
        'username': 'admin',
        'password': 'admin',
        'secret': 'admin',
    }

    try:
        with open(yaml_file, 'r') as f:
            yaml_data = yaml.safe_load(f)
        configure_bgp(yaml_data, jinja2_template, device)
        module.exit_json(changed=True, msg="BGP configuration applied successfully.")
    except Exception as e:
        module.fail_json(msg="Failed to apply BGP configuration: {}".format(str(e)))
