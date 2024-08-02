# LMS Project - Fonctionnalité de Formation de Groupes

## Description

Ce projet consiste à ajouter une fonctionnalité de formation de groupes à un LMS (Learning Management System). La fonctionnalité permet aux formateurs de créer des groupes d'apprenants aléatoirement en fonction des noms saisis et du nombre de groupes souhaité.

## Fonctionnalités

- **Formulaire de saisie des apprenants :** Le formateur peut entrer les noms et prénoms des apprenants.
- **Définition du nombre de groupes :** Le formateur spécifie le nombre de groupes à créer.
- **Génération des groupes :** Un bouton permet de former les groupes aléatoirement.
- **Affichage des groupes :** Les groupes sont affichés en dessous du formulaire après la génération.

## Technologies Utilisées

- **Backend :** Django
- **Base de données :** SQLITE3
- **Suivi des erreurs :** Sentry
- **Conteneurisation :** Docker
- **CI/CD :** GitHub Actions
- **Déploiement :** Render

## Installation

### Prérequis

- **Docker**
- **Docker Compose**

## Installation

1. Clone the repository:
````
git clone https://github.com/BFCraftCode/lms_project.git
````
2. Create a virtual environment and activate it:
````
python -m venv venv 
source venv/bin/activate  # On Windows: venv\Scripts\activate
````
3. Install dependencies:
````
pip install -r requirements.txt
````
4. Run the Application:
````
cd lms_project
````
````
python manage.py runserver
````
## Tests and reports

1. Running Tests with pytest:
````
pytest
````
To generate an HTML report:
````
pytest --html=pytest_report.html
````
2. Generating Code Coverage Report:
````
coverage run -m pytest
````
Generate the coverage report:
````
coverage html
````
Access the HTML coverage report in the htmlcov directory.

3. Linting:
````
flake8.
````

## CI/CD Pipeline

This project includes a CI/CD (Continuous Integration/Continuous Deployment) pipeline that automates the testing, building, and deployment processes. The pipeline is configured using GitHub Actions.

### Workflow Overview

The CI/CD workflow consists of the following main steps:

1. **Check:** Runs testing, linting and code quality checks.

2. **Build:** Builds and tags the Docker image, then pushes it to Docker Hub.

3. **Deploy:** Triggers the deployment process, such as updating a Render web service.

### Setting Up CI/CD

To set up the CI/CD pipeline for this project, follow these steps:

1. **Fork the Repository:** Fork this repository to your GitHub account.

2. **Configure Secrets:** Go to your forked repository's settings and configure the following secrets:
   - `DOCKER_USERNAME`: Your Docker Hub username.
   - `DOCKER_PASSWORD`: Your Docker Hub password.
   - `SECRET_KEY`: Django secret key.
   - `DEPLOY_HOOK`: Your deployment webhook (if applicable).

3. **Run the Pipeline:** Push changes to your repository, and GitHub Actions will automatically run the CI/CD pipeline.

### Workflow File

The CI/CD workflow is defined in the [`.github/workflows/main.yml`](.github/workflows/main.yml) file.

### Important Notes

- Ensure that your Docker Hub repository and Render service are set up correctly.
- Monitor the CI/CD workflow on the Actions tab in your GitHub repository.

Feel free to customize the pipeline based on your specific requirements and deployment environment.

## Deployment

### Overview

This project is deployed using Docker and hosted on Render. Docker Hub is used to store and manage Docker images, while Render provides a platform for easy deployment and hosting.

### Configuration

To deploy this project, ensure you have the following configurations in place:

1. **Docker Hub Account:**
   - Create an account on Docker Hub: [Docker Hub](https://hub.docker.com/).

2. **Render Account:**
   - Create an account on Render: [Render](https://render.com/).

3. **GitHub Repository:**
   - The project should be hosted on GitHub.

### Deployment Steps

Follow these steps to deploy the project:

1. **Build Docker Image:**
   - Make sure your Docker image is ready and available on Docker Hub.

2. **Configure Render:**
   - Create a new web service on Render.
   - Link your GitHub repository to Render for automatic deployments.
   - Set up environment variables on Render for any sensitive information or configuration needed by your application.

3. **Configure Docker Image on Render:**
   - In the Render dashboard, specify the Docker image from Docker Hub that you want to deploy.
   - Set the necessary environment variables for your application within the Render dashboard.

4. **Deploy the Service:**
   - Trigger a manual deployment or wait for Render to automatically deploy your application whenever changes are pushed to the linked GitHub repository.

5. **Access the Deployed Application:**
   - Once the deployment is complete, access your application on the provided Render URL.

### Notes

- Ensure that your Docker image includes all the necessary dependencies and configurations for the application to run smoothly in a production environment.
- Regularly check the Render dashboard for deployment logs and updates.
- Refer to the [Render documentation](https://render.com/docs) for more detailed information on managing services and deployments.

**Congratulations!** Your application is now deployed and accessible via the provided Render URL.

---

Feel free to customize the steps and details based on your specific project requirements and deployment process.

