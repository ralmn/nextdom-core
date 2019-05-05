# docker-nextdom-core-dev

Image permettant le développement de Nextdom

# Utilisation

Lancer le container:
```bash
sudo docker run -d --name=nextdom --privileged=true -p 8080:80 -v $(pwd)/nextdom-core/:/usr/share/nextdom  nextdom/nextdom-core-dev
```

# Fonctionnalités optionnelles

## Server samba

Installe et configure un server samba pour les testes de sauvegarde.
* utilisateur: nextdom
* mot de passe: nextdom
* ip: localhost
* chemin sur le système de fichier: /var/backups

Pour construire l'image docker avec cette fonctionnalité:
```
cd ./tests/docker/nextdom-dev/
docker build --build-arg with_samba=1 -t nextdom/nextdom-core:dev .
```

<!-- Local Variables: -->
<!-- ispell-local-dictionary: "francais" -->
<!-- End: -->
