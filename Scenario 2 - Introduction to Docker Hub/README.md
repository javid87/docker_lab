# Scenario 2 - Introduction to Docker Hub

In Scenario 1, you created a new container using the `hello-world` image. Since the image wasn't present on the workstation, Docker downloaded it from Docker Hub. **Docker Hub** is a cloud-based registry service provided by Docker for storing, sharing, and distributing Docker images. You can share images publicly or privately with authorized users. Alternatively, you can set up a local Docker registry to keep images within your company's infrastructure, particularly when data requirements restrict storing container images outside the organization.

In this scenario, you will learn more about Docker Hub, including how to find and download images that can serve as starting points for building your own images and containers.

---

## Navigating the Docker Hub Website

1.  On your workstation, open one of the provided web browsers (Chrome or Firefox), available on the sidebar or as desktop shortcuts, and navigate to the Docker Hub homepage: [https://hub.docker.com/](https://hub.docker.com/).

    You should be brought to a page that looks like this:

    ![Docker Hub Homepage](https://i.postimg.cc/dv53ZptQ/scenario2-docker-hub-homepage.png)

    > As a best practice, when selecting a Docker image from Docker Hub, opt for images with the **'Docker Official Image'** or **'Verified Publisher'** tags, unless the image is from a trusted site or developer you are familar with. These verified images are created by developers vetted by Docker to ensure high quality, adherence to Docker guidelines, and regular updates to address security issues and bug fixes. Using images from unknown developers may expose you to significant security risks or malicious code.

2.  Scroll down and click on the **Docker Official Image** link under the **Trusted Content** section.

    ![Clicking Docker Official Image](https://i.postimg.cc/7xNGs6D0/scenario2-docker-hub-official-image-click.png)

    On the page, you'll find various software options that you may already be familiar with, such as Python, the nginx web server, databases like PostgreSQL and MySQL, and operating systems like Ubuntu.

3.  Click on the result for **nginx**. If you are having trouble finding it, here is the direct link to the nginx image page: [https://hub.docker.com/_/nginx](https://hub.docker.com/_/nginx)

    ![NGINX page on Docker Hub](https://i.postimg.cc/g0M0Yxk7/scenario2-docker-hub-nginx-page.png)

    On this page, you'll find important information about the image, which may vary depending on the specific image you're viewing on Docker Hub:

    * **Image Download Command:** In the top right corner, you'll see the command to download the image to your workstation: `docker pull nginx`. The `docker pull` command is used to download an image from Docker Hub without running it immediately in a new container.
    * **Supported tags and respective Dockerfile links Section:** This section lists the various tags available for the image. A **tag** specifies a specific version or variant of the Docker image. If no tag is specified, Docker defaults to the `latest` version. Specifying a tag ensures you know the exact version of the container you're using. Clicking on a tag redirects you to a page showing the `Dockerfile` used to build that version. A `Dockerfile` contains the instructions for building an image, detailing what was added or executed to create it. You'll learn more about Dockerfiles in a later scenario.
    * **Scrolling further down,** you'll find instructions for using the nginx image, including instructions for incorporating it into your own `Dockerfile`. The documentation for this may vary depending on the developer and the specific image.

---

## Using a Docker Image from Docker Hub

1.  Pull the `nginx` image to your workstation. This time, instead of using the `latest` image as you did with the `hello-world` image, you'll use version **1.26.3** of the nginx image. To specify a specific tag for an image, use the following syntax for your `docker pull` command: `docker pull <image_name>:<tag>` (note the colon between the image name and tag).

    > **Note:** In this pull command, you'll notice the prefix `ghcr.io/sweickge/` before the nginx image name. This indicates that the image is being downloaded from the GitHub Container Registry rather than the default public Docker Hub, similar to how the `hello-world` image was retrieved earlier.
    ```bash
    docker pull ghcr.io/sweickge/nginx:1.26.3
    ```
    You should see output similar to this, and it may take a few seconds for the image to download:

    ![Pulling NGINX image output](https://i.postimg.cc/MGtnvstd/Screenshot-2025-06-22-230806.png)

    * The first line shows the specific tag being pulled and its source.
    * The lines that say "Pull complete" indicate the image layers being downloaded. A Docker image consists of multiple layers stacked to form the final image.
    * The last few lines display the checksum of the image, the download result, and the full image name for running or using it in a `Dockerfile`.

2.  Now create a new container using the `nginx` image. Before doing so, it's important to understand a key Docker concept called **port publishing**. By default, containers are isolated and cannot be accessed from outside the Docker environment.

    To access the container from the host, you need to set up a port mapping between the host and the container. You can achieve this by adding the `-p` or `--publish` option to your `docker run` command. Here's the syntax:
    ```
    docker run -p HOST_PORT:CONTAINER_PORT <image_name>
    ```
    * `HOST_PORT` = The port number on your host that you want to access the container on.
    * `CONTAINER_PORT` = The port number on the container that you want to access.
    
    If the `HOST_PORT` number is the same as the `CONTAINER_PORT` number you can shorten the `-p` argument to this:
    ```
    docker run -p PORT_NUMBER <image_name>
    ```
    For the `nginx` container, the `CONTAINER_PORT` will be port **80**, as that is the well known port for HTTP. For the `HOST_PORT` you need to choose a port that is not in use. Go ahead and choose **20000** for this.

    This is the full command you would enter into your Terminal:
    ```bash
    docker run -p 20000:80 ghcr.io/sweickge/nginx:1.26.3
    ```
    In your Terminal, you should see several messages appear, followed by the prompt waiting, indicating the nginx server is now running.

    ![Running NGINX container output](https://i.postimg.cc/pXYhwX8w/Screenshot-2025-06-22-231035.png)

3.  In your web browser on the workstation, open a new tab and navigate to: [http://127.0.0.1:20000](http://127.0.0.1:20000).

    You should see the nginx welcome page, indicating that the nginx server running in the Docker container is accessible. If you check the Terminal window running Docker, you'll see messages confirming that a connection was made to the container.

    ![NGINX welcome page in browser](https://i.postimg.cc/43hJTBqY/Screenshot-2025-06-22-231150.png)

4.  To wrap up this scenario, stop the nginx Docker container. In the Terminal window showing the container's output, press **Ctrl-C** to stop it. This will bring you back to the Terminal prompt.

---

## Conclusion
In this scenario, you explored Docker Hub and examined the `nginx` image page, learning about the available information. You downloaded a specific version of the `nginx` image using a Docker tag, created a container from it, and verified its functionality by successfully accessing the nginx welcome page in your browser. Navigating Docker Hub and utilizing its resources are important skills for managing and building your own images. In the next scenario, you'll learn about some common Docker commands that are used to manage containers and images on a Docker host.