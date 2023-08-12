#!/bin/bash

export $(cat .env | xargs)

envsubst < config/odoo/odoo.conf.template > config/odoo/odoo.conf

for var in $(grep -oP '\${\w+}' config/nginx/default.conf.template | sort -u); do
    envsubst "$var" < config/nginx/default.conf.template > config/nginx/default.conf.updated
    mv config/nginx/default.conf.updated config/nginx/default.conf
done

sudo docker compose up -d