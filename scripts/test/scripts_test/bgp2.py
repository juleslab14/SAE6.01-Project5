import yaml
from jinja2 import Environment, FileSystemLoader
import paramiko
from ansible.module_utils.basic import AnsibleModule

def render_template_jinja(template_path, yaml_data):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_path)
    rendered_config = template.render(bgp_config=yaml_data)
    return rendered_config

def apply_config(device, config):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=device['R3'], 
                username=device['admin'], 
                password=device['admin'],
                secret=device['admin'])

    ssh_shell = ssh.invoke_shell()
    ssh_shell.send("conf t\n")
    ssh_shell.send(config)
    ssh_shell.send("end\n")
    ssh.close()

def configure_bgp(yaml_file, jinja2_template, device):
    with open(yaml_file, 'r') as f:
        bgp_data = yaml.safe_load(f)
    render_config = render_template_jinja(jinja2_template, bgp_data['bgp_config'])
    apply_config(device, render_config)

if __name__ == '__main__':
    module_args = dict(
        yaml_file=dict(type='str', required=True),
        jinja2_template=dict(type='str', required=True),
        host=dict(type='str', required=True),
        username=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        secret=dict(type='str',required=True, no_log=True)
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    yaml_file = module.params['bgp_config']
    jinja2_template = module.params['bgp_template']
    host = module.params['R3']
    username = module.params['admin']
    password = module.params['admin']
    secret= module.params['admin']

    device = {
        'R3': host,
        'admin': username,
        'admin': password,
        'admin': secret,
    }

    try:
        configure_bgp(yaml_file, jinja2_template, device)
        module.exit_json(changed=True, msg="BGP configuration applied successfully.")
    except Exception as e:
        module.fail_json(msg="Failed to apply BGP configuration: {}".format(str(e)))
