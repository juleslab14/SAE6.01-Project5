# Automatisation de déploiement réseau

## Arborescence du dépôt Github

Le dossier *Recherches* comprend toutes les recherches que nous avons effectuées dans le cadre du projet sur Ansible, EVE-NG, GNS3 et ZTP. On peut retrouver l'étude d'art sur EVE-NG et GNS3, ainsi que ce qui nous a fait choisir GNS3 plutôt que EVE-NG et des détails de la maquette. On retrouve également les recherches effectuées sur les différents modules d'Ansible, qui sont utilisés ou non dans les différents playbooks, et la recherche documentaire sur le provisionnement de routeur Cisco CSR1000v avec ZTP.

Le dossier *scripts* quant à lui contient les différents fichiers et playbooks que nous avons utilisé pour configurer la maquette avec Ansible. Le sous-dossier *inventory* contient quant à lui tous les hôtes avec leurs variables dans des fichiers yaml ainsi que les groupes avec les variables communes pour chaque routeur.

```bash
|-- Recherches                  #Recherches documentaires liées au projet
|       -- ansible
|       -- EVE-NG vs GNS3
|       -- ztp
|-- scripts                     #playbook et les fichiers de variables/conf utilisés dans le projet
|       -- ansible
           config.cfg
           ansibles.cfg
           bgp.yml
           bgp_CE.yml
|           -- inventory
               hosts.ini
|             -- group_vars
                 all.yml
|             -- host_vars
                 PE2.yml
                 PE1.yml
                 etc
```

## Prérequis pour le projet

Dans le scénario de notre projet, nous avons un schéma gns3 avec des routeurs CSR1000v avec une configuration ospf opérationnel, des interfaces up et l’accès SSH sur les routeurs afin qu’ansible puisse mettre en place la configuration bgp et les vrf. Nous avons également besoin d’une machine avec ansible dessus pour exécuter les playbook, dans notre scénario, nous avons utilisé l’appliance GNS3 “Network Automation”, il s’agit d’une VM avec ansible installée dessus.

## Lancement du playbook Ansible

Vous devez exécuter les commandes suivantes dans la machine "Network Automation" et dans le répertoire ansible/.

```bash
ansible-playbook bgp.yml #configuration bgp et des vrfS
```

Le playbook permet la configuration bgp sur les routeurs PE et la création des vrf sur les routeurs (les routeurs R et PE (je crois))

message de  Monsieur Brisacier: 
avec les pré-requis, comment utiliser le projet
axes d'amélioration
```