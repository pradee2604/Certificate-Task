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






"
