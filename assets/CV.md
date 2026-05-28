# Hailemichael Atrsaw Tibebu

**DevOps Engineer | SRE | Platform Engineer**

*Addis Ababa, Ethiopia* | +251 912 828397 | [hailemichael.atrsaw@gmail.com](mailto:hailemichael.atrsaw@gmail.com)

[LinkedIn](https://www.linkedin.com/in/hailat/) • [GitHub](https://github.com/hailatGH)

## Professional Summary

DevOps Engineer with **4+ years of production experience** managing **12+ Kubernetes clusters**, **30+ microservices**, and **12+ production environments** across **6 cloud providers** (AWS, Azure, GCP, Digital Ocean, Infomaniak, Exoscale). Achieved **99.9% uptime** for systems serving **20k+ daily active users**. Proven track record of delivering measurable impact: reduced deployment times **from 45 to 8 minutes** (84% improvement), cut service onboarding time by **80%**, decreased infrastructure operations by **70%** through automation, and achieved **35% cloud cost reduction**. Expert in **Infrastructure as Code (Terraform/Terragrunt)**, Kubernetes orchestration, CI/CD automation, enterprise observability, and zero-trust security. Engineered custom platforms managing **50+ nodes** and backup orchestrators protecting **30+ PostgreSQL instances** with **99.99% success rate**. Created reusable infrastructure libraries adopted by **10+ engineering teams**.

## Core Technical Skills

- **Cloud Platforms:** 
    - **AWS:** Compute (EC2, ECS Fargate, EKS, Lambda), Storage (S3, ECR), Database (RDS), Networking (VPC, Route 53, Site-to-Site VPN, ELB, ASG), Messaging (SQS, SNS), Security (IAM, Secrets Manager)
    - **Azure:** Compute (VM, Container Apps, AKS, Functions), Storage (Blob Storage, ACR), Database (PostgreSQL Flexible Server), Networking (VNet, Traffic Manager, Application Gateway), Messaging (Service Bus), Security (Microsoft Entra ID, Key Vault)
    - **GCP:** Compute (Compute Engine, GKE, Cloud Run), Storage (Cloud Storage, Artifact Registry), Database (Cloud SQL, BigQuery), Data Streaming (Datastream), Identity (Firebase), Monitoring (Cloud Logging, Cloud Monitoring), Security (IAM, Secret Manager, reCaptcha)
    - **Others:** Digital Ocean, Infomaniak, Exoscale, Hetzner
- **Containerization & Orchestration:** Docker, Kubernetes (EKS, AKS, GKE, self-hosted RKE2), Helm, Docker Compose
- **Infrastructure as Code:** Terraform, Terragrunt, Ansible, Packer
- **CI/CD:** GitLab CI, GitHub Actions, Azure DevOps
- **Observability & Monitoring:** Prometheus, Grafana, Loki, Mimir, CloudWatch, Azure Monitor, Sentry
- **Programming:** Python (FastAPI, Litestar, Django Rest Framework, Mesop), Bash
- **Security & Secrets Management:** Teleport, HashiCorp Vault, Infisical, 1Password
- **Networking:** Site-to-Site VPN, Ingress Nginx, Traefik, Load Balancers, VPC Design

## Professional Experience

### **DevOps Engineer | Exponent**

*July 2023 – Present (2.9 years)*

- **Infrastructure Management:** Designed and provisioned multi-cloud infrastructure (AWS, Azure, GCP, Digital Ocean, Infomaniak, Exoscale) using Terraform and Terragrunt, maintaining 12+ production and staging environments with high consistency across 6 cloud providers.
- **Kubernetes Expertise:** Orchestrated 12+ managed (EKS, AKS, GKE) and self-hosted (RKE2) clusters, implementing Kyverno for policy enforcement and Cert-Manager for automated TLS management across multi-cloud environments.
- **CI/CD Pipeline Design:** Developed robust GitLab CI and GitHub Actions pipelines featuring automated linting, security best-practice validation, unit testing, multi-stage builds and deployment, reducing deployment time from 45 to 8 minutes.
- **Observability & Reliability:** Deployed and managed a full-scale observability stack (Grafana, Prometheus, Loki, Mimir) monitoring 30+ services and 100+ metrics; established SLIs/SLOs achieving 99.9% uptime and led on-call rotations, responding to production incidents and conducting post-mortem analyses.
- **Cloud-Native Tooling:** Implemented automated CNPG database backups for 30+ PostgreSQL instances, centralized secret management via Infisical, and zero-trust access control through Teleport.
- **Automation:** Built internal CLI tools to streamline SRE tasks, reducing common operations time by 70%, and integrated Renovate bot for automated dependency management across 20+ repositories.

### **DevOps Engineer | Tefer (Contracted by Stableduel)**

*February 2022 – July 2023*

- **Architected Cloud Solutions:** Designed and scaled AWS and Azure infrastructure handling 20k+ daily active users and 3k+ concurrent requests using IaC patterns.
- **CI/CD Modernization:** Built and maintained enterprise CI/CD pipelines in Azure DevOps, implementing secure secret injection and optimized build stages.
- **Cost & Efficiency Optimization:** Implemented rigorous lifecycle policies for ECR/ACR and S3/Blob storage, reducing monthly cloud expenditures by 35%.
- **Data Protection:** Standardized database scheduled backup strategies (onsite and offsite) to ensure business continuity.

### **Backend | Cloud Developer | Tefer (Contracted by Stableduel)**

*March 2021 – February 2022*

- **API Development:** Engineered high-performance REST APIs using Python (Django Rest Framework, FastAPI) and implemented real-time communication via WebSockets.
- **Systems Engineering:** Developed multi-stage optimized Docker images and managed background task processing using Celery and Redis.
- **Cloud Foundations:** Provisioned AWS infrastructure (ECS Fargate, RDS, SQS, SNS) using Terraform, laying the groundwork for automated scaling.

## Featured Projects

### **Custom Kubernetes Platform**
- **Problem Solved:** Overcame the lack of managed Kubernetes services on niche cloud providers by engineering a custom solution to achieve automated lifecycle management and horizontal cluster autoscaling.
- **Tools Used:** Python, RKE2, Terraform, Terragrunt, Cloud-Init, Packer, Envoy, Ansible
- **Impact:** Built automation framework provisioning self-hosted RKE2 clusters using custom CRDs and Terraform, managing 8 production clusters and 50+ nodes with 95% reduction in manual deployment effort.

### **Database Backup Orchestrator**
- **Problem Solved:** Addressed the need for a non-invasive, decentralized backup mechanism for diverse CNPG workloads running on Kubernetes.
- **Tools Used:** Python, Kubernetes API, S3-Compatible Storage (MinIO/AWS S3), Poetry.
- **Impact:** Built K8s-native backup automation using resource annotations to auto-discover and backup 30+ database instances with 99.99% success rate, supporting multi-cloud retention and offsite synchronization without manual configuration.

### **Multi-Tenant VPN Gateway**
- **Problem Solved:** Resolved complex secure connectivity requirements for third-party clients needing isolated access to internal Kubernetes services without compromising the primary network.
- **Tools Used:** StrongSwan (IPsec), Terragrunt, OpenStack, Bash.
- **Impact:** Architected a multi-tenant VPN relay system using a *unique two-hop IPsec tunnel* (`Customer <-> Relay VM <-> K8s Pod`), supporting 8 concurrent client connections. Ensured network isolation and unique NAT-T port mapping for multiple providers while centralizing traffic management.

### **Universal Helm Template**
- **Problem Solved:** Eliminated "configuration drift" and duplicated Helm code across dozens of microservices.
- **Tools Used:** Helm, Kubernetes, YAML.
- **Impact:** Created a versatile "Standard Library" Helm chart that supports both `Deployment` and `StatefulSet` via simple value toggles, adopted by 60+ microservices. Included pre-configured patterns for Ingress Nginx, Traefik, Cert-Manager, and horizontal autoscaling, *reducing new service onboarding time by 80%*.

### **Error Tracking Proxy**
- **Problem Solved:** Optimized error tracking and security by abstracting project-specific DSNs and providing a unified entry point for error reporting.
- **Tools Used:** FastAPI, Python, Docker.
- **Impact:** Built a centralized middleware proxy that routes application errors to appropriate monitoring projects while managing sensitive project tokens at the gateway level, improving security and event filtering.

### **Infrastructure Libraries (Terraform Modules & GitLab CI Templates)**
- **Problem Solved:** Standardized organizational security and deployment patterns to ensure consistent quality across all engineering teams.
- **Tools Used:** Terraform, Terragrunt, GitLab CI, GitHub Actions.
- **Impact:** Developed a versioned library of 20+ reusable IaC modules and CI templates adopted across 10 engineering teams. Standardized everything from VPC peering and EKS cluster hardening to automated multi-stage Docker builds and linter enforcement.

## Additional Deployment Projects

- **Healthcare Analytics Platform:** Hybrid Azure infrastructure utilizing Azure Container Apps, PostgreSQL Flexible Server, Data Lake Gen2, and automated deployment of ClickHouse, Apache Superset, and workflow automation for centralized health data analytics.
- **Case Management Platform:** Full-stack GCP deployment with Cloud Run microservices, Firebase authentication, Datastream-to-BigQuery pipeline, and enterprise-grade monitoring and security policies.
- **Enterprise Service Platform:** AWS-based monorepo with ECS Fargate services, RDS PostgreSQL, Site-to-Site VPN, SQS event processing, and automated GitHub Actions deployment pipelines.
- **Conversational AI Platform:** DigitalOcean App Platform deployment with managed PostgreSQL clusters, VPC networking, container registry, and secret management.

## Education

- **Bachelor of Science in Electrical and Computer Engineering** *(Computer Engineering Focus)* – Jimma University, 2021
- **AWS Cloud Computing** – ALX Africa, 2022

## Certifications

- **AWS Certified Solutions Architect – Associate** – [View Certificate](https://www.credly.com/badges/4898bdae-19da-4ce7-b501-4ef43db0737e)
- **AWS Certified Cloud Practitioner** – [View Certificate](https://www.credly.com/badges/e630c56d-ab6e-4f98-b6da-cfce5263ad38)
