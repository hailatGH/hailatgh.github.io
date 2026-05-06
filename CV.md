# Hailemichael Atrsaw Tibebu

**DevOps Engineer | SRE | Platform Engineer**

*Addis Ababa, Ethiopia* | +251 912 828397 | [hailemichael.atrsaw@gmail.com](mailto:hailemichael.atrsaw@gmail.com)

[LinkedIn](https://www.linkedin.com/in/hailat/) • [GitHub](https://github.com/hailatGH) • [Upwork](https://www.upwork.com/freelancers/~01e6a8c52f8512b0e5) • [Djinni](https://djinni.co/q/8f7c56d873/)

## Professional Summary

Highly skilled DevOps Engineer with **4 years of hands-on production experience** *(5 years total professional experience)* specializing in multi-cloud infrastructure, Kubernetes orchestration, and comprehensive CI/CD automation. Proven track record in designing scalable, high-availability systems across **AWS, Azure, GCP**, and specialized European providers. Expert in **Infrastructure as Code (Terraform/Terragrunt)**, cloud-native security, and observability stacks. Adept at bridging the gap between development and operations to improve deployment frequency and system reliability.

## Core Technical Skills

- **Cloud Providers:** 
    - **AWS:** EC2, S3, SQS, SNS, Lambda, ECR, IAM, RDS, ECS (Fargate), EKS, VPC, Subnet, Internet Gateway, NAT gateway, Route 53, ELB, ASG, Secrets Manager, AWS Site-to-Site VPN 
    - **Azure:** VM, Blob Storage, Service Bus, Functions, ACR, Microsoft Entra ID, Azure Database for PostgreSQL, Container Apps, AKS, VNet, Subnet, Azure Traffic Manager, Azure Application Gateway, Key Vault
    - **GCP:** Compute Engine, Cloud Storage, Cloud Run (Function, Service, Job, Domain Mapping), GKE, Artifact Registry, Cloud SQL, Datastream, Firebase (Identity Platform), BigQuery, IAM, Cloud Logging, Cloud Monitoring (Alerting, Notification Channel, Uptime Check), Places API, reCaptcha, Secret Manager
    - **Others:** Digital Ocean, Infomaniak, Exoscale, Hetzner
- **Containerization & Orchestration:** Docker, Docker Compose, Kubernetes (EKS, AKS, GKE, self-hosted RKE2), Helm.
- **Infrastructure as Code (IaC):** Terraform, Terragrunt, Ansible (Configuration as a Code), Packer (Image as a Code).
- **CI/CD Tools:** GitLab CI, GitHub Actions, Azure DevOps.
- **Observability:** Prometheus, Grafana, Loki, Mimir, CloudWatch, Azure Monitor, Sentry, Cloud Logging and Cloud Monitoring.
- **Languages & Frameworks:** Python (FastAPI, Litestar, Django Rest Framework, Mesop), Bash.
- **Security & IAM:** Teleport, HashiCorp Vault (Infisical), Microsoft Entra ID, Cert-Manager, Kyverno.
- **Networking:** VPC, Site-to-Site VPN, Ingress Nginx, Traefik, Load Balancers.

## Professional Experience

### **DevOps Engineer | Exponent**

*July 2023 – Present*

- **Infrastructure Management:** Designed and provisioned multi-cloud infrastructure (AWS, Azure, GCP, Digital Ocean, Infomaniak, Exoscale) using Terraform and Terragrunt, maintaining multiple environments with high consistency.
- **Kubernetes Expertise:** Orchestrated managed (EKS, AKS, GKE) and self-hosted (RKE2 on Infomaniak/Exoscale) Kubernetes clusters, implementing advanced controllers like Kyverno for policy enforcement and Cert-Manager for TLS automation.
- **CI/CD Pipeline Design:** Developed robust GitLab CI and GitHub Actions pipelines featuring automated linting, security best-practice validation, unit testing, multi-stage builds and deployment.
- **Observability & Reliability:** Deployed and managed a full-scale observability stack (Grafana, Prometheus, Loki, Mimir); established SLIs/SLOs and led on-call rotations, responding to production incidents and conducting post-mortem analyses.
- **Cloud-Native Tooling:** Implemented automated database backups using CNPG for PostgreSQL, secret management via Infisical, and secure resource access through Teleport.
- **Automation:** Built internal CLI tools to streamline SRE tasks and integrated Renovate bot for automated dependency management across repositories.

### **DevOps Engineer | Tefer (Contracted by Stableduel)**

*February 2022 – July 2023*

- **Architected Cloud Solutions:** Designed and scaled AWS and Azure infrastructure for high-traffic environments using IaC patterns.
- **CI/CD Modernization:** Built and maintained enterprise CI/CD pipelines in Azure DevOps, implementing secure secret injection and optimized build stages.
- **Cost & Efficiency Optimization:** Implemented rigorous lifecycle policies for ECR/ACR and S3/Blob storage, significantly reducing monthly cloud expenditures.
- **Data Protection:** Standardized database scheduled backup strategies (onsite and offsite) to ensure business continuity.

### **Backend | Cloud Developer | Tefer (Contracted by Stableduel)**

*March 2021 – February 2022*

- **API Development:** Engineered high-performance REST APIs using Python (Django Rest Framework, FastAPI) and implemented real-time communication via WebSockets.
- **Systems Engineering:** Developed multi-stage optimized Docker images and managed background task processing using Celery and Redis.
- **Cloud Foundations:** Provisioned AWS infrastructure (ECS Fargate, RDS, SQS, SNS) using Terraform, laying the groundwork for automated scaling.

## Featured Projects

### **Exponent Kubernetes Service (XKS)**
- **Problem Solved:** Overcame the lack of managed Kubernetes services on niche cloud providers (Infomaniak, Exoscale) by engineering a custom solution to achieve automated lifecycle management and horizontal cluster autoscaling.
- **Tools Used:** Python, RKE2, Terraform, Terragrunt, Cloud-Init, Packer, Envoy, Ansible
- **Impact:** Engineered a sophisticated automation framework that provisions self-hosted RKE2 clusters using *custom CRDs and Terraform blueprints*, ensuring standardized bootstrapping and scaling for sovereign cloud environments.

### **Datacycle**
- **Problem Solved:** Addressed the need for a non-invasive, decentralized backup mechanism for diverse CNPG workloads running on Kubernetes.
- **Tools Used:** Python, Kubernetes API, S3-Compatible Storage (MinIO/AWS S3), Poetry.
- **Impact:** Developed a K8s-native tool that utilizes resource annotations to *automatically discover and back up databases*. Handles scheduling, multi-cloud retention policies, and offsite storage synchronization without requiring manual intervention for new apps.

### **Exponent Site to Site VPN (XSSV)**
- **Problem Solved:** Resolved complex secure connectivity requirements for third-party clients needing isolated access to internal Kubernetes services without compromising the primary network.
- **Tools Used:** StrongSwan (IPsec), Terragrunt, OpenStack (Infomaniak), Bash.
- **Impact:** Architected a multi-tenant VPN relay system using a *unique two-hop IPsec tunnel* (`Customer <-> Relay VM <-> K8s Pod`). Ensured network isolation and unique NAT-T port mapping for multiple providers while centralizing traffic management.

### **Chart Generic**
- **Problem Solved:** Eliminated "configuration drift" and duplicated Helm code across dozens of microservices.
- **Tools Used:** Helm, Kubernetes, YAML.
- **Impact:** Created a versatile "Standard Library" Helm chart that supports both `Deployment` and `StatefulSet` via simple value toggles. Included pre-configured patterns for Ingress Nginx, Traefik, Cert-Manager, and horizontal autoscaling, *reducing new service onboarding time by 80%*.

### **Sentry Gateway**
- **Problem Solved:** Optimized error tracking and security by abstracting proyek-specific Sentry DSNs and providing a unified entry point for error reporting.
- **Tools Used:** FastAPI, Python, Docker.
- **Impact:** Built a centralized middleware proxy that routes application errors to appropriate Sentry projects while managing sensitive project tokens at the gateway level, improving security and event filtering.

### **Infrastructure Libraries (Terraform Modules & GitLab CI Templates)**
- **Problem Solved:** Standardized organizational security and deployment patterns to ensure consistent quality across all engineering teams.
- **Tools Used:** Terraform, Terragrunt, GitLab CI, GitHub Actions.
- **Impact:** Developed a versioned library of reusable IaC modules and CI templates. Standardized everything from VPC peering and EKS cluster hardening to automated multi-stage Docker builds and linter enforcement.

## Additional Deployment Projects

### **Africa CDC & Data Repository (CDR)**
- **Azure Infrastructure:** Provisioned **Azure Container Apps (ACA)** for microservices, **PostgreSQL Flexible Server**, and **Azure Container App Jobs** for data tasks. Configured **Service Bus Namespace**, **Key Vault**, **Log Analytics**, and **Storage Accounts (Data Lake Gen2)**.
- **Hetzner & Hybrid-Cloud:** Orchestrated **Hetzner (hcloud)** servers with **Cloudflare** for DNS. Automated the installation of **ClickHouse**, **Apache Superset**, **n8n**, **DHIS2**, and **RServe** using specialized Terraform `null_resource` and remote-exec blocks.
- **Global Data Hub:** Designed a hybrid infrastructure to support a centralized data repository, leveraging Azure for orchestration and Hetzner for cost-effective heavy-lifting analytics.

### **Case Tracking Monorepo**
- **GCP Foundation:** Architected the entire GCP environment including **VPC Networks**, **Subnets**, and **Cloud SQL (PostgreSQL)**. Implemented **Firebase (Identity Platform)** for user authentication.
- **Data Streaming & Analytics:** Configured **GCP Datastream** for real-time replication from **PostgreSQL** to **BigQuery**, utilizing **Secret Manager** for credential safety.
- **Microservices Orchestration:** Deployed monorepo services to **GKE** and **Cloud Run**. Integrated **GCP Monitoring (Uptime Checks)**, **Logging**, and **reCaptcha enterprise**.
- **Security & IAM:** Standardized project-level **IAM Roles**, custom service accounts, and **Organization Policies** to enforce security best practices across environments.

### **KGI Monorepo**
- **AWS Infrastructure:** Provisioned comprehensive AWS environments utilizing **ECS Fargate** for containerized services (**web**, **api**, **website**) and **RDS (PostgreSQL)** for persistence.
- **Advanced Networking:** Configured **AWS VPC**, **Public/Private Subnets**, and **AWS VPN Gateway (S2S VPN)** to bridge internal networks.
- **Event-Driven & Security:** Implemented **AWS SQS** for asynchronous job processing and **AWS Secrets Manager** for secure credential management. Integrated **AWS Route 53** for DNS and managed automated deployment pipelines via **GitHub Actions**.

### **ROE Chatbot**
- **DigitalOcean Stack:** Engineered the production environment utilizing **DigitalOcean App Platform** for backend/frontend and **DigitalOcean Database Clusters (PostgreSQL)**.
- **Network & Scaling:** Provisioned **DigitalOcean VPC** and **Container Registry**. Managed horizontal scaling and domain routing with automated SSL/TLS certificates.
- **Secret Management:** Integrated **Infisical** for centralized, secure secret injection across build and runtime environments, utilizing **PostgreSQL** as the persistent backend for the Infisical instance.

## Education

- **Bachelor of Science in Electrical and Computer Engineering** *(Computer Engineering Focus)* – Jimma University
- **AWS Cloud Computing** – ALX Africa

## Certifications

- **AWS Certified Solutions Architect – Associate** *(Amazon Web Services)* - [View Certificate](https://www.credly.com/badges/4898bdae-19da-4ce7-b501-4ef43db0737e)
- **AWS Certified Cloud Practitioner** *(Amazon Web Services)* - [View Certificate](https://www.credly.com/badges/e630c56d-ab6e-4f98-b6da-cfce5263ad38)
- **IELTS – British Council** *(Overall Band Score: 7.0)* - [View Certificate](https://www.credly.com/badges/bd73fccc-196b-469a-bbb3-9c117ede0373/linked_in_profile)