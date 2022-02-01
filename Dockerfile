#--==================================================--
#                      .______.
#     ______ ___.__. __| _/\_ |_________  ____
#     \____ <   |  |/ __ |  | __ \_  __ \/  _ \
#     |  |_> >___  / /_/ |  | \_\ \  | \(  <_> )
#     |   __// ____\____ |  |___  /__|   \____/
#     |__|   \/         \/      \/
#     
#                                         [ DOKR FILE ]
#
#--==================================================--
# NBTERMIX DOCKER FILE
FROM debian:latest
# INSTALL PKGS
RUN apt-get update && apt-get install -y git python3 
# pydbro specific
RUN cd root && git clone https://github.com/mtatton/pydbro
#
# next steps: cd /root/pydbro; ./run.sh
#
