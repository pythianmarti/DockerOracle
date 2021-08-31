# DockerOracle
DockerOracle is primarily for dockering the Oracle environments and make it available as microservice for deploying on various containers. 

While Oracle has already published various docker images on github, this repository would contain images for speicifc versions that are not published by Oracle. Most of the content was copied from Oracle github and customizations were made as required.

Below steps would help to dockerize OHS 12.1.3, the last version that supports mod_plsql based applications and helps customers for hosting their applications on cloud (EKS/GKE/AKS)

Please note that this content is just a knowledge reference and usage would be based on personal discretion. User should review vendor licensing requirements.

1. Download 1213 media using wget_12.1.3.sh and rename the file as fmw_12.1.3.0_ohs_linux64_Disk1_1of1.zip
2. Login to dockerhub, accept the conditions for store/oracle/serverjre:1.8.0_241-b07
3. Build the docker image using below command

cd  dockerfiles
sh buildDockerImage.sh -v 12.1.3.0 -s

4. Create the container runtime for OHS 12.1.3

docker run -itd --name=OHS oracle/ohs:12.1.3.0

5. Login to container and ensure all processes are up

docker exec -u oracle -it SabreOHS /bin/bash
curl http://localhost:7777|grep -i OHS
