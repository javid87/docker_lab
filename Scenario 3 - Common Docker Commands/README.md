# Scenario 3 - Common Docker Commands

Now that you have run your first container and explored Docker Hub, you will now look at some important Docker commands used to manage the Docker environment. While there are many commands available, we'll cover some of the most common ones. For a complete list, you can visit the [Docker CLI Commands Reference Page](https://docs.docker.com/engine/reference/commandline/cli/).

---

## Docker Container Commands
These commands are used to manage containers on the host.

### `docker container ls`
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