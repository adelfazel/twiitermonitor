Adel Fazel
6/NOV/2020
--------
This application is written in response to seersec challenge. 

Challenge accepted. 

-------- Spec ---------

This is a Python program that monitors a twitter account.
This programs prints new tweets to stdout.

1) To make use of the program extract and enter:
    make run (or sudo make run)
2) The above command will build a docker image, with the required libraries and executes the program.
3) The solution includes two request handlers, one for "GET" and one for "PUT" requests. To use them: 
    a) curl localhost:5000 (retrieves existing tweets)
    b) curl -X PUT -H "account: someaccount" localhost:5000, switches monitoring to "someaccount" (not required by the spec 
but too cool to ignore)
4) To start the program using command line:
    a) pip3 install requirements.txt
    b) go to /app
    c) python3 src/server/server.py 
5) optional arguments allow initial account and different consumer-key,consumer-password pair
sample execution: python3 src/server/server.py -a "hello"
6) to tear down the program:
make stop (sudo make stop)
 