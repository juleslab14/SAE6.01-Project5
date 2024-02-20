#Lancement du playbook Ansible
Vous devez exécuter les commandes suivantes dans la machine "Network Automation"

```bash
ansible-playbook config.yml -u admin -k
```
Le playbook permet (normalement) la configuration bgp d'un routeur en utilisant une template Jinja2