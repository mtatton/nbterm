#--==================================================--
#
# _______ ___. ___________                  .__
# \      \\_ |_\__    ___/__________  _____ |__|__  ___
# /   |   \| __ \|    |_/ __ \_  __ \/     \|  \  \/  /
#/    |    \ \_\ \    |\  ___/|  | \/  Y Y  \  |>    <
#\____|__  /___  /____| \___  >__|  |__|_|  /__/__/\_ \
#        \/    \/           \/            \/         \/
# 
#                                         [ DOKR FILE ]
#
#--==================================================--
# NBTERMIX DOCKER FILE
FROM debian:latest
# INSTALL PKGS
RUN apt-get update; apt-get -y install python3 vim screen python3-pip
# INSTALL NBTERMIX
RUN pip3 install jupyter_client ipykernel nbtermix
# DEBIAN XI FIX
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.9 1
