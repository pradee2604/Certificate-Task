"Task lists"




"Task 1

Create a VPC with 2 subnets (public and private) in different AZs, attach an internet gateway, and launch EC2 instances. 
Try to access the private instance through the instance in public subnet (Clue:- using SSH)




Task 2

Create 2 VPC's Named Webapp-VPC & Db-VPC
It should have 2 Subnets each, one with Class A IPv4 CIDR and Class B IPv4 CIDR and 255 ports in each subnet.


Task 3

Associate an Elastic IP to an EC2 Instance using Terra-form 
- Create an ec2 instance using terra-form workflow
- Associate an elastic IP


Task 4

Configure ec2 linux machine and install apache configuration
Screenshot:


Task 5

Creating a Basic Amazon S3 Lifecycle Policy
- Create an S3 Bucket and Upload an Object
- Create a Lifecycle Policy - Create a lifecycle policy that moves objects to Glacier Flexible Retrieval (formerly Amazon Glacier) if they haven't been accessed in the last 30days.


Task 6

Create and configure an S3 bucket: Create a new Amazon Simple Storage Service (S3) bucket and configure it for static website hosting. Then, upload a sample HTML file and ensure that it can be accessed through a web browser.



Task 7

Host a static website in S3
        	-> create a s3 bucket with private access ..
        	-> Note : bucket should not be Public access
        	-> ADD the objects -> like front-end code eg: index.html
        	-> create the Cloud Front (CDN- Content Delivery Network )
        	-> now you need to Redirect the traffic from Cloud-Front to s3 bucket
    	-> copy the distribution id of the cloud-front . check in any Browser . website should appear.


Task 8


Set up Cross-Region S3 Bucket Replication
           - Create an S3 Bucket and Enable Replication
           - Test Replication and Observe Results


Task 9

Create a Staging branch in GitHub and push code from the local repository to the Remote and share the full commands screen


Task 10


Implement Auto Scaling: Create an Auto Scaling group that automatically launches new EC2 instances based on predefined rules. You can use the EC2 instance that you created in Task 1 as the base instance for the Auto Scaling group. Test the Auto Scaling group by simulating a surge in traffic to the web server.


Task 11

Configure a Load Balancer: Set up an Elastic Load Balancer (ELB) that distributes incoming traffic to the EC2 instances in your Auto Scaling group. Configure health checks to ensure that the ELB only forwards traffic to healthy instances.


Task 12

Creating a Custom Amazon Machine Image (AMI)
- Launch a New EC2 Instance
- Install http on the new instance, enable the http service to start at boot.
- Create a New AMI from customized instance and name the AMI MicroDegreeWeb
- Launch a New Instance Using the Custom AM
- Verify that http is running.


Task 13
Web Application:
●	Develop a simple "Hello World" web application (you can use any programming language or framework of your choice).
●	Package the application into a deployable artifact (e.g., a JAR file, Docker image).


Task 14

Create a sample Jenkins CICD pipeline and share output logs and pipeline script
Upload the final output Screenshot


Task 15

Create a docker service with image "tomcat", name "HTTP", port 80


Task 16

Creating an IAM User and Assigning Permissions:

Click on "Users" in the left-hand menu and choose "Add user."
Provide a username and select the access type (programmatic access, AWS Management Console access, or both).
Set permissions by adding the user to one or more IAM groups with predefined policies or by attaching custom policies directly.


Task 17

Create a deployment strategy for a containerized application. Choose a container orchestration platform such as Kubernetes or Docker Swarm, and design a deployment process that includes blue-green deployments or canary deployments. Outline the steps required to roll out new versions while minimizing downtime and ensuring service availability.



Task 18

Setting Up Continuous Integration and Deployment (CI/CD):
Jenkins is often used for implementing CI/CD pipelines to automate the build, test, and deployment processes. Create a pipeline job using Jenkins Pipeline DSL (declarative or scripted) or a Jenkins file.
Define the stages of your pipeline, including building, testing, code analysis, and deployment.
Configure Jenkins to trigger the pipeline based on code changes, commits, or other events.

Task 18.1


Setting up a Continuous Integration (CI) Pipeline: Configure a CI pipeline using tools like Jenkins, CircleCI, or AWS CodePipeline to automate the building, testing, and deploymentof your application code whenever changes are pushed to the repository.



Task  19


Working with Docker Images
- Pull the latest `httpd` image.
- Pull the latest `alpine` image.
- verify images pulled and create 2 containers in each server



Task 20

Ceate a basic deployment pipeline that deploys your application to different environments, such as development, staging, and production. Implement testing and approval steps for each environment.


Task 21 

Build a custom docker image using Ubuntu as a base docker image and run the nginx application. 
This docker image should be built using a Dockerfile. Once the docker image is build, start the docker image using the host network and make it accessible on Public IP


Task 22

Creating a Docker Compose Configuration:
Write a Docker Compose YAML file (docker-compose.yml) to define a multi-container application setup.
Specify the services, their configurations, and any necessary links or dependencies between containers.
Use the docker-compose up command to start the containers defined in the Docker


Task 23

Exposing an Application with a Service:
Create a YAML file (service.yaml) that defines a Service to expose your application.
Specify the Service type (e.g., LoadBalancer, NodePort, ClusterIP), ports, and target selectors.
Apply the Service to the cluster using kubectl apply -f service.yaml.
Access the exposed application using the appropriate service endpoint (e.g., LoadBalancer external IP, NodePort, ClusterIP).
Upload the final output Screenshot


Task 24

Configure email notifications
Description: Configure Jenkins to send email notifications when a build fails.
Instructions:




    "Scenario based questions"

1 Scenario : You have a running process that is consuming a lot of system resources and needs to be terminated. How would you find the process ID (PID) of the process and terminate it gracefully?

2 Scenario : You are using a computer with a single-core processor. You have multiple applications open, including a web browser, a text editor, and a media player. The media player freezes and becomes unresponsive. Explain the potential reasons behind this issue and suggest a possible solution.

3 Scenario : A user reports that they are unable to access a website by its domain name, but other websites are working fine. What steps would you take to troubleshoot and resolve this issue from the DNS perspective?

4 Scenario : Infrastructure as Code
Your team is managing infrastructure using Infrastructure as Code (IaC) principles. How would you use AWS CloudFormation to provision and manage resources? Provide an example of a CloudFormation template that creates an Amazon S3 bucket and an Amazon DynamoDB table.

5 Scenario : You are deploying a web application on AWS. How would you set up an automated deployment pipeline using DevOps principles?
Question: What steps would you take to implement continuous integration and continuous deployment (CI/CD) for your web application on AWS?

6 Scenario : Your team is working on an application that requires scalability and high availability. How would you architect the application using AWS services and Dev-Ops best practices ?  
 Question : Explain how you would design an architecture that leverages AWS services to ensure scalability and high availability for your application, following Dev-Ops principles.

7 Scenario : Your application needs to process and analyze streaming data from various sources. Which AWS service can you use for real-time data streaming and analytics?



"
