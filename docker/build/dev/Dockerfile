FROM debian:stretch-slim
MAINTAINER info@nextdom.com

ENV locale-gen fr_FR.UTF-8
ENV APACHE_PORT 80
ENV APACHE_PORT 443
ENV MODE_HOST 0
ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=DontWarn
ENV DEBIAN_FRONTEND noninteractive

RUN echo "127.0.1.1 $HOSTNAME" >> /etc/hosts && \
    apt-get update  -y && \
    apt-get install -y --no-install-recommends software-properties-common && \
    add-apt-repository non-free && \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -fr /var/lib/apt/lists/*

# install nextdom runtime dependencies
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
      systemd systemd-sysv gnupg wget \
      openssl apache2 bash sudo tar wget curl lsb-release ntp logrotate ntpdate \
      git python python-pip libexpat1 ssl-cert apt-transport-https cutycapt xauth \
      duplicity libav-tools libsox-fmt-mp3 sox libttspico-utils php php-curl php-gd \
      php-imap php-json php-mcrypt php-mysql php-xml php-soap php-xmlrpc \
      libapache2-mod-php php-common php-dev php-zip php-ssh2 php-mbstring php-ldap \
      composer mysql-server mysql-client grep sed bash coreutils unzip \
      locate telnet dos2unix htop iotop vim iftop smbclient xvfb gcc g++ make && \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -fr /var/lib/apt/lists/*

# pre-install dev dependencies
COPY install/dependencies/ensure-npm      /tmp/
COPY install/dependencies/ensure-yarn     /tmp/
COPY install/dependencies/ensure-composer /tmp/
COPY install/dependencies/ensure-sass     /tmp/
COPY install/dependencies/ensure-minify   /tmp/
RUN /tmp/ensure-npm      && \
    /tmp/ensure-yarn     && \
    /tmp/ensure-composer && \
    /tmp/ensure-sass     && \
    /tmp/ensure-minify   && \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -fr /var/lib/{apt,dpkg,cache,log}/ && \
    rm -f /tmp/ensure-{npm,yarn,composer,sass,minify} && \
    npm cache rm --force && \
    composer clearcache

# optional built-in configured samba server
ARG  with_samba
COPY docker/build/dev/with_samba.sh /tmp/
RUN  bash /tmp/with_samba.sh && \
     apt-get clean autoclean && \
     apt-get autoremove -y && \
     rm -fr /var/lib/{apt,dpkg,cache,log}/ && \
     rm -f /tmp/with_samba.sh

#fix apparmor bug when dockerd host is ubuntu:bionic-beaver
RUN mv /usr/sbin/mysqld /usr/bin/mysqld && \
    ln -nfs /usr/bin/mysqld /usr/sbin/mysqld

COPY docker/build/dev/nextdom.service /etc/systemd/
RUN  systemctl enable /etc/systemd/nextdom.service

EXPOSE 80
CMD ["/sbin/init"]
