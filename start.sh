#!/bin/bash

export $(cat .env | xargs)
envsubst < config/odoo/odoo.conf.template > config/odoo/odoo.conf
envsubst < config/nginx/default.conf.template > config/nginx/default.conf
sudo docker compose up -d