## File structure
- addons-extra: Addons to include in your Odoo deployment, if you will use a database with already some custom addons make sure they are in this place, so the install will be easy. Most of them are from OCA repository, except for crm_custom_field which is created in-house.
- config: Config file for odoo, nginx, certbot.
- yml-store: Some docker-compose.yml configurations. In the name it includes the containers every file has. By default in the main folder is the config for odoo, postgres and nginx.
- .env.template: A file to update and rename to .env, the SUBDOMAIN_URL is exclusive for the docker compose yml with nginx.
- start.sh: It will autocomplete config (.conf files) with environment variables and start the docker-compose build, make sure it has a execute permission (chmod +x)

## First Step

1. Define the need: Get the repo and select from yml-store for the configuration you want
```bash
git clone https://github.com/tomas-pucutay/odoo-base-config.git
cd odoo-base-config
sudo cp yml-store/[selected-yml-file] docker-compose.yml
```

2. Config file: Read carefully .env.template to update it, some variables are required for specific yml configs.
```bash
sudo vim .env.template #After edit, Esc :wq to close and save
sudo mv .env.template .env
chmod +x start.sh
./start.sh
```

3. Additional process (exclusive for certbot): After starting containers, certbot will generate the SSL. It's required to replace the actual nginx default.conf with the new one for the SSL
```bash
sudo mv config/nginx/default.conf config/nginx/default.conf.old
sudo cp config/certbot/nginx/default.conf config/nginx/default.conf
sudo docker restart nginx
```

## Some requisites in advance for Nginx:
The docker-compose with nginx requires DNS register in advance to relate the SUBDOMAIN_URL with the public IP. This will be accomplished by going to your domain provider, create an A type register, add the subdomain and the public IP.

## Bonus
- 0 odoo-upgrade-process: A separate and complete process to upgrade Odoo to another version, it has its own README.