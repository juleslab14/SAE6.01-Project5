## Comparaison entre les deux :

<https://medium.com/@williamaddox_80973/eve-ng-vs-gns3-a-comparative-study-of-two-leading-network-simulators-535ece13b696#:~:text=GNS3%20is%20known%20to%20be,scale%20and%20complex%20simulations%20effectively>.
<https://letmetechyou.com/eve-ng-vs-gns3-complete-2022-review/>
<https://gns3.com/why-should-i-use-gns3-over-eve-n>
<https://www.reddit.com/r/networking/comments/hu7bdd/gns3_vs_eveng/?rdt=39956>

## En bref :

### EVE-NG :

* +. Prend en charge plus de constructeurs et résite mieux au gros réseaux
* -. Demande beaucoup de bon matériel pour bien fonctionner
* +. Intègre tout les besoins réseau pour le projet
* -. Accès en WEB seulement pour les labs, une connexion possible à la fois, empêchant plusieurs personne à travailler en simultané
* +. ISO déja faite pour des serveurs proxmox

### GNS3 :

* +. Répond à nos besoins de config réseau
* +. On sait déja intégrer une VM dans un schéma
* -. Propose moins de multimarques (principalement Cisco), mais pas dérangeant pour notre projet
* +. Plus stable que EVE-NG en règle générale (Problème rencontré lors de la SAE501)
* +. Script d'installation proposé par GNS3 pour télécharger sur une machine ubuntu serveur

Choix final : VM Ubuntu serveur (install plus facile, par script) avec l'ip 192.168.222.252 faisant tourner une instance GNS3 sur le proxmox PVE8 (192.168.222.248) de la salle Oresme (3258), permettant à tout le monde de travailler sur la même session sans problème

### Pour integrer une VM dans le lab :

## Le lab

La lab est composé de 5 routeurs cisco 7200 ainsi que deux VM, une pour l'automatisation avec ansible et une autre pour faire des tests sur le ZTP, cela nous permet de simuler un petit backbone operateur compoosé ainsi : ![Schéma](https://github.com/juleslab14/SAE6.01-Project5/blob/main/schema_v5.2.png)

