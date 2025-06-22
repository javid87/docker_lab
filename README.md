# Introduction to Docker Lab

This repository contains the materials for a hands-on lab designed to introduce the fundamentals of Docker.

## 🎯 Learning Objectives
This lab introduces **Docker**, an open-source platform for creating, deploying, and running applications in isolated environments called **containers**. Containers package application code with all necessary libraries, dependencies, and settings. The instructions for building a **Docker image**, which serves as a blueprint for creating a Docker container, are specified in a `Dockerfile`.

Containers can run on any environment—Windows, Mac, or Linux—provided a container runtime, like Docker, is installed. In this lab, Docker is pre-installed for you. For installation at home, refer to the following links:
* [How to Install Docker Engine on Windows](https://docs.docker.com/desktop/install/windows-install/)
* [How to Install Docker Engine on Mac](https://docs.docker.com/desktop/install/mac-install/)
* [How to Install Docker on Linux](https://docs.docker.com/engine/install/)

---

## 🔬 Key Lab Focus Areas
In this lab, you will explore the following topics:

* Verifying that Docker is installed correctly
* Creating containers using Docker images from Docker Hub
* Introduction to common Docker CLI commands for managing containers and images
* Creating a `Dockerfile` for an existing application and building it into a Docker image

---

## ✨ Benefits of Docker
There are many benefits to using Docker and containers. Here are a few advantages:

#### Portability and Consistency
Containers ensure applications run consistently across various environments. There's no need to worry about installing libraries or operating system compatibility; just make sure Docker is installed. You can then download or build your image using a `Dockerfile` and seamlessly run it in a container.

#### Lightweight
The following diagram shows a virtual machine versus a container environment:

![Virtual Machine vs. Container Environment](https://i.imgur.com/SdaFPWb.png)

In a **virtual machine (VM)** environment, each VM has its own operating system and kernel, along with the application and its dependencies. VMs run on a hypervisor, which manages them. While VMs are more isolated than containers, their large size and need to boot a full OS make them resource-intensive and slow to start.

In contrast, **containers** on the same host share resources and the OS kernel, making them smaller, more resource-efficient, and faster to start, as they don't require booting a complete OS. The container runtime manages the lifecycle of containers, allowing many containers to run simultaneously on a host due to their reduced size.

---

## 📚 Common Docker Terms
Here are definitions of some common Docker terms you will see in this lab:

* **Image**
    > A Docker image is a read-only template that includes all of the files, binaries, libraries, and configurations needed to create a container. Multiple containers can be created from the same image. Once a Docker image is created, it cannot be modified. Instead, you can create a new image or layer changes on top of it to form a new image.

* **Container**
    > A Docker container is a running instance of a Docker image. Each container can have its own unique data and state and is isolated from other running containers.

* **Docker Engine**
    > The Docker Engine is the core component of the Docker platform, enabling the creation, management, and execution of containers. It consists of the following components:
    > * **Docker Daemon (`dockerd`):** A background process running on the host machine, responsible for managing Docker objects such as images and containers. It handles lifecycle operations like starting, stopping, and removing containers and images.
    > * **Docker CLI:** A command-line interface used to interact with the Docker Daemon for building, running, and managing containers.
    > * **REST API:** A programmatic interface to interact with the Docker Daemon, enabling automation and integration with other tools and systems.

* **Dockerfile**
    > A `Dockerfile` is a special text file containing instructions and commands to build a Docker image. Each instruction creates a new layer, and multiple layers are stacked to form the final image at the end of the build process.

* **Docker Hub**
    > Docker Hub is a cloud-based registry service provided by Docker for storing, sharing, and distributing Docker images. You can share images publicly or privately with authorized users. Alternatively, you can set up a local Docker registry to keep images within your company's infrastructure, particularly when data requirements restrict storing container images outside the organization.

---

## 🚀 Let's start  Getdiyeeee 🚀

---

### Disclaimer
> This lab is to familarize participants with the basics of Docker. For any design related questions please contact your representative at **Javid Alizada**