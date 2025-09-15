# Kubernetes Interview Questions
---

## 1. What is the difference between Pods and Deployments in Kubernetes?

* **Pod**: Smallest unit in Kubernetes. It runs one or more containers. Pods are temporary and don’t come back automatically if they fail.
* **Deployment**: A controller that manages Pods. It makes sure the right number of Pods are running, supports scaling, rolling updates, and rollbacks.

---

## 2. How can application updates be rolled out in Kubernetes?

### Scenario

Imagine you have **3 Pods serving your app (v1)**. Users are hitting a **Service** that load balances across these Pods. Now you want to update to **v2** without downtime.

---
### What is a Zero-Downtime Rolling Update in Kubernetes?

A rolling update is a way Kubernetes updates your application **without stopping it completely**.
Instead of shutting down all Pods and starting new ones, Kubernetes replaces Pods **one by one** while keeping the app available to users.

**Goal:** Users never see errors or downtime during an update.

### How It Works (Step by Step)

**STEP 1. You have a Deployment**

* Example: 3 Pods of version v1 running behind a Service.
* Users send requests to the Service, which load balances across all 3 Pods.

**STEP 2. You update the Deployment (v2)**

* You change the Deployment (e.g., update container image from `app:v1` → `app:v2`).
* Kubernetes starts a rolling update.

**STEP 3. Rolling Update Process (with `maxUnavailable=0`, `maxSurge=1`)**

* Step 1: Add 1 new Pod (v2). Old Pods still running, Service only sends traffic to healthy Pods.

  ```
  [ v1 | v1 | v1 ] + [ v2 (starting) ]
  ```
* Step 2: Wait for readiness probe. Only after v2 Pod is “Ready” does the Service send traffic to it.

  ```
  [ v1 | v1 | v1 | v2 ]
  ```
* Step 3: Remove 1 old v1 Pod.

  ```
  [ v1 | v1 | v2 ]
  ```
* Step 4: Repeat until all v1 Pods are replaced by v2 Pods.

  ```
  [ v2 | v2 | v2 ]
  ```

**STEP 4. Why Users See No Downtime**

* Old Pods keep running until new Pods are ready.
* Readiness probes ensure new Pods only receive traffic once fully initialized.
* The Service object hides Pod IP changes — clients always connect via the Service, not directly to Pods.

### Deployment YAML with Rolling Update strategy

👉 Example YAML: [deployment\_with\_rolling\_update\_strategy.yml](https://github.com/Purushotham-Learning/mynotes/blob/main/k8s/deployment_with_rolling_update_stratergy.yml)

---

## 4. How do you expose or connect a service running in one network/namespace to another?

## 5. How can applications be autoscaled in Kubernetes?

## 6. How does networking work inside a Kubernetes cluster?

## 7. What do High Availability (HA) and Vertical/Horizontal Autoscaling (VA/HA) mean in Kubernetes?

## 8. How can ephemeral (temporary) data be preserved or captured in Kubernetes?

## 9. How do you detect and troubleshoot I/O errors in Kubernetes storage?

## 10. How can we automatically determine application load and configure autoscaling in Kubernetes?

## 11. What is a Horizontal Pod Autoscaler (HPA), and how does it differ from Vertical Pod Autoscaler (VPA), Cluster Autoscaler (CA), and KEDA?

## 12. How does service discovery work in Kubernetes?

## 13. What are Pod affinity, anti-affinity, and readiness probes in Kubernetes?
🟢 Pod Affinity

Meaning: Tells the scheduler to place Pods together with other Pods (same node/zone).

How it works:

Scheduler looks for nodes that already have Pods with matching labels.

Pods get packed together, possibly leaving other nodes unused.

Rule types:

Required → strict, scheduler must place Pods together.

Preferred → scheduler tries but may relax if resources are limited.

Example scenario: 3 nodes, 6 Pods → all 6 may run on Node A (co-location).

Analogy: Friends who insist on sitting on the same bench.

🔴 Pod Anti-Affinity

Meaning: Tells the scheduler to place Pods apart (spread across nodes/zones).

How it works:

Scheduler avoids putting Pods with the same label on the same node.

Ensures distribution for high availability.

Rule types:

Required → strict, if not enough nodes, extra Pods stay Pending.

Preferred → flexible, scheduler spreads Pods if possible, but may place multiple on the same node if needed.

Example scenario: 3 nodes, 5 Pods →

Required → 3 scheduled (1 per node), 2 remain Pending.

Preferred → all 5 scheduled, but some nodes have 2 Pods.

Analogy: Teacher spreads students across benches so one collapse doesn’t affect everyone.

🟡 Readiness Probe

Meaning: Checks if a Pod is ready to serve traffic.

How it works:

Kubelet runs probe inside container (HTTP, TCP, or command).

If passes → Pod marked Ready, added to Service endpoints.

If fails → Pod stays NotReady, removed from Service (but container keeps running).

Purpose: Prevents traffic from going to Pods that are starting up or unhealthy.

Analogy: A shop that hangs an "Open" sign only when it’s ready to serve customers.

## 14. What is RBAC (Role-Based Access Control) in Kubernetes and how is it configured?

## 15. What are the common challenges while creating a Kubernetes cluster?

## 16. How can Dockerfiles be optimized for building efficient container images?
🧱 How Docker creates layers

Each filesystem instruction (FROM, RUN, COPY, ADD) → creates a new image layer.

Metadata instructions (ENV, CMD, WORKDIR, USER, EXPOSE, LABEL) → update image config, no new layer.

Layers are read-only snapshots stacked together.

At runtime, Docker adds a thin writable container layer on top.

Caching: if a layer hasn’t changed, Docker reuses it → faster builds.

⚡ Dockerfile optimization tips

Order instructions smartly → put stable steps (base OS, system packages, dependency manifests) first, app code last → maximize cache reuse.

Multi-stage builds → build in a heavy image (with compilers/tools), copy only the compiled output into a slim runtime image.

Use minimal base images (slim, alpine, or distroless) → smaller, faster, safer.

Combine RUN commands → fewer layers, clean package caches inside the same RUN.

Use .dockerignore → exclude .git, logs, build artifacts, node_modules, etc.

Don’t run as root → add a non-root user for security.

Pin versions/digests → reproducible and reliable builds.

Enable BuildKit → faster builds + better caching in CI/CD.

## 17. When running CronJobs or DaemonSets, logs are ephemeral — how do you handle logging in Kubernetes?

## 18. What are inodes in Linux and how do they affect Kubernetes storage usage?

## 19. How do you “create a network” in Kubernetes?

* Kubernetes uses a **CNI plugin** (Flannel, Calico, Cilium, etc.) to provide the cluster network.
* To connect workloads:

  * **Expose Pods internally** → use a **Service**.
  * **Expose externally** → use **Service (NodePort/LoadBalancer) + Ingress**.
  * **Control traffic** → use **NetworkPolicy**.

## 20. Autoscaling of node and pods without manual intervention





# 📘 Kubernetes Interview Prep Notes + Hands-On

---

## 1. Core Concepts
**Notes**
- Pod = smallest unit; 1+ containers sharing network & volumes.  
- Controllers: Deployment, StatefulSet, DaemonSet, Job/CronJob.  
- Control Plane: API server, etcd, scheduler, controller-manager.  
- Data Plane: kubelet, kube-proxy, CNI.  

**Hands-on**
```bash
kubectl get nodes -o wide
kubectl get pods -A
kubectl cluster-info
