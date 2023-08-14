The upgrade has different process depending on the version.
- Until Odoo 13.0: It uses a migration folder on many addons to ensure the upgrade.
- From Odoo 14.0: It is packed into 2 main folders for framework and scripts.

Every upgrade should be made to the next consecutive one.
As I am using Odoo 14.0, I'll document the process of "From Odoo 14.0"

From Odoo 14.0

Steps:
1. Change the target ODOO_VERSION in Dockerfile
2. Modify .env.template and delete the suffix .template
3. Get the content for the target upgrade. If you want to Upgrade Odoo 14.0 to Odoo 15.0, get the OpenUpgrade 15.0
   Repo: https://github.com/OCA/OpenUpgrade
   e.g. for 15.0: https://github.com/OCA/OpenUpgrade/archive/refs/heads/15.0.zip
   wget, decompress and rename folder to OpenUpgrade
4. Docker Compose and odoo.conf are already modified to include OpenUpgrade in the container.
5. addons-extra: Add the same modules you had in the old version.
   The script will update it in case some of them are from OCA.
6. Execute start.sh (Make sure it has execute permissions).
7. Load the database from old Odoo, enter with (localhost or public IP):8069.
8. Execute: sudo docker exec odoo odoo --database=[db-name] --upgrade-path=/mnt/OpenUpgrade/openupgrade_scripts/scripts --load=base,web,openupgrade_framework --update all --stop-after-init

Some bugs:

From Odoo 14.0 to Odoo 15.0
CRM fails when trying to enter a lead.
Solution:
- Enter developer mode.
- Update CRM in Applications.
- Go to Configuration > Translations > Translated terms
- Search for "meeting_count" as translation value
- Replace every occurrence of "meeting_count" by "calendar_event_count"

From Odoo 15.0 to Odoo 16.0
OCA module partner_industry_seconary failed and corrupted database
This package only adds a industry field to CRM leads
Solution:
- From Odoo 15.0 uninstall it.
- In Odoo 16.0 restore again the database
- Execute the "sudo exec" command for upgrade.