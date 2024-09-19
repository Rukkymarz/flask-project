# Flask, anislble, Jenkins, project 

## Step 1
install python and flask
entered resume template and run the code with
```bash 
python main.py 
```
## step 2 
* create 2 severs one with T2 medium (jenskins master) and one with T2 micro(nodes).
* Go to `Manage Jenkins` -> plugins and install SSH build agent 
* connect the Node to Master Node. open jenskins in the browser, then go to `manage jenskins` then click on `Node` then `add new Nodes`.
* enter Node name and select the type `Permanent Agent`, then click create.
* enter your project 
- on `Description`enter any description
- then `Number of executors` should be 1. 
- on `Remote root directory` enter the Node root directory eg /home/ubuntu, 
- then on label any `label` name eg N1 label is important. 
 - leave `usage` as default.
 - change  `Launch method` launch agent via SSH 
    - on `host` enter private IP of Node.
    -  on credientials click on add 
        - on `domain` leave as default 
        - on `kind` change to SSH username with private key
        - on `scope` leave as default
        - on ID enter n1 
        - on description enter n1 
        - on user name enter ubuntu 
        - on private key enter directly and copy and paste pem file. save and add then select N1 on credentials
        

- enter   `Availability` `node properties` leave as default
- after creating the node it should be offline, to launch, install java and lunch. 

## step 3 configure webhook

- go to the github on the project repo, click on settings
- select webhooks
   - add wehooks 
   - on payload url add the jenskins master public IP url e.g http://54.175.184.89:8080/github-webhook/
   - Leave everything as default, then add webhook and wait for it activate with the check mark symbol.

## Step 4 Build Test and Deploy with jenkins
 - install pluggins 
    1. credentials 
    2. mailer
    3. github
    4. stageview 

## Step 5 Email Configuration
 - search for App password. 
   - signing, enter app name
   - click on create and copy code
- go to jenkins,manage jenkins
   - click on system 
   - scroll down to Email notification 
    - on SMPT Server add smpt.gmail.com
    - expand the advance button 
    - then select use smpt authentication
     - then on username enter email address 
     - on password enter the code copied from app password
     - select use ssl, on smpt port enter 465
     - leave everything else on default 
     - lastly click on test configuration. if sucessful email should be sent then click apply and save.
