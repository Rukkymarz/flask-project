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

