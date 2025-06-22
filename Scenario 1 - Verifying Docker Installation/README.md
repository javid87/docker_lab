# Scenario 1 - Verifying Docker Installation

## Verifying Docker Installation
Before running or building any Docker containers, you need to verify that Docker has been installed correctly and is currently running on the workstation.

1.  Open up the **Terminal** program on the Docker Workstation to open up a Linux command prompt. This can be found as a shortcut on the Desktop or on the sidebar. Or, if you use Windows, open the **WSL terminal** or **Git-Bash terminal**.
    <br>
    Once open, enter the `docker` command:

    ![Docker command help output](https://i.imgur.com/ehARDme.png)

    This command launches the Docker command-line interface (CLI), which is the main tool for interacting with your Docker environment. One of the benefits of the Docker CLI is its consistency across different operating systems, including Windows, Mac, and Linux.

2.  Next, verify the version of the Docker CLI that is currently installed using the following command:
    ```bash
    docker --version
    ```
    You should see the following output:

    ![Docker version output](https://i.imgur.com/b5ngNyU.png)

    Based on the output, Docker version `28.0.1` is installed on the workstation.

3.  Now you need to verify that the Docker daemon is currently running. In the same Terminal window, enter the `docker info` command. If successful, you will see output similar to this:
    ```bash
    docker info
    ```
    ![Virtual Machine vs. Container Environment](https://www.guru99.com/images/1/101818_0504_DockerTutor9.png)

    Pay particular attention to the `Server` section, which provides details about the Docker environment. Key information includes:
    * The total number of Docker containers on the system, with counts of running, stopped, and paused containers.
    * The total number of Docker images available on the workstation.
    * The installed version of the Docker server (27.5.1 in this example).
    * The CPU and memory resources available for Docker to use.

    This is a fresh Docker installation, so you’ll notice that there are no containers or images on the workstation yet.
    If the Docker daemon was not running, the `Server` section will display an error message indicating that it cannot connect to the daemon:
    
    ![Virtual Machine vs. Container Environment](https://cdn.appuals.com/wp-content/uploads/2020/09/Docker-connectionn-error-1.png.webp)

    To resolve this, you would need to start the Docker daemon using the appropriate method for your operating system. On Ubuntu, you can use the command:
    ```bash
    sudo systemctl start docker
    ```
    However, since the Docker daemon is already running on this workstation, there’s no need to execute this command.

---

## Running Your First Image
With Docker installed and running, you can now run your first Docker image. You'll create a new container using the `hello-world` image, which serves as a test to verify your connection to Docker Hub. Running this image is an excellent initial step after installing Docker in a new environment.

1.  For this step you will be using the `docker run` command. The `docker run` command is used to create and run a new container from a Docker image. You will learn more later on in the lab about how you can find different images you can use.
    <br>
    Inside of your Terminal window, enter and run the following command:
    ```bash
    docker run ghcr.io/sweickge/hello-world
    ```
    You should see the following output:

    ![Virtual Machine vs. Container Environment](https://i.postimg.cc/xTv3yvnd/Screenshot-2025-06-22-224416.png)