#################
# builder image #
#################

FROM debian:stretch-slim AS builder
MAINTAINER info@nextdom.com

WORKDIR /tmp
COPY ./install/dependencies/ ./

# install build dependencies
RUN apt-get update  -y && \
     apt-get install -y --no-install-recommends \
      wget curl gnupg apt-transport-https php-cli ca-certificates php-curl git \
      php-dom php-mbstring php-zip && \
      ./ensure-npm \
      ./ensure-yarn \
      ./ensure-composer \
      ./ensure-saas \
      ./ensure-minify \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* && \
    rm -f /tmp/ensure-*

# preprare nextdom root directory
# - genereate assets (vendor / js / css)
# - clean directory
WORKDIR /usr/share/nextdom
COPY / ./
RUN bash ./scripts/gen_composer_npm.sh && \
    bash ./scripts/gen_assets.sh && \
    npm cache rm --force && \
    composer clearcache && \
    rm -rf \
      .coveralls.yml .dockerignore .github .gitignore .sass-cache \
      .travis.yml composer.json composer.lock package.json phpunit.xml.dist \
      yarn.lock var

###############
# final image #
###############
FROM debian:stretch-slim
STOPSIGNAL SIGRTMIN+3
VOLUME /var/lib/nextdom
VOLUME /var/log/nextdom
EXPOSE 80
EXPOSE 443

# install run dependencies
RUN echo "127.0.1.1 $HOSTNAME" >> /etc/hosts && \
    apt-get update  -y && \
    apt-get install -y --no-install-recommends \
      software-properties-common && \
    add-apt-repository non-free && \
    apt-get install -y --no-install-recommends \
      apache2 apache2-utils apt-transport-https ca-certificates coreutils \
      cron curl cutycapt dos2unix g++ gcc git gnupg grep htop iftop iotop \
      libapache2-mod-php libexpat1 libexpat1 locate make ntp \
      ntpdate php php-common php-curl php-gd php-imap php-json php-mbstring \
      php-mcrypt php-mysql php-opcache php-soap php-ssh2 php-xml php-xmlrpc \
      php-zip python python-pip sed  smbclient software-properties-common \
      ssl-cert sudo systemd systemd-sysv tar telnet unzip vim  wget xvfb \
      mysql-client && \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# copy nextdom root from builder image
WORKDIR /usr/share/nextdom
COPY --from=builder /usr/share/nextdom ./

# register nextdom service, that runs postint on first run
COPY tests/docker/conf/systemd/nextdom.service  /usr/share/nextdom/systemd/
COPY tests/docker/conf/systemd/nextdom          /usr/share/nextdom/systemd/
RUN systemctl enable /usr/share/nextdom/systemd/nextdom.service

CMD ["/sbin/init"]
