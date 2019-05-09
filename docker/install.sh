#!/bin/bash

which docker-compose >/dev/null 2>&1 || {
  echo "docker-compose is not installed, need sudo password to install it"
  echo -n "password: "
  read -s password
  echo ""
  echo "${password}" | sudo -S curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  echo "${password}" | sudo -S chmod +x /usr/local/bin/docker-compose
}

target="nextdom/docker-compose.yml"

mkdir nextdom
curl -sSL https://raw.githubusercontent.com/NextDom/nextdom-core/optim-assets/docker/nextdom/docker-compose.yml -o ${target}

echo -n "choose mysql root password: "
read -s mysql_root_password
echo ""

echo -n "choose mysql nextdom password: "
read -s nextdom_root_password
echo ""

cat - > nextdom/.env <<EOS
MYSQL_ROOT_PASSWORD=${mysql_root_password}
MYSQL_ROOT_PASSWORD=${nextdom_root_password}
EOS

cat - <<EOS
-> mysql passwords are stored in file $(pwd)/nextdom/.env
-> this file is necessary to start nextdom

you can now run the following commands:
  - run nextdom containers                               => docker-compose -f $(pwd)/${target} up -d
  - stop nextdom containers                              => docker-compose -f $(pwd)/${target} stop
  - start nextdom containers again                       => docker-compose -f $(pwd)/${target} start
  - completly remove nextdom and its data (DATA LOSS !!) => docker-compose -f $(pwd)/${target} down
EOS
