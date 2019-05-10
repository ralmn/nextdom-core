FROM debian:stretch-slim
MAINTAINER info@nextdom.com

ENV locale-gen fr_FR.UTF-8
ENV APACHE_PORT 80
ENV APACHE_PORT 443
ENV DEBIAN_FRONTEND noninteractive

RUN echo "127.0.1.1 $HOSTNAME" >> /etc/hosts && \
    apt-get update -y && \
    apt-get install -y --no-install-recommends \
      mysql-server grep gnupg \
      sed bash coreutils apache2 apache2-utils ntp ca-certificates \
      unzip curl sudo cron locate tar wget logrotate dos2unix ntpdate htop iotop iftop \
      smbclient git python python-pip libexpat1 ssl-cert \
      apt-transport-https cutycapt mysql-client mysql-common php php-curl php-gd php-imap \
      php-json php-mcrypt php-mysql php-xml php-soap php-xmlrpc libapache2-mod-php php-common \
      php-zip php-ssh2 php-mbstring && \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -fr /var/lib/apt/lists/*

# pre-install dev dependencies (would habe been installed by postint)
COPY ./install/dependencies/ensure-npm      /tmp/
COPY ./install/dependencies/ensure-yarn     /tmp/
COPY ./install/dependencies/ensure-composer /tmp/
COPY ./install/dependencies/ensure-sass     /tmp/
COPY ./install/dependencies/ensure-minify   /tmp/
RUN /tmp/ensure-npm      && \
    /tmp/ensure-yarn     && \
    /tmp/ensure-composer && \
    /tmp/ensure-sass     && \
    /tmp/ensure-minify   && \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -fr /var/lib/apt/lists/* && \
    rm -f /tmp/ensure-* && \
    npm cache rm --force && \
    composer clearcache

COPY docker/build/test/start.sh  /start.sh
COPY docker/build/test/launch.sh /launch.sh

VOLUME /data
ENTRYPOINT ["/usr/bin/env"]
CMD ["bash", "/start.sh"]
