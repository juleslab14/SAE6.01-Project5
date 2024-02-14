# Liste des modules disponibles sur Ansible Galaxy qui peuvent être utiles pour le projet

## Il s'agit de modules provenant de la collection cisco.ios, qui a été testée intégralement sur la version 17.3 d'IOS XE dans Cisco Moduling Labs (CML)

La collection a été testée avec les versions >= 2.14.0 d'Ansible. Chacun des modules contient dans sa page de documentation des exemples d'utilisation du module dans la catégorie "Notes", et notamment l'effet des commandes envoyées sur la configuration.
source de la collection : <https://galaxy.ansible.com/ui/repo/published/cisco/ios/>

- ios_bgp_address_family: module permettant de configurer et de gérer les attributs des familles d'adresses BGP. Testé sur la version IOS-XE 17.3
lien : <https://galaxy.ansible.com/ui/repo/published/cisco/ios/content/module/ios_bgp_address_family/>

- ios_ospf_interfaces: module permettant de configurer et de gérer les interfaces OSPF (OSPFv2). Testé sur la version IOS-XE 17.3
lien : <https://galaxy.ansible.com/ui/repo/published/cisco/ios/content/module/ios_ospf_interfaces/>

- ios_ospfv2 : module permettant de configurer et gérer OSPF (OSPFv2). Testé sur la version IOS-XE 17.3
lien : <https://galaxy.ansible.com/ui/repo/published/cisco/ios/content/module/ios_ospfv2>

- ios_ospfv3 : module pour configurer OSPF v3. Testé sur la version IOS-XE 17.3
lien : <https://galaxy.ansible.com/ui/repo/published/cisco/ios/content/module/ios_ospfv3/>

- ios_vrf : module pour configurer les VRF
lien : <https://galaxy.ansible.com/ui/repo/published/cisco/ios/content/module/ios_vrf/>

- ios_interfaces : module permettant de configurer les interfaces sur les IOS
lien ; <https://galaxy.ansible.com/ui/repo/published/cisco/ios/content/module/ios_interfaces/>

Liens utiles :

- <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>
Ce lien détaille comment utiliser le mode Enable sur les IOS dans Ansible.

- <https://docs.ansible.com/ansible/latest/collections_guide/index.html>

- <https://github.com/ipspace/MPLS-infrastructure> : playbook trouvé sur Github permettant de déployer des configurations OSPF/IBGP/EBGP et MPLS/VPN sur des IOS.
/!\ Le dépôt n'a pas eu de changement depuis 6ans mais je pense que ça peut donner des exemples.
