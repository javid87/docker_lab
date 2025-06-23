# Scenario 4 - Creating a Dockerfile for a Web Application

In this last scenario, you will learn to containerize an existing Flask web application by creating a Docker image and running it in a container. Flask is a lightweight framework for building Python web apps. This application runs on Gunicorn, a web server designed to handle Python applications by translating web requests into a format Python understands. Unlike Nginx, which supports various web applications, Gunicorn is specifically created for Python-based applications.

To create a Docker image for your application, you will create a **Dockerfile**, which is a text file containing instructions and commands to build the image. Each instruction creates a new layer, and multiple layers are stacked to form the final image at the end of the build process.

---

## Verify Flask Web Application Functionality

First, you will confirm that the existing web application functions correctly outside the Docker environment before creating a Docker image. This approach is the recommended best practice when developing Docker images.

### Review Flask Web Application Contents in Visual Studio Code

1.  On the workstation, open up the **Visual Studio Code Editor**. This can be found as shortcut on the Desktop, or as a shortcut on the sidebar.

    ![Visual Studio Code Icon](https://i.postimg.cc/X7GdCXLZ/Screenshot-2025-06-23-164325.png)

2.  The location of the Flask application you will be turning into a Docker container is located in the following folder: `/home/<your_usernae/<your_path>/flask_project`. After Visual Studio Code opens, click on **File -> Open Folder**.

    ![Visual Studio Code - Open Folder menu](https://i.postimg.cc/Ss1YXpz7/scenario-4-visual-studio-open-folder.png)