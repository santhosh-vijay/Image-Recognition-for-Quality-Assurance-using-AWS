# Image-Recognition-for-Quality-Assurance-using-AWS
The requirements for this project is as follows:
An image recognition startup is in the process innovating their inspection process which has been completely manual to this point. Inspectors take pictures of random objects to ensure that the they are within compliance standards set by the Quality Assurance Group.

In order to ensure that the process meets or achieves standards, the following manual process is currently used:

- A digital picture of the object is taken 
- The image is analyzed by the inspector to determine if it is the right object and meets quality requirements
- Once the inspection is complete, a message is sent to the Quality Control group with the results of the inspector's analysis
- The results are also stored with the image in an "inspected" folders in the event the analysis results and image need to be reviewed
- The original images as well as the analysis results are stored for compliance purposes for 3 years

The objective of this new project is to automate and innovate the existing process. The company has decided to create an AWS serverless architecture that has the following requirements:

- The current manual inspection process must be as automated as possible (fully automated)
- The design and implementation must be serverless and leverage AWS best practices architecture
- The inspection process will be automated using AWS image recognition services
- The architecture/implementation will be completely event based starting with the presence of the digital image from the assembly line (assume that there is a camera on the assembly line that is able to take images and store them in the cloud)

The solution is implemented thorugh AWS well-architected framework and cloud best practices which can be found on the report file.
