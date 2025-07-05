# 🚀 Self-Hosted GitHub Actions Runners on AWS EKS (Free Tier) with Auto-Scaling
This guide sets up GitHub Actions self-hosted runners inside Kubernetes pods using AWS EKS (Free Tier), with automatic scaling powered by the Actions Runner Controller (ARC).

# 📦 STEP 1: Install Required CLI Tools
Install the following tools:
## ✅ AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
unzip awscliv2.zip && sudo ./aws/install
## ✅ eksctl
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp \
sudo mv /tmp/eksctl /usr/local/bin

### ✅ kubectl
curl -o kubectl https://s3.us-west-2.amazonaws.com/amazon-eks/1.27.3/2023-07-05/bin/linux/amd64/kubectl \
chmod +x kubectl && sudo mv kubectl /usr/local/bin

### ✅ Helm
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# 🔐 STEP 2: Configure AWS CLI
aws configure

Fill in the following:\
AWS Access Key ID\
AWS Secret Access Key\
Default region name: us-east-1\
Default output format: json


# ☁️ STEP 3: Create EKS Cluster (Free Tier)
```
eksctl create cluster \
  --name github-runner-cluster \
  --version 1.27 \
  --region us-east-1 \
  --nodegroup-name default \
  --node-type t3.micro \
  --nodes 1 \
  --nodes-min 1 \
  --nodes-max 1 \
  --managed
```

Verify nodes:\
kubectl get nodes

# ⚙️ STEP 4: Install Actions Runner Controller (ARC)

kubectl create namespace actions-runner-system

helm repo add actions-runner-controller https://actions-runner-controller.github.io/actions-runner-controller
helm repo update

helm install arc actions-runner-controller/actions-runner-controller \
  --namespace actions-runner-system \
  --set githubWebhookServer.enabled=false


# 🔑 STEP 5: Create GitHub PAT and Register Secret
1. Go to GitHub Tokens
2. Generate a Personal Access Token with scopes:\
repo\
workflow\
admin:repo_hook

3. Run the following (replace <YOUR_PAT>):

kubectl create secret generic controller-manager \
  -n actions-runner-system \
  --from-literal=github_token=<YOUR_PAT>
  
# 🛠️ STEP 6: Create Runner Deployment and Autoscaler
Save this YAML as runner-deployment.yaml
```
apiVersion: actions.summerwind.dev/v1alpha1
kind: RunnerDeployment
metadata:
  name: my-github-runner
  namespace: actions-runner-system
spec:
  replicas: 1
  template:
    spec:
      repository: yourusername/your-repo-name
      labels:
        - self-hosted
        - eks
        - dev
---
apiVersion: actions.summerwind.dev/v1alpha1
kind: HorizontalRunnerAutoscaler
metadata:
  name: my-runner-autoscaler
  namespace: actions-runner-system
spec:
  scaleTargetRef:
    kind: RunnerDeployment
    name: my-github-runner
  minReplicas: 1
  maxReplicas: 5
  metrics:
    - type: TotalNumberOfQueuedAndInProgressWorkflowRuns
      repositoryNames:
        - yourusername/your-repo-name
```
#### Apply the deployment:
```
kubectl apply -f runner-deployment.yaml
```
# 🚦 STEP 7: Create Workflow to Use the Runner
Save this file as .github/workflows/eks-test.yml in your repo:
```
yml
name: Test EKS GitHub Runner
on: [push]
jobs:
  build:
    runs-on: [self-hosted, eks, dev]
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3
      - name: Say Hello
        run: echo "👋 Hello from EKS GitHub Runner!"
```

Commit and push this file to your repository. A new pod will start in your EKS cluster to handle the job!

# 🔍 STEP 8: Monitor the Runner Pods

kubectl get pods -n actions-runner-system -w

# 🧹 (Optional) STEP 9: Cleanup Resources

To delete the EKS cluster and free up AWS resources:
\
```eksctl delete cluster --name github-runner-cluster --region us-east-1```


