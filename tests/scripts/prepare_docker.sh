#!/bin/bash

set -e
if [[ "$OSTYPE" == "darwin"* ]]; then
    rootDir=$(dirname $(dirname $(cd $(dirname $0) && pwd -P)))
else
    rootDir=$(dirname $(dirname $(dirname $(readlink -n -f $0))))
fi

echo "step 1. removing  existing nextdom-test containers..."
${rootDir}/tests/docker/compose test kill  > /dev/null 2>&1 || true
${rootDir}/tests/docker/compose test down  > /dev/null 2>&1 || true


echo "step 2. creating installer container nextdom-test..."
${rootDir}/tests/docker/compose test up -d >/dev/null 2>&1 || {
  echo "-> unable to create nextdom-test container"
  echo "-> command: ${rootDir}/tests/docker/compose test up -d"
  exit 1
}


echo -n "step 3. watting for installation to complete..."
END_OF_INSTALL_STR="OK NEXTDOM TEST READY"
while true; do
	DOCKER_LOGS=$(docker logs --tail 10 nextdom-test 2>&1)
	if [[ "$DOCKER_LOGS" =~ .*NEXTDOM.TEST.READY.* ]]; then
		break
	fi
  echo -n "."
	sleep 2
done
echo " "


echo "step 4. snapshotting container to nextdom-test-snap..."
docker exec   nextdom-test /bin/rm -fr /var/www/html/plugins/*
docker commit nextdom-test nextdom-test-snap >/dev/null


echo "step 5. deleting nextdom-test installer container..."
${rootDir}/tests/docker/compose test kill  > /dev/null 2>&1 || {
  echo "-> unable to kill container nextdom-test"
  echo "-> command: ${rootDir}/tests/docker/compose test kill"
  exit 1
}
${rootDir}/tests/docker/compose test down  > /dev/null 2>&1  || {
  echo "-> unable to remove container nextdom-test "
  echo "-> command: ${rootDir}/tests/docker/compose test down"
  exit 1
}
