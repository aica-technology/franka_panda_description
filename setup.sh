#!/bin/bash

IMAGE_NAME=aica-technology/franka-panda-description

docker pull ghcr.io/aica-technology/ros2-ws:foxy
DOCKER_BUILDKIT=1 docker build -t "${IMAGE_NAME}" . || exit 1

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
echo $SCRIPT_DIR
aica-docker interactive "${IMAGE_NAME}" -u ros2 --volume=${SCRIPT_DIR}:/home/ros2/ros2_ws/src/franka_panda_description:rw