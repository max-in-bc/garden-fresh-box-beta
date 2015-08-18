Want to run this?
Open this directory in a terminal and type

$ python server.py [development|production]

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
