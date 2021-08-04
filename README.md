# Smart City

Code repository for the Smart City team for Yeshiva University's Industrial Software Development Summer Project. Created in Summer 2021 by [Nir Solooki](https://www.linkedin.com/in/nir-solooki-018702204/), [Ephraim Crystal](https://www.linkedin.com/in/ephraim-crystal-429a8020a/), [Max Friedman](https://www.linkedin.com/in/max-friedman-98a77a205/), and [Meir Jacobs](https://www.linkedin.com/in/jordan-meir-jacobs/), under the guidance of [David Rosenstark](https://www.linkedin.com/in/david-rosenstark-3b070b8/).

## About
We built a deployable Smart City Reporting System. Using AWS, we created a system that allows users to report and query issues in a city. We then used Spring Boot to create a web application built on our AWS system that allows both regular users and city employees to easily add, update, and query information. Finally, we used Docker to create an executable file that anyone can pull and run.\
For more details, please take a look at our [slideshow](https://docs.google.com/presentation/d/1FifAM7bcKuk-KgVGY6ksQmhvsuYZ_ZC_haIsi3fixUU/edit?usp=sharing). Click "Present" on the top right for the most ideal viewing experience.

## Steps for Deployment

Prerequisites: 
- AWS Account with appropriate permissions and sufficient credits
- Gmail account
- Docker desktop app installed

Steps:
1. Create an [S3 Bucket](https://s3.console.aws.amazon.com/s3/home) with the default settings. Copy the name of the bucket for the next step.\
Download [lambdas.zip](https://github.com/meirjacobs/Smart-City/blob/main/CloudFormation/lambdas.zip) and [mysql_layer.zip](https://github.com/meirjacobs/Smart-City/blob/main/CloudFormation/mysql_layer.zip) and add them to the bucket.

2. Create a [CloudFormation Stack](https://console.aws.amazon.com/cloudformation/home) with the [Smart City template](https://github.com/meirjacobs/Smart-City/blob/main/CloudFormation/smart_city_template.yml).\
Follow the instructions in the 'Parameters' section.

3. Wait about 10 minutes for the Stack to finish deploying.

4. Open a command line and run\
`docker run -p 8080:8080 -e API_URL=api_gateway_link -e SPRING_DATASOURCE_URL=jdbc:mysql://database_link:3306/Smart_City -e SPRING_DATASOURCE_PASSWORD="password" ecrystal/smart_city_repository:latest`, but replace `api_gateway_link` with the Invoke URL to your API Gateway, `database_link` with your database hostname, and `password` with your database password (see below for assistance).
    * To find the URL to your API Gateway, visit the [API Gateway Console](https://console.aws.amazon.com/apigateway/main/apis) and click SmartCityAPIGateway. On the left of the screen, click Stages. Click deployedStage. The URL next to Invoke URL is what you need.
    * To find the hostname and password to your database, visit the [Secrets Manager Console](https://console.aws.amazon.com/secretsmanager/home), select MySQL-Credentials, scroll down a little and click "Retrieve secret value." You should see key-value pairs for "host" and "password."

5. Open your browser of choice, visit [localhost:8080](https://localhost:8080), and enjoy.