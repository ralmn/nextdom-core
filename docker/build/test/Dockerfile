FROM debian:stretch-slim
MAINTAINER info@nextdom.com

COPY docker/build/common/apt-source-non-free.list /etc/apt/sources.list.d/
COPY docker/build/common/apt-package-list         /tmp/apt-package-list
RUN echo "127.0.1.1 $HOSTNAME" >> /etc/hosts && \
    apt-get update -y && \
    apt-get install -y --no-install-recommends \
      $(cat /tmp/apt-package-list) \
      php-dev mysql-server && \
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
