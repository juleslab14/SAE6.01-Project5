# Automatisation de déploiement réseau

## Arborescence du dépôt Github

Le dossier *Recherches* comprend toutes les recherches que nous avons effectuées dans le cadre du projet sur Ansible, EVE-NG, GNS3 et ZTP. On peut retrouver l'étude d'art sur EVE-NG et GNS3, ainsi que ce qui nous a fait choisir GNS3 plutôt que EVE-NG et des détails de la maquette. On retrouve également les recherches effectuées sur les différents modules d'Ansible, qui sont utilisés ou non dans les différents playbooks, et la recherche documentaire sur le provisionnement de router Cisco 7200 avec ZTP.

Le dossier *scripts* quant à lui contient les différents fichiers et playbooks que nous avons utilisé pour configurer la maquette avec Ansible. Le sous-dossier *inventory* contient quant à lui tous les hôtes et leurs variables ainsi que les groupes et leurs variables.

```bash
|-- Recherches                  #Recherches documentaires liées au projet
|       -- ansible
|       -- EVE-NG vs GNS3
|       -- ztp
|-- scripts                     #Scripts et playbooks utilisés dans le projet
|       -- wallah (à renommer)
|           -- inventory
```

## Prérequis pour le projet

Lorem Ipsum Dolor sit amet

## Lancement du playbook Ansible

Vous devez exécuter les commandes suivantes dans la machine "Network Automation".

```bash
ansible-playbook config.yml -u admin -k
```

Le playbook permet (normalement) la configuration bgp d'un routeur en utilisant une template Jinja2.
