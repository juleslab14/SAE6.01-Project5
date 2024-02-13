# Utilisation des routeurs Cisco 7200 avec GNS3 et ZTP

## Introduction
Dans ce guide, nous allons explorer comment utiliser les routeurs Cisco 7200 avec GNS3 et Zero Touch Provisioning (ZTP) pour configurer automatiquement les routeurs connectés au client sur le backbone d'un opérateur.

## Prérequis
Avant de commencer, assurez-vous d'avoir les éléments suivants :
- GNS3 installé sur votre machine
- Images du routeur Cisco 7200 pour GNS3
- Une compréhension de base des concepts de réseau et de la configuration des routeurs Cisco.

## Configuration de GNS3
1. Installez GNS3 sur votre machine en suivant la documentation officielle.
2. Téléchargez les images des routeurs Cisco 7200 compatibles avec GNS3.
3. Importez les images du routeur dans GNS3.
4. Configurez les interfaces réseau et les connexions nécessaires dans GNS3 pour simuler la topologie réseau souhaitée.

## Configuration de ZTP
1. Activez ZTP sur les routeurs Cisco 7200 en configurant les paramètres nécessaires dans la configuration du routeur.
2. Configurez un serveur ZTP sur votre réseau pour fournir les fichiers de configuration aux routeurs.
3. Créez les fichiers de configuration pour chaque routeur, en spécifiant les paramètres de configuration souhaités.
4. Configurez le serveur DHCP sur le serveur ZTP pour qu'il fournisse des adresses IP aux routeurs et spécifiez l'adresse IP du serveur ZTP en tant qu'option du serveur suivant.
5. Connectez les routeurs au réseau et mettez-les sous tension.

## Vérification de la configuration ZTP
1. Surveillez les journaux du serveur ZTP pour vous assurer que les routeurs demandent des fichiers de configuration.
2. Vérifiez que les routeurs reçoivent les fichiers de configuration et appliquent les configurations automatiquement.
3. Tester la connectivité entre les routeurs et le client sur le backbone de l'opérateur pour s'assurer de la réussite de la configuration.

## Conclusion
En utilisant les routeurs Cisco 7200 avec GNS3 et ZTP, vous pouvez automatiser le processus de configuration des routeurs connectés au client sur le backbone de l'opérateur. Cela facilite le déploiement et la gestion de l'infrastructure réseau.
