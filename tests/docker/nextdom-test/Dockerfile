FROM debian:stretch-slim
MAINTAINER info@nextdom.com

ENV locale-gen fr_FR.UTF-8
ENV APACHE_PORT 80
ENV APACHE_PORT 443
ENV DEBIAN_FRONTEND noninteractive

RUN echo "127.0.1.1 $HOSTNAME" >> /etc/hosts && \
    apt-get update -y && \
    apt-get install -y --no-install-recommends \
      software-properties-common \
      gnupg \
      wget && \
    add-apt-repository non-free && \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -fr /var/lib/{apt,dpkg,cache,log}/

COPY nextdom-apt.list /etc/apt/sources.list.d/
ADD  http://debian.nextdom.org/debian/nextdom.gpg.key nextdom.gpg.key
ADD  https://deb.nodesource.com/setup_10.x install_npm.sh

RUN  apt-key add nextdom.gpg.key && \
     bash install_npm.sh && \
     apt-get install -y --no-install-recommends \
       composer \
       nodejs \
       nextdom-mysql \
       nextdom-minimal \
       python-jsmin  && \
     apt-get clean autoclean && \
     apt-get autoremove -y && \
     rm -fr /var/lib/{apt,dpkg,cache,log} && \
     npm install -g sass && \
     npm cache rm --force

COPY start.sh  /start.sh
COPY launch.sh /launch.sh

VOLUME /data
ENTRYPOINT ["/usr/bin/env"]
CMD ["bash", "/start.sh"]
