#!/bin/bash

set_root() {
  local this=$(readlink -n -f $1)
  local bin=$(dirname $this)
  root=$(dirname $(dirname $bin))
}
set_root $0


./tests/docker/compose test kill > /dev/null 2>&1
./tests/docker/compose test down > /dev/null 2>&1
docker rmi nextdom-test-snap > /dev/null 2>&1
