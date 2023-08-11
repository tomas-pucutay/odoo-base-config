#!/bin/bash

envsubst < config/odoo/odoo.conf.template > config/odoo/odoo.conf
sudo docker compose up -d --build