# Scenario 3 - Common Docker Commands

Now that you have run your first container and explored Docker Hub, you will now look at some important Docker commands used to manage the Docker environment. While there are many commands available, we'll cover some of the most common ones. For a complete list, you can visit the [Docker CLI Commands Reference Page](https://docs.docker.com/engine/reference/commandline/cli/).

---

## Docker Container Commands
These commands are used to manage containers on the host.

## `docker container ls`
This command displays the containers currently running on the host. You might also come across the `docker ps` command, which provides the same functionality. The `docker container <command>` structure was introduced later to standardize the Docker CLI syntax. If you're familiar with the Linux `ls` command, which lists directory contents, you'll notice this command serves a similar purpose, but specifically for Docker containers.

1.  Run `docker container ls` in your Terminal:
    ```bash
    docker container ls
    ```
OR old one
    ```bash
    docker ps
    ```

![Virtual Machine vs. Container Environment](https://i.postimg.cc/fWv5KZyb/Screenshot-2025-06-22-231943.png)

In this output, you'll see the `hello-world` and `nginx` containers you ran previously.
    Other key information includes:

* **Container ID:** A unique identifier assigned to each container, used for management.
* **Command:** The default command executed when the container starts. You can override this by specifying a command at the end of the `docker run` command.
* **Status:** Indicates the container's state, such as `Exited (0)` for both containers here. An exit code of `0` means the command executed successfully; other exit codes may indicate issues. If the container is running, you'll see `Running`. For more status details, refer to the `docker container ls` command reference page.
* **Name:** The container's name, which defaults to a random two-word phrase. To specify a name, use the `--name` argument, such as: `docker run --name my-hello-world-container hello-world`.

### `docker container [start|restart|stop|kill]`
These commands manage containers that have already been created:

* **Start:** Begin running a stopped container (`docker container start`).
* **Restart:** Stop and then start a container (`docker container restart`).
* **Stop:** Gracefully shut down a container (`docker container stop`).
* **Kill:** Immediately terminate a container, useful if it can't be shut down gracefully (`docker container kill`).

You'll need the container's ID for each command, obtainable via `docker container ls -a`. The Container ID is unique to your lab. For example, using the `nginx` container ID from the screenshot above (`1e1cf...`), start the container with: `docker container start 1e1cf`.

1.  Start your `nginx` container again using the `docker container start` command with your container's unique ID:
    ```bash
    docker container start <your_container_id>
    ```

2.  Verify that the container is running with:
    ```bash
    docker container ls
    ```
    ![docker container ls output after start](https://i.postimg.cc/c49pFfC6/Screenshot-2025-06-22-232527.png)

3.  Verify that the `nginx` website is avaiable again as well. In your web browser, navigate to [http://127.0.0.1:20000](http://127.0.0.1:20000).

4.  If you want, you can also go ahead and test out the other docker commands, but make sure the `nginx` container has been started before moving on.

### `docker container logs`
This command is used to view the logs for a container and can be executed regardless of the container's state (started, stopped, etc.). It's very useful for debugging purposes, allowing you to see what a container is or was doing. To use this command, you need the container ID of the container whose logs you want to view.

1.  In your Terminal, enter the `docker container logs` command with your `nginx` container's ID added at the end:
    ```bash
    docker container logs <your_container_id>
    ```
    ![docker container logs output](https://i.postimg.cc/k4JwrhhC/Screenshot-2025-06-22-232749.png)

### `docker container inspect`
This command provides detailed information about a container, including:
* Networking information
* The command and arguments used to start the container
* Container state

1.  Enter the `docker container inspect` command followed by the nginx's container ID to see what detailed info there is for your `nginx` container:
    ```bash
    docker container inspect <your_nginx_container_id>
    ```
    ![Virtual Machine vs. Container Environment](https://i.postimg.cc/3rcZPX6b/Screenshot-2025-06-23-150031.png)

### `docker container rm` and `docker container prune`
These commands remove stopped containers from your host to free up space. Periodically cleaning up containers helps prevent your host from running out of storage.
* **`docker container rm`**: Removes one or more specified containers.
* **`docker container prune`**: Removes **all** stopped containers.

1.  In your Terminal, enter `docker container ls -a` to view all containers on the host. Locate one of the `hello-world` containers from Scenario 1.
    ```bash
    docker container ls -a
    ```
    ```bash
    javid@sandbox:~$ docker container ls -a
    CONTAINER ID   IMAGE         COMMAND    CREATED         STATUS                     PORTS     NAMES
    cb9e4f16f9fb   hello-world   "/hello"   4 minutes ago   Exited (0) 4 minutes ago             laughing_aryabhata
    ```

2.  Execute `docker container rm` with the `hello-world` container's ID to remove it:
    ```bash
    docker container rm <hello-world_container_id>
    ```
    ```bash
    javid@sandbox:~$ docker container rm laughing_aryabhata
    laughing_aryabhata
    ```

3.  Before using `docker container prune`, stop the `nginx` container started earlier in this scenario:
    ```bash
    docker container stop <nginx_container_id>
    ```
    ```bash
    javid@sandbox:~$ docker container ls
    CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS                                     NAMES
    9b14a218fdf9   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:2000->80/tcp, [::]:2000->80/tcp   nginx
    javid@sandbox:~$ docker stop nginx
    nginx
    ```
4.  Enter the `docker container prune` command. You'll be prompted to confirm the removal of all stopped containers. Enter `y` to confirm. A message will confirm space has been reclaimed.
    ```bash
    docker container prune
    ```
    ```bash
    javid@sandbox:~$ docker container prune
    WARNING! This will remove all stopped containers.
    Are you sure you want to continue? [y/N] y
    Deleted Containers:
    9b14a218fdf99446ffa4f304481b21d5e4d36703dbdaadbac89783cc9d0a5c70

    Total reclaimed space: 1.095kB
    ```
5.  Use `docker container ls -a` again to confirm all containers have been removed from the workstation:
    ```bash
    docker container ls -a
    ```
    ![Virtual Machine vs. Container Environment](https://i.postimg.cc/mgbKmxnG/Screenshot-2025-06-23-151059.png)

---

## Docker Image Commands
Now that you've learned about some common commands for managing Docker containers, let's explore commands used to manage Docker images on the host. You'll notice these commands serve similar functions to the Docker container commands, but they focus on Docker images.

### `docker image ls`
This command lists the current Docker images on the host.

1.  Run the `docker image ls` command on your workstation:
    ```bash
    docker image ls
    ```
    ![Virtual Machine vs. Container Environment](https://i.postimg.cc/7h8W7jzd/Screenshot-2025-06-23-151209.png)

    You should see the `nginx` and `hello-world` images you have used previously. One thing to note with this command, is that if you have multiple tags for the same image, you may see multiple entries for that image.

### `docker image pull`
You've used the `docker pull` command in previous scenarios. It serves as a shorthand for `docker image pull`, which aligns with the updated Docker CLI structure. Both commands function identically, allowing you to download images from a registry, such as Docker Hub.
```bash
docker image pull ghcr.io/sweickge/nginx:1.26.3
```
~[docker image pull](https://i.postimg.cc/qMG5hbvD/Screenshot-2025-06-23-151405.png)

### `docker image build`
This command is used to build a new image from a `Dockerfile` on your local host. You will learn more about this command in the next scenario, when you create a `Dockerfile`.

### `docker image tag`
This command creates a new tag for an existing image. Tagging allows you to reference the same image with multiple identifiers, making it easier to organize, manage, and push images to container registries such as Docker Hub. The syntax is:
docker image tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]

* `SOURCE_IMAGE` is the image that you want to create a new tag for; you can optionally specify the tag as well.
* `TARGET_IMAGE` is the new name and tag you want to give the image.

1.  In your Terminal, create a new tag for the `ghcr.io/sweickge/nginx:1.26.3` you downloaded previously, naming it `prod_nginx:1.0`:
    ```bash
    docker tag ghcr.io/sweickge/nginx:1.26.3 prod_nginx:1.0
    ```
    You won't see any output when you run this command.

    ![docker tag](https://i.postimg.cc/7hnmzhwJ/Screenshot-2025-06-23-151712.png)

2.  Verify the image has been created with the `docker image ls` command:
    ```bash
    docker image ls
    ```
    *[Здесь будет скриншот со списком образов, включая новый тег]*

    You'll notice both the `nginx:1.26.3` image and the `prod_nginx:1.0` image have the same image ID. This is expected because you created a new tag for the nginx image without altering its content. When two images share the same image ID, they are identical in content, and Docker manages them efficiently by storing only one copy while allowing you to reference them through different tags and repository names.

### `docker image inspect`
This command displays detailed information about a specific image.

1.  In your Terminal, run the following command to view the detailed info about the `nginx:1.26.3` image:
    ```bash
    docker image inspect ghcr.io/sweickge/nginx:1.26.3
    ```
    *[Здесь будет скриншот с подробной информацией об образе]*

### `docker image rm` and `docker image prune`
These commands remove images from your host to free up space, helping prevent storage issues with periodic cleanups:
* **`docker image rm`**: Removes one or more specified images.
* **`docker image prune`**: By default, removes all **dangling images**, which are untagged images not associated with any existing containers. If you want to remove **all unused images** (both tagged and untagged), you need to add the `-a` option.

> It's important to note that if a container on the host is using an image you're trying to remove, Docker will prevent its removal until those containers are stopped and removed. Since you previously ran `docker container prune` to clean up all existing containers, it is safe to remove the images now.

1.  Use the `docker image rm` command to remove the `hello-world` image:
    ```bash
    docker image rm hello-world
    ```

2.  Verify the image has been removed:
    ```bash
    docker image ls
    ```

3.  Finally, remove the remaining images on the workstation using the `docker image prune -a` command. You'll be prompted to confirm the removal. Enter `y` to proceed. A message will confirm that space has been reclaimed.
    ```bash
    docker image prune -a
    ```
    You'll notice some extra images being removed in this output. These are extra image layers that were used to create the final `nginx` image.

---

## Conclusion
In this scenario, you learned fundamental commands for managing Docker containers and images. You learned how to create, start, stop, and remove containers, as well as how to inspect and look at their logs. Additionally, you learned about image commands to list, tag, and prune images, ensuring efficient space management and organization of your Docker environment. These foundational skills will allow you to utilize Docker in future development and deployment scenarios. In the final scenario, you will learn how to turn an existing application into a Docker image that can be deployed in a container environment.