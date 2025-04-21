
# One AiQ: Odoo Challenge

## Before starting
Before starting I researched about Odoo to have a better understanding about what it is, how it works and went thru the development guide. 

For that I used the following references: 
- General Odoo Development Overview
https://medium.com/@jivasotechnologies/mastering-odoo-development-a-comprehensive-guide-a51ac2584457

- Basic understanding odoo interface (first module):
https://www.odoo.com/slides/getting-started-15

- Official development documentation
https://www.odoo.com/documentation/17.0/
https://www.odoo.com/documentation/17.0/developer/tutorials.html
https://www.odoo.com/documentation/17.0/administration/odoo_sh/getting_started/first_module.html?highlight=libraries

- Official Python documentation
https://docs.python.org/3/

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

###### Task 1 Github commit: https://github.com/mevilela/odoo_challenge/commit/41518311c5b21ce84c61cd2edec5fcdaa08d7bb7


### Task 2 

Create the view layer
https://www.odoo.com/documentation/17.0/th/developer/reference/user_interface/view_records.html?highlight=view#odoo.addons.base.models.ir_ui_view.View

I have researched about Odoo constrains, depends and exceptions 
https://www.odoo.com/documentation/17.0/pt_BR/developer/reference/backend/orm.html?highlight=constrains#odoo.api.constrains
https://www.odoo.com/documentation/17.0/pt_BR/developer/reference/backend/orm.html?highlight=exceptions#module-odoo.exceptions
https://www.odoo.com/documentation/17.0/pt_BR/developer/reference/backend/orm.html?highlight=depends#odoo.api.depends

###### Task 2 Github commit: https://github.com/mevilela/odoo_challenge/commit/aa7201e85c0768bd736556e7ebafdfd561770f9f

### Task 3: 
Testing on Odoo Research
https://www.odoo.com/documentation/17.0/th/developer/reference/backend/testing.html?highlight=testing
 
https://www.cybrosys.com/blog/how-to-write-test-case-in-the-odoo-17-erp

https://medium.com/@devanshu.bhatt_42277/a-complete-guide-to-software-testing-in-odoo-with-code-examples-341f1a783607

https://www.youtube.com/watch?v=oUbRHnOZUbo

Configuration changes to enable tests on odoo.conf
https://www.odoo.com/documentation/17.0/th/developer/reference/backend/testing.html?highlight=transactioncase#running-tests

###### Task 3 Github commit:https://github.com/mevilela/odoo_challenge/commit/a90185058cc8d0b840ef5dae66d3b7a8bade10b2

### Bonus 1: Add custom discount button

- A new button called "Apply Custom Discount" was added at the view layer
- Business logic was updated: if a custom discount is applied, it overrides the default 10% low stock discount
- During my research I found that there is an specific ***action type button***. However, I wasn't able to successfully implement it. I will need to research futher how to properly use it. 
- The current implementation prioritizes functionality while maintaining compatibility with existing components.

https://www.odoo.com/documentation/17.0/developer/reference/backend/actions.html

https://www.odoo.com/documentation/17.0/th/developer/reference/user_interface/view_architectures.html?highlight=button#reference-view-architectures-form-button

https://www.cybrosys.com/blog/how-to-add-a-button-inside-action-menu-in-odoo-17

https://www.youtube.com/watch?v=Ny13m-l-wHU

https://www.odoo.com/forum/help-1/how-can-i-add-buttons-to-the-header-of-a-list-view-for-quick-access-to-things-in-the-action-menu-186225

###### Bonus 1 Github commit: https://github.com/mevilela/odoo_challenge/commit/67cf9af34e41b0166cbedfe19f8ab90b55d5cf07

### Bonus 2: Remove custom discount button
- For the Bonus 2 task I researched how to use conditionals for buttons in Odoo views
https://www.youtube.com/watch?v=1sgflzCAx9U

- I modified the compute_discount method, which ended up disabling the effect of my Apply Discount button, as the discount is now applied automatically. 

- However, for future improvements, my goal is to hide the custom_discount field by default and only show it when the Apply Discount button is clicked. This would make the UI cleaner and provide better control over the discount application process.

### Limitations 
While working on this challenge, I faced some dificulties:
- I was unable to run the tests inside the container environment, which prevented me from properly validating them.  (Task 3)

- VS Code was unable to correctly recognize Odoo’s libraries, making development and debugging more difficult.

- These issues highlighted the need for deeper research on how to configure a pratical development environment for Odoo, particulary container integration and IDE support. 

### Further Improvements
- To improve this feature and my overall understanding about Odoo development, I plan to explore more Odoo concepts. 
- One of my goals is to take this Udemy course on Odoo Development (https://www.udemy.com/course/mastering-odoo-9-development-technical-fundamentals/?couponCode=KEEPLEARNING)
- I also intent to complete the official Odoo "Getting Start"  tutorial available at http://odoo.com (which I started to do during this challenge) and take more advanced Odoo official tutorials

### Conclusion
I truly enjoyed the opportunity to get to know Odoo and participate in this challenge. I believe this challenge was a valuable learning experience which allows me to deep dive into a such versatile and powerful platform. I’m excited to continue exploring Odoo's features and applying my knowledge in future projects.
