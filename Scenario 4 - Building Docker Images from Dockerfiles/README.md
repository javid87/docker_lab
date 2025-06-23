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

The home directory for the <User_Name> user will appear. If it doesn’t, click the **Home** button on the left side. Then, double-click the `workspace` folder, followed by the `flask_project` folder, and click the **Open** button in the top-right corner.

![Navigating to and opening the project folder](https://i.postimg.cc/BbWL5BMX/Screenshot-2025-06-23-164717.png)

After clicking **Open**, the `flask_project` folder will appear on the left-hand side. It contains two subfolders, a README file, a `requirements.txt` file, and a `Dockerfile` which you will modify later in this scenario. If you do not see the folder contents appear, click on the **Explorer** icon in the sidebar, which is the icon with the 2 pages on top of each other.

![Project folder open in Visual Studio Code](https://i.postimg.cc/yYsW-Vd54/scenario-4-visual-studio-with-project-open.png)

3.  The Flask website is located in the `website` folder. Click the `>` next to the `website` folder to expand its contents. The Flask application is in the `flask_website.py` file. Open this file.

    ![Opening the flask_website.py file](https://i.postimg.cc/0QGx3G96/Screenshot-2025-06-23-165046.png)

    This file initializes a new Flask application object on line 10 called `app`. Lines 15-22 define a route to the application's root URL (`/`), rendering the `index.html` file when the page is visited.

4.  The `index.html` file is located in the `templates` folder of the website. Click the `>` next to the `templates` folder and then open the file:

    ![Opening the index.html file](https://i.postimg.cc/cJhGBxhY/Screenshot-2025-06-23-165937.png)

    This webpage includes a header defined on line 1. On line 3, it inserts an image named `rick.png`, stored in the `static` folder within the `website` folder.

5.  The Flask application is run using Gunicorn. The configuration for the application is located in the `gunicorn_config.py` file inside the `website` folder. Open this file and review its contents.

    ![Opening the gunicorn_config.py file](https://i.postimg.cc/kgdrr6hK/Screenshot-2025-06-23-170100.png)

    * Line 4 defines the application to be run. `flask_website` is the name of the Python file that contains the Flask application and `app` is the name of the Flask application to execute.
    * Line 7 specifies the IP address and port where the application will run. In this case, it listens on all interfaces on port `8000`.
    * The remaining contents of the file define additional Gunicorn configuration parameters.

6.  There is also a `requirements.txt` file that contains the python package requirements for this application. It contains `Flask` and `gunicorn`.

7.  Finally, there is a `Dockerfile` with comments inside of it. You will modify this file later in this scenario.

### Running the Flask Web Application

1.  The other folder inside the `flask_project` folder, `flaskvenv`, is a Python 3.10 virtual environment with the application's required dependencies already installed. You will use this virtual environment to test the web application. In Visual Studio Code, click the **Terminal** button in the top toolbar, then select **New Terminal** to open a new Ubuntu terminal within Visual Studio Code.

When the Terminal opens, you should be inside of the flask_project directory:

![VS terminal](https://i.postimg.cc/9XdZtzqz/Screenshot-2025-06-23-173444.png)

If you're not already in this directory, use the following command in your Terminal to navigate to it:

```bash
cd Scenario\ 4\ -\ Building\ Docker\ Images\ from\ Dockerfiles/flask_project
```
2. Now activate the Python 3.10 virtualenv named flaskvenv with the following command:

```bash
source flaskvenv/bin/activate
```
After you enter this command you should now see (flaskenv) displayed to the left of the username in your Terminal. This indicates that you are currently running the Python virtual environment.

3. Inside of the Terminal change to the website directory
```bash
cd website
```

4. Run the web application using the gunicorn command and use the -c command line argument and specify the gunicorn configuration file
  ```bash
  gunicorn -c gunicorn_config.py
  ```
  P.S: if you use windows use: 
  ```bash
  waitress-serve --host 127.0.0.1 --port 8000 flask_website:app
  ```

  After entering this command you will see output appear in your Terminal. Look for the following output at the bottom, which indicates the web application is running on port 8000:
5. In the workstation, open a web browser and go to http://localhost:8000. You should see the following page, confirming that the website is working correctly:

![rick](https://i.postimg.cc/9MGb7bhQ/Screenshot-2025-06-23-174522.png)
