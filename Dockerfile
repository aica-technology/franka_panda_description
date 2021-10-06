FROM ghcr.io/aica-technology/ros2-ws:foxy

USER ${USER}
WORKDIR ${HOME}/ros2_ws
COPY ./ ./src/franka_panda_description

RUN /bin/bash -c "source ${HOME}/ros2_ws/install/setup.bash; colcon build --symlink-install"