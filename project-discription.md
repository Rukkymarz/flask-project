 #  PROJECT DISCRIPTION
Create a Github repository to store the code and configuration files for the Flask web 
app

Sample code for the flask web app

```bash 
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
 return "I am almost a Devops Engineer!"
if __name__ == "__main__":
 app.run(host='0.0.0.0')
 ```

this should have the .py extension
please this should run on 2 servers using Jenkins
also add a webhook
make use of search engines to find out requirements for a flask application should work(you 
can try it on one server first, before deploying with Jenkins)
use any ec2 ami (amazon linux, centos, or ubuntu)
• Use Jenkins to automatically build, test and deploy the web app
• Use Ansible to automate the provisioning and configuration of the target 
deployment environment
Steps:
1. Create a Flask Web App: Write a simple Flask web app in Python, and 
save it as a .py file. You can start with the sample script I provided in the 
previous answer.
2. Create an EC2 instance: Log into the AWS Management Console and 
create an EC2 instance. Make sure that the instance is in a public subnet 
with a public IP address and a security group that allows incoming traffic 
on port 5000 (the default port for Flask).
3. Install Jenkins on the EC2 instance: Connect to the EC2 instance using 
SSH, and install Jenkins by following the installation instructions for your 
operating system.
4. Create a Jenkins Job: Log into the Jenkins web interface, and create a 
new job. Configure the job to clone your Flask web app repository from 
Github and build the application using the command python app.py.
5. Integrate Ansible with Jenkins: Install Ansible on the EC2 instance, and 
configure Jenkins to use Ansible as a deployment tool. You can do this 
by installing the Ansible plugin for Jenkins, and configuring the Jenkins 
job to run an Ansible playbook as a post-build step.
6. Create an Ansible Playbook: Write an Ansible playbook that provisions 
and configures the EC2 instance for your Flask web app. This playbook 
should include tasks to install required packages, configure the firewall, 
and start the Flask web app as a service.
7. Deploy the Flask Web App: Trigger the Jenkins job to build, test, and 
deploy your Flask web app. The job should clone the code from Github, 
build the application, and use Ansible to deploy the app to the EC2 
instance.
pdkf