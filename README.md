This repository has a structure of
- addons-extra: Addons to include in your Odoo deployment, if you will use a database with already some custom addons make sure they are in this place, so the install will be easy.
- config: Config file for odoo and nginx.
- odoo-upgrade-process: A separate and complete process to upgrade Odoo to another version, it has its own README.
- yml-store: Some docker-compose.yml configurations. In the name it includes the containers every file has. By default in the main folder is the config for odoo, postgres and nginx.
- .env.template: A file to update and rename to .env, the SUBDOMAIN_URL is exclusive for the docker compose yml with nginx.
- start.sh: It will autocomplete config (.conf files) with environment variables and start the docker-compose build, make sure it has a execute permission (chmod +x)

To execute this repository, get the repo and select from yml-store the configuration you need:

Follow the next steps
- git clone https://github.com/tomas-pucutay/odoo-base-config.git
- sudo vim .env.template #After edit, Esc :wq to close and save
- sudo mv .env.template .env
- chmod +x start.sh
- ./start.sh

Considerations:
The docker-compose with nginx requires DNS register in advance to relate the SUBDOMAIN_URL with the public IP. This will be accomplished by going to your domain provider, create an A type register, add the subdomain and the public IP.