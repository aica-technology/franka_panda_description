FROM ghcr.io/aica-technology/ros2-ws:foxy

RUN sudo apt-get update && sudo apt-get install -y ros-foxy-joint-state-publisher-gui

USER ${USER}
WORKDIR ${HOME}/ros2_ws
RUN git clone -b foxy --single-branch https://github.com/IntelRealSense/realsense-ros.git && \
  mv realsense-ros/realsense2_description ./src/realsense2_description && rm -rf realsense-ros
COPY ./ ./src/franka_panda_description

RUN /bin/bash -c "source ${HOME}/ros2_ws/install/setup.bash; colcon build --symlink-install"