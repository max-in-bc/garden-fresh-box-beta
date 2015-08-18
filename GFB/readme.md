***The Garden Fresh Box Web Application***

Want to run this?
Open this directory in a terminal and type

`$ python server.py [development|production]`

Then open a browser, and go to 127.0.0.1:80

If something crashes
  -either inspect in browser (right click, inspect element, check out the console. Should show html/javascript errors)
  -if its the server side that’s crashing, you’ll get a url in the terminal window with a link to debug your issue.

System Requirements
————————————
pycrypto (pip install pycrypto)
mysql (brew install mysql)
MySQL-python (pip install MySQL-python)
(pip install --allow-external mysql-connector-python mysql-connector-python)

*The Project Goals*
-------------------

*The purpose of this project is to provide the GCHC clients with a
working website suited to carry out any administrative task relating to
Garden Fresh Box. Currently the only system available is to call in via
phone to order, and customers must pay with cash when they arrive to
pick up a pre-ordered box. By sometime in 2015 the plan is to have a
website that will allow customers to order* **Garden Fresh Boxes** *from
their preferred host site, as well as use PayPal to pay for their box
online before they ever go to pick it up. The website will also allow
for other users to donate cash via PayPal, and the database will
store/offer automatically generated tax receipts over the federal
minimum for charitable donations. Moreover, host sites will be able to
use the website to review all donations and box orders for their
specific site, for each specific pickup date, and they will be able to
make changes/transfers therein. A master administrator (to be eventually
controlled by a GCHC employee) will exist who will have access to all
data from the project, including read/write access to host site and
customer order information. The end goal of this project will be a
preliminarily tested and working web application suited for properly
organizing, administering, and maintaining the Garden Fresh Box project
inside-and-out by 2015.*

*Pages Included* 
----------------

-   **Home** – Home page with links

-   **Information** – Contains information on program, boxes, host
    sites, and pickup dates

-   **Purchasing** – A page for a user to place a box purchase using
    online order form

-   **Donations –**Currently linking to CanadaGives.org will eventually
    integrate with their API once it is updated

-   **Contact –**This page contains contact info for the Guelph
    Community Health Centre

-   ### **User Tools**

    -   **User orders –**Lists only orders made by user who is logged in

    -   **User donations –**Lists only donations made by user who is
        logged in

    -   **Change user password –**User who is logged in may change their
        password

    -   **Edit user information –**User who is logged in may change
        profile information

-   ### **Host Site Tools** (Only available to host site coordinators and GFB admins) 

    -   **Manage orders for a particular host site –**Edit/add orders
        associated with a particular host site

    -   **Edit details (contact info) for particular host site –**Edit
        info associated with host site such as hours of operation

-   ### **Admin Tools** (Only available to GFB admins)

    -   **Manage user accounts –**Manage accounts of users who have
        signed up; may also be used to assign administrator or host site
        priveledges

    -   **Manage complete order list (all host sites) –**See orders by
        host site, if a host site is selected it will open up a page
        listing all orders for that host site

    -   **View complete donation list –**Lists all donations by users
        and non-users

    -   **View complete customer list –**List all customers who have
        purchased boxes, if a user is selected then list his/her orders.
        Existing orders can be edited as well.

    -   **Manage the pickup dates for boxes –**Manage the pickup dates
        that are used with forms throughout the site, as well as listed
        on the info page

    -   **Manage sample boxes that appear on info page –**Manage the
        example boxes that are listed on the info page


\*NOTE: **See config/routing.py to get a list of all of the files
created for the project (some are under construction or unused); list
also contains a description for each page of the website**

*About the Project/Pyramid*
---------------------------

*This project is built using Model-View-Controller principles, this is
based largely on the fact that Pylons Pyramid Python framework uses this
framework as well. For more info on Pylons Pyramid and MVC principles
please visit their site
at:* [**http://docs.pylonsproject.org/en/latehest/docs/pyramid.html**](http://docs.pylonsproject.org/en/latest/docs/pyramid.html).

The project itself is based on one of the basic Pyramid scaffolds, and has
the following basic structure:

**GFB** is the main project folder

the **data** and **GardenFreshBox.egg-info** are automatically generated
and do not need to be changed by anyone

Inside the **gardenfreshbox** folder is where all of the project code
resides:

**config** contains a number of Python configuration files (including
routing table and some Pyramid setup)

**controllers** contains the Python MVC controllers for errors,
hostsites, the index page, purchases, and users

**lib** contains globals and helper functions

**model** contains all of the models for the site cookie, user views,
hostsite views, sale views, and all access to backend

**public** contains all data downloaded by user (css, images, js, etc.)

**templates** contains the web markup in the form of MAKO templates which
are basically HTML with some added tricks

-   the **.ini** files (like development.ini) are used by Pyramid to
    configure the server before launch

-   **README.txt** contains quick info on how to run the development
    server

-   **requirements.txt** contains a list of applications installed on the
    production machine

-   **setup.cfg** contains more Pyramid configuration

-   **setup.py** is the Python/Paster setup wrapper that must get run on
    each development machine before the server can start
    (**startserver.sh** is a quick run of dev server)

*Database Schema*
-----------------------
 
![alt text](https://raw.githubusercontent.com/maxgardiner/Garden-Fresh-Box/master/Database%20Schema.png "Schema for Backend")

*How to add a new page*
-----------------------

1.  *Create the html/mako page(s) for the new page*

2.  *Add physical links to the existing mako templates which must link
    to the new page (in most cases adding it to the sidebar.mako)*

3.  *Add the routing information to routing.py in
    the* **config** *folder*

4.  *Sometimes new models must be created if adding new functionality*

*How to start the server*
----------------------------------------------------------------------

1.  *Setup the python server:* 
	**$python setup.py [develop|production]**

2.  *Start the server with the WSGI (in this case its Pserver until
    Gunicorn or more appropriate gateway is setup):* 
	**$paster serve --reload development.ini**

*How to switch over to production machine (ideally)*
----------------------------------------------------------------------

1.  *Tar the project, and untar on the production machine*

2.  *Change the links to the php files located in
    models/GFBDatabaseController.py for the login verification to the
    appropriate full links on the production machine (a quick search for
    “php” in the document will find them for you)*

3.  *Install all needed, Apache, Pyramid, PHP, etc.*

4.  *Run the project according to README.txt*

*How the database is associated* 
--------------------------------

Within the **model** folder there is a csv file with access
information to the database. If the database is ever moved or changes IP
then this is the file that must be changed to update the server.
Unfortunately we had to remove database constraints so that the mobile
developer and I could continue working with the same database during
development, and the proper constraints have never been put back in
place.

*How the editing timer works*
-----------------------------------------------------------------------

As it stands right now users nor admins can change records after
payment has been received, and users cannot change their orders after
the first friday of the month.

The same thing goes for not listing past pickup dates in dropdown
boxes, in the future perhaps admin should be given opportunity to set
past dates.

In the sale.py **model** the calculation is done in the method
called 	**toDistList**

*Still To Do*
-------------

-   *Some sort of back-end sorting must be done to take care of archived
    orders once this system is used more, for example orders from 2012
    and 2013 will not be displayed as readily as orders from 2015, etc.*

-   *Integrate GCHC paypal info with Paypal button on orders*

-   *Integrate GCHC CanadaGives info with donations page*

-   ***The Voucher System***

-   *Must have a way of notifying "pay in person" customers or
    customers who missed deadlines*

-   *Error messages for orders that cannot be edited anymore due to time
    passed or payment received*

-   *A "forgot-your-password" page will be necessary but we will
    force them to change their password upon entering*

-   *It is recommended that forms be validated in the backend as well*

-   *Email server setup integrate with system*

-   *Setup on production machine*

-   *Paypal IPN*

-   *Fonts*

-   *CASL legislation standards*

-   *Email server setup*
-       ..*Email non-paid recipients* 
-       ..*Email paid recipients*
-       ..*Email newsletter signups*

-   *Write instructions for forms (instructions button maybe)*

-   *Donation form on our website populates DonateNow site form*

-   *Back-end cleanup*

-   *Move back-end to production machine*

-   *Archival mechanisms if needed*

-   *Beta testing*

*Notes*
-------

-   *The passwords are hashed and salted using PHP's builtin abilities
    to do so*

-   *Shellshock use of python command line security issues fixed*

-   *Inputs to database are sanitized*

-   *Penetration testing necessary still, as I AM NOT A SECURITY EXPERT*

-   *Still waiting on a main logo for the header*

-   *Feedback from users will be nice because I have a feeling more
    instruction will be necessary for some of the pages especially
    admins*

-   *As it stands right now validation.js contains all validation
    javascript for forms, and each html file has it's own js file. I
    realize this is not properly compartmentalized but I did this for
    simplicitys sake, as this is my first major web application*

