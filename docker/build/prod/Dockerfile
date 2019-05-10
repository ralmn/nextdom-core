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
    rm -rf var

###############
# final image #
###############
FROM debian:stretch-slim

# install run dependencies
COPY docker/build/common/apt-source-non-free.list /etc/apt/sources.list.d/
COPY docker/build/common/apt-package-list         /tmp/apt-package-list
RUN echo "127.0.1.1 $HOSTNAME" >> /etc/hosts && \
    apt-get update -y && \
    apt-get install -y --no-install-recommends $(cat /tmp/apt-package-list) && \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# copy nextdom root from builder image
WORKDIR /usr/share/nextdom
COPY --from=builder /usr/share/nextdom ./

# register nextdom service, that runs postint on first run
COPY docker/build/prod/nextdom.service  /usr/share/nextdom/systemd/
COPY docker/build/prod/nextdom          /usr/share/nextdom/systemd/
RUN systemctl enable /usr/share/nextdom/systemd/nextdom.service

STOPSIGNAL SIGRTMIN+3
VOLUME /usr/share/nextdom
VOLUME /var/lib/nextdom
VOLUME /var/log/nextdom
VOLUME /etc
EXPOSE 80
EXPOSE 443

CMD ["/sbin/init"]
