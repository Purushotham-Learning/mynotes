# 🚀 Production-Grade GitHub Actions Self-Hosted Runners in Docker

This project allows you to run **secure, scalable, production-grade GitHub Actions runners** using Docker containers on your own infrastructure (local, cloud, or on-prem).

---

## ✅ Key Features

* 🐳 **Dockerized GitHub Actions runners**
* 🛡️ Runs as a **non-root user**
* 🔐 Auto **registers & deregisters** with GitHub
* ⚙️ Supports **custom labels**
* ⚡ Built-in support for **`.env` variables**
* 📈 Easy scaling with `docker-compose`

---

## 📁 Project Structure

```
github-actions-runner-docker/
├── Dockerfile               # Runner container image
├── entrypoint.sh            # Bootstrap script
├── docker-compose.yml       # Runner service definition
├── .env                     # Runner config via environment
```

---

## 🔧 Step-by-Step Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/github-actions-runner-docker.git
cd github-actions-runner-docker
```

---

### 2️⃣ Generate a GitHub Registration Token

> Go to: **GitHub → Settings → Actions → Runners → Add Runner**
> Copy the `registration token` (not the PAT)

---

### 3️⃣ Configure `.env`

Create a `.env` file in the project root:

```env
REPO_URL=https://github.com/your-username/your-repo-name
REG_TOKEN=ghs_XXXXXXXXXXXXXXXXXXXXXXXXXXXX
RUNNER_NAME=custom-runner-1
RUNNER_LABELS=self-hosted,docker,build,prod
```

> 🍿️ You can define any **custom labels** like `test`, `gpu`, `ci`, etc.

---

### 4️⃣ Build and Run with Docker Compose

```bash
docker-compose up -d --build
```

---

## 🐋 Dockerfile

```Dockerfile
FROM ubuntu:22.04

ENV RUNNER_VERSION=2.317.0

RUN apt-get update && \
    apt-get install -y curl jq git sudo unzip libicu70 ca-certificates && \
    apt-get clean

RUN useradd -m runner
WORKDIR /home/runner
USER runner

RUN curl -o actions-runner.tar.gz -L \
    https://github.com/actions/runner/releases/download/v${RUNNER_VERSION}/actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz && \
    tar xzf actions-runner.tar.gz && rm actions-runner.tar.gz

COPY --chown=runner:runner entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
```

---

## 💥 entrypoint.sh

```bash
#!/bin/bash
set -e

if [[ -z "$REPO_URL" || -z "$REG_TOKEN" ]]; then
  echo "❌ REPO_URL and REG_TOKEN must be set"
  exit 1
fi

echo "🔧 Configuring runner for $REPO_URL"

./config.sh \
  --url "$REPO_URL" \
  --token "$REG_TOKEN" \
  --name "${RUNNER_NAME:-$(hostname)}" \
  --labels "${RUNNER_LABELS:-self-hosted,docker}" \
  --unattended \
  --replace

cleanup() {
  echo "🧹 Removing runner..."
  ./config.sh remove --unattended --token "$REG_TOKEN"
}
trap cleanup INT TERM

echo "🌟 Starting runner..."
./run.sh
```

---

## ⚙️ docker-compose.yml

```yaml
version: '3.8'

services:
  github-runner:
    build: .
    container_name: github-runner
    env_file:
      - .env
    restart: always
```

---

## 🧪 Sample GitHub Workflow

Create `.github/workflows/docker-runner-test.yml` in your repo:

```yaml
name: Test Docker Runner

on: [push]

jobs:
  docker-job:
    runs-on: [self-hosted, docker, build, prod]
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Say Hello
        run: echo "👋 Hello from your Docker-based runner!"
```

> 🧠 The `runs-on` block must match your runner’s **custom labels**.

---

## 🚩 Cleanup

```bash
docker-compose down
docker image rm github-actions-runner
```

---

## 🛡️ Best Practices

| Best Practice       | Implemented | Description                              |
| ------------------- | ----------- | ---------------------------------------- |
| ✅ Non-root user     | Yes         | Runner uses `runner` user                |
| ✅ Auto-registration | Yes         | Register at container start              |
| ✅ Auto-cleanup      | Yes         | Deregister on shutdown                   |
| ✅ Custom labels     | Yes         | Use `RUNNER_LABELS` in `.env`            |
| ✅ Portable config   | Yes         | Use `.env` and `docker-compose`          |
| ✅ Scalable          | Yes         | Run multiple containers or use Swarm/K8s |

---

## 💬 Common Use Cases

| Label    | Description                       |
| -------- | --------------------------------- |
| `docker` | General Docker-based runner       |
| `build`  | Build pipeline jobs               |
| `test`   | Testing jobs (unit/integration)   |
| `prod`   | Stable runners used in production |
| `gpu`    | If GPU enabled runners (custom)   |

---
