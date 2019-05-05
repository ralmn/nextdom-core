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
    apt-get install -y --no-install-recommends \
      systemd \
      systemd-sysv \
      mysql-server \
      sed \
      software-properties-common \
      gnupg \
      wget && \
    add-apt-repository non-free && \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -fr /var/lib/{apt,dpkg,cache,log}/

# install nextdom debian dependencies
COPY ./tests/docker/conf/apt/nextdom-apt.list /etc/apt/sources.list.d/
ADD  http://debian.nextdom.org/debian/nextdom.gpg.key nextdom.gpg.key
RUN apt-key add nextdom.gpg.key && \
    apt-get update -y && \
    apt-get install -y  nextdom-common && \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -fr /var/lib/{apt,dpkg,cache,log}/

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
    rm -fr /var/lib/{apt,dpkg,cache,log}/

# optional built-in configured samba server (useful for tests)
ARG  with_samba
COPY ./tests/docker/nextdom-dev/with_samba.sh /tmp/
RUN  bash /tmp/with_samba.sh && \
     apt-get clean autoclean && \
     apt-get autoremove -y && \
     rm -fr /var/lib/{apt,dpkg,cache,log}/

#fix apparmor bug when dockerd host is ubuntu:bionic-beaver
# for the record, the following fixed problem a time, then failed again:
# RUN  echo "/usr/sbin/mysqld { }" > /etc/apparmor.d/usr.sbin.mysqld
RUN mv /usr/sbin/mysqld /usr/bin/mysqld && \
    ln -nfs /usr/bin/mysqld /usr/sbin/mysqld

COPY ./tests/docker/conf/systemd/nextdom-install.service /etc/systemd/
RUN  systemctl enable /etc/systemd/nextdom-install.service

EXPOSE 80
CMD ["/sbin/init"]
