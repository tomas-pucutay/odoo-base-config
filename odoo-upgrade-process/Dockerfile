ARG ODOO_VERSION=16

FROM odoo:${ODOO_VERSION}

USER root

RUN apt-get update && \
    apt-get install -y git python3-pip

RUN pip3 install git+https://github.com/OCA/openupgradelib.git@master#egg=openupgradelib