
# One AiQ: Odoo Challenge

## Before starting
Before starting I researched about Odoo to have a better understanding about what it is, how it works and went thru the development guide. 

For that I used the following references: 
- General Odoo Development Overview
https://medium.com/@jivasotechnologies/mastering-odoo-development-a-comprehensive-guide-a51ac2584457

- Basic understanding odoo interface (first module):
https://www.odoo.com/slides/getting-started-15

- Official development documentation
https://www.odoo.com/documentation/17.0/developer/tutorials.html

### Task 1: Working Odoo Instance
I found the following repository https://github.com/minhng92/odoo-17-docker-compose with the Docker Composer and used it to spin up the containers for PostgreSQL and Odoo 17. In the docker composer Odoo service I have adjusted the Oddo port for the requested one (8069) and runned the following command to spin up the containers:

`docker-compose up -d`

###### Odoo URL
http://localhost:8069

###### Restart Odoo:
`docker-compose restart`

###### Stop Odoo:
`docker-compose down`

###### Additional Information:
- Logs file: ./etc/odoo-server.log
- Config file: ./etc/odoo.conf
- Custom Addons folder: ./addons




 