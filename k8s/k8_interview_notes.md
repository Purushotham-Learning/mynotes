Difference between pods & deployments
How to rollout an updates.
How to attach service running on network a to network b
How to auoscale application
How network works in kubernetes
What is HA & VA scaling
How to make sure the ephermal data is captured in kubernetes
How to determine I/O erros in storage
How can we automatically determine application load and implement autoscaling in Kubernetes
HorizontalPodAutoscaler (HPA) – adds/removes pods based on metrics.
VerticalPodAutoscaler (VPA) – right-sizes pod requests/limits.
Cluster Autoscaler (CA) – adds/removes nodes when pods are pending.
Event-driven autoscaling (KEDA) – scales on external systems (queues, cloud services).

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
