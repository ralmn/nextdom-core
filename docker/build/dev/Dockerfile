FROM debian:stretch-slim
MAINTAINER info@nextdom.com

# install nextdom runtime dependencies
COPY docker/build/common/apt-source-non-free.list /etc/apt/sources.list.d/
COPY docker/build/common/apt-package-list         /tmp/apt-package-list
RUN echo "127.0.1.1 $HOSTNAME" >> /etc/hosts && \
    apt-get update -y && \
    apt-get install -y --no-install-recommends \
      $(cat /tmp/apt-package-list) \
      php-dev \
      mysql-server && \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -fr /var/lib/apt/lists/* /tmp/apt-package-list

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
    npm cache rm --force && \
    composer clearcache && \
    rm -fr /var/lib/apt/lists/* && \
    rm -f /tmp/ensure-*

# optional built-in configured samba server
ARG  with_samba
COPY docker/build/dev/with_samba.sh /tmp/
RUN  bash /tmp/with_samba.sh && \
     apt-get clean autoclean && \
     apt-get autoremove -y && \
     rm -fr /var/lib/apt/lists/* && \
     rm -f /tmp/with_samba.sh

#fix apparmor bug when dockerd host is ubuntu:bionic-beaver
RUN mv /usr/sbin/mysqld /usr/bin/mysqld && \
    ln -nfs /usr/bin/mysqld /usr/sbin/mysqld

COPY docker/build/dev/nextdom.service /etc/systemd/
RUN  systemctl enable /etc/systemd/nextdom.service

EXPOSE 80
CMD ["/sbin/init"]
