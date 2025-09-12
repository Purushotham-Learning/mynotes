# Kubernetes Interview Questions

1. **What is the difference between Pods and Deployments in Kubernetes?**  
Pod: Smallest unit in Kubernetes. It runs one or more containers. Pods are temporary and don’t come back automatically if they fail.
Deployment: A controller that manages Pods. It makes sure the right number of Pods are running, supports scaling, rolling updates, and rollbacks.
2. **How can application updates be rolled out in Kubernetes?**  
3. **How do you expose or connect a service running in one network/namespace to another?**  
4. **How can applications be autoscaled in Kubernetes?**  
5. **How does networking work inside a Kubernetes cluster?**  
6. **What do High Availability (HA) and Vertical/Horizontal Autoscaling (VA/HA) mean in Kubernetes?**  
7. **How can ephemeral (temporary) data be preserved or captured in Kubernetes?**  
8. **How do you detect and troubleshoot I/O errors in Kubernetes storage?**  
9. **How can we automatically determine application load and configure autoscaling in Kubernetes?**  
10. **What is a Horizontal Pod Autoscaler (HPA), and how does it differ from Vertical Pod Autoscaler (VPA), Cluster Autoscaler (CA), and KEDA?**  
11. **How does service discovery work in Kubernetes?**
12. Pod affinity and readiness
13. RBAC


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
