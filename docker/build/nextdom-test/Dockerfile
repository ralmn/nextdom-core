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


# install nextdom debian dependencies
COPY ./tests/docker/conf/apt/nextdom-apt.list /etc/apt/sources.list.d/
ADD  http://debian.nextdom.org/debian/nextdom.gpg.key nextdom.gpg.key
RUN apt-key add nextdom.gpg.key && \
    apt-get update -y && \
    apt-get install -y  nextdom-mysql nextdom-minimal && \
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
    rm -fr /var/lib/{apt,dpkg,cache,log}/ && \
    rm -f /tmp/ensure-{npm,yarn,composer,sass,minify} && \
    npm cache rm --force && \
    composer clearcache

COPY tests/docker/nextdom-test/start.sh  /start.sh
COPY tests/docker/nextdom-test/launch.sh /launch.sh

VOLUME /data
ENTRYPOINT ["/usr/bin/env"]
CMD ["bash", "/start.sh"]
