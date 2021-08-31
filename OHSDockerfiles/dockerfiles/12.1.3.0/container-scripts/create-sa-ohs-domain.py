#!/usr/bin/python
#
# Copyright (c) 2016-2019 Oracle and/or its affiliates. All rights reserved.
#
# Licensed under the Universal Permissive License v 1.0 as shown at http://oss.oracle.com/licenses/upl.
#
# Create OHS Domain and OHS System component
#
# OHS Domain 'ohsDomain' (or anything defined under DOMAIN_NAME) to be created inside the Docker image for OHS
# OHS System Component "ohs1" (Or anything defined under OHS_COMPONENT_NAME)to be created inside the Docker image for OHS
#
# Author: hemastuti.baruah@oracle.com
# ==============================================
import os, sys
admin_port   = (os.environ.get("ADMIN_PORT", "7001"))
ohs_http_port   = (os.environ.get("OHS_LISTEN_PORT", "7777"))
ohs_ssl_port   = (os.environ.get("OHS_SSL_PORT", "3333"))
ohs_comp_name   = os.environ.get("OHS_COMPONENT_NAME", "ohs1")
domain_name  = os.environ.get("DOMAIN_NAME", "ohsDomain")
domain_path  = '/u01/oracle/ohssa/user_projects/domains/' + domain_name
ORACLE_HOME = '/u01/oracle/ohssa'
# Select OHS standalone template
# ==============================================
#setTopologyProfile('Compact')
#selectTemplate('Oracle HTTP Server (Standalone)')
#loadTemplates()
#showTemplates()
readTemplate(ORACLE_HOME + '/wlserver/common/templates/wls/base_standalone.jar')
addTemplate(ORACLE_HOME + '/ohs/common/templates/wls/ohs_standalone_template_12.1.3.jar')
# Set NodeManager user name and password
# ======================================================================
cd('/')
create(domain_name, 'SecurityConfiguration')
cd('SecurityConfiguration/ohsDomain')
set('NodeManagerUsername','weblogic')
set('NodeManagerPasswordEncrypted','welcome1')
setOption('NodeManagerType','PerDomainNodeManager')
# Create OHS System Component by the name ohs1, Configure OHS Listen Port and SSL Port
# ======================================================================
cd('/OHS/' + ohs_comp_name)
cmo.setAdminHost('127.0.0.1')
cmo.setAdminPort(admin_port)
cmo.setListenAddress('127.0.0.1')
cmo.setListenPort(ohs_http_port)
cmo.setSSLListenPort(ohs_ssl_port)
#Write Domain, close template and exit
# ======================================================================
#writeDomain(r'/u01/oracle/ohssa/user_projects/domains/ohsDomain')
writeDomain(domain_path)
dumpStack()
closeTemplate()
exit()
