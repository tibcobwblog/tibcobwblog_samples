FROM tutum/centos
COPY files/TIB_ems_8.2.1_linux_x86.zip /tmp/
COPY files/jdk-7u75-linux-x64.rpm /tmp/

RUN useradd -ms /bin/bash tibco
ENV HOME /home/node
RUN rpm -Uvh /tmp/jdk-7u75-linux-x64.rpm
RUN alternatives --install /usr/bin/java java /usr/java/latest/bin/java 2
RUN yum -y  install unzip


RUN mkdir /tmp/software/
RUN mv /tmp/TIB_ems_8.2.1_linux_x86.zip /tmp/software/

RUN unzip /tmp/software/TIB_ems_8.2.1_linux_x86.zip -d /tmp/software/
RUN /tmp/software/TIBCOUniversalInstaller-lnx-x86.bin -silent

EXPOSE 7222

COPY files/ems.sh /opt/tibco/ems/
RUN chmod +x /opt/tibco/ems/ems.sh
RUN chown -R tibco:tibco /tmp/software/
RUN chown -R tibco:tibco /opt/tibco/
RUN chown -R tibco:tibco /home/user/tibco/

VOLUME /home/user/tibco/tibco/cfgmgmt/ems/data:rw

USER tibco
CMD /opt/tibco/ems/ems.sh
##CMD /run.sh
