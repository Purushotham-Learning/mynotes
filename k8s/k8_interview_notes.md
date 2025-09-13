# Kubernetes Interview Questions

1. **What is the difference between Pods and Deployments in Kubernetes?**  
Pod: Smallest unit in Kubernetes. It runs one or more containers. Pods are temporary and don’t come back automatically if they fail.
Deployment: A controller that manages Pods. It makes sure the right number of Pods are running, supports scaling, rolling updates, and rollbacks.
2. **How can application updates be rolled out in Kubernetes?**                                                                                                     Imagine you have 3 Pods serving your app (v1). Users are hitting a Service that load balances across these Pods.                                                  Now you want to update to v2 without downtime                                                                                                                       

What Kubernetes Does

Step 1 – Add a new Pod (v2)
Deployment spins up 1 extra Pod with the new version.
Old Pods (v1) still serve traffic.

Users see no downtime.      

What is a Zero-Downtime Rolling Update in Kubernetes?

A rolling update is a way Kubernetes updates your application without stopping it completely.
Instead of shutting down all Pods and starting new ones, Kubernetes replaces Pods one by one while keeping the app available to users.

The goal: users never see errors or downtime during an update.

How It Works (Step by Step)
STEP 1. You have a Deployment
  Example:
  3 Pods of version v1 running behind a Service.
  Users send requests to the Service, which load balances across all 3 Pods.
STEP 2. You update the Deployment (v2)
  You change the Deployment (e.g., update container image from app:v1 → app:v2).
  Kubernetes starts a rolling update.
STEP 3. Rolling Update Process
With strategy maxUnavailable=0, maxSurge=1 (the safest zero-downtime config):
Step 1: Add 1 new Pod (v2).
Old Pods still running, Service only sends traffic to healthy Pods.
[ v1 | v1 | v1 ] + [ v2 (starting) ]
Step 2: Wait for readiness probe.
Only after v2 Pod is “Ready” does the Service send traffic to it.
[ v1 | v1 | v1 | v2 ]
Step 3: Remove 1 old v1 Pod.
[ v1 | v1 | v2 ]
Step 4: Repeat until all v1 Pods are replaced by v2 Pods.
[ v2 | v2 | v2 ]
STEP 4. Why Users See No Downtime
Old Pods keep running until new Pods are ready.
Readiness probes ensure new Pods only receive traffic once they are fully initialized.
The Service object hides Pod IP changes — clients always connect via the Service, not directly to Pods.

Deployment with Rolling Update strategy
https://github.com/Purushotham-Learning/mynotes/blob/main/k8s/deployment_with_rolling_update_stratergy.yml
3. 
4. **How do you expose or connect a service running in one network/namespace to another?**  
5. **How can applications be autoscaled in Kubernetes?**  
6. **How does networking work inside a Kubernetes cluster?**  
7. **What do High Availability (HA) and Vertical/Horizontal Autoscaling (VA/HA) mean in Kubernetes?**  
8. **How can ephemeral (temporary) data be preserved or captured in Kubernetes?**  
9. **How do you detect and troubleshoot I/O errors in Kubernetes storage?**  
10. **How can we automatically determine application load and configure autoscaling in Kubernetes?**  
11. **What is a Horizontal Pod Autoscaler (HPA), and how does it differ from Vertical Pod Autoscaler (VPA), Cluster Autoscaler (CA), and KEDA?**  
12. **How does service discovery work in Kubernetes?**
13. **Pod affinity and readiness**
14. **RBAC**
15. **Challenges while creating Kubernetes Cluster**
16.  **How to optimize dockerfiler**
17.  **When you are running a cron jobs in deameonset, the logs are ephermal how do you handle this in kubernetes**
17.  **Learn about inodes** 
18. **Got it 👍 — in Kubernetes you don’t explicitly “create a network” (the cluster network is handled by a CNI plugin like Flannel, Calico, Cilium).
But what you usually mean is:
Expose Pods to each other (internal network) → use a Service.
Expose Pods externally (outside cluster) → use Service + Ingress/LoadBalancer.
Control communication → use a NetworkPolicy.** 







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
