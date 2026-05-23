# ☸️ Kubernetes AI Troubleshooter

> AI-powered Kubernetes troubleshooting CLI for DevOps & SRE engineers.

Detect Kubernetes pod issues automatically and generate AI-based root cause analysis with remediation recommendations.

---

# 🚀 Features

- ✅ Kubernetes pod diagnostics
- ✅ CrashLoopBackOff detection
- ✅ Restart analysis
- ✅ Resource validation
- ✅ Image tag validation
- 🤖 AI-powered root cause analysis
- ⚡ Simple CLI workflow
- ☸️ Multi-namespace support

---

# 🏗️ Architecture

```text
Kubernetes Cluster
        ↓
 Kubernetes Python Client
        ↓
 Static Rule Engine
        ↓
 AI Diagnosis Engine
        ↓
 Root Cause + Recommendations
```

---

# 📂 Project Structure

```bash
k8s-ai-troubleshooter/
├── analyzer/
│   ├── ai.py
│   └── rules.py
├── k8s/
│   └── client.py
├── requirements.txt
├── main.py
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/shakirbhattt/k8s-ai-troubleshooter.git

cd k8s-ai-troubleshooter
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Configure Kubernetes Access

Verify kubeconfig works:

```bash
kubectl get pods
```

---

## 4. Configure OpenAI API Key

```bash
export OPENAI_API_KEY=your_api_key_here
```

---

# ▶️ Usage

## Diagnose pod

```bash
python main.py pod <pod-name>
```

Example:

```bash
python main.py pod nginx-app
```

---

## Diagnose pod in namespace

```bash
python main.py pod nginx-app production
```

---

# 📊 Example Output

```text
🔍 Diagnosing pod: nginx-app

❌ Issues Found:

- Container 'app' in CrashLoopBackOff
- Container 'app' missing resource limits
- Container 'app' using latest image tag

🤖 AI Diagnosis:

Root Cause:
Application startup failure causing repeated restarts.

Impact:
Service instability and downtime.

Recommended Fix:
- Review pod logs
- Add resource requests/limits
- Avoid latest image tags
- Configure liveness probes
```

---

# 🔍 Validation Rules

## Pod Health
- Pod phase validation
- Restart count analysis
- CrashLoopBackOff detection

## Container Validation
- Missing resource requests
- Missing resource limits
- Latest image tag usage

---

# 🤖 AI Diagnosis

AI engine provides:

- Root cause analysis
- Impact assessment
- Remediation steps
- Kubernetes best practices

---

# 🧠 Use Cases

- Kubernetes troubleshooting
- Incident debugging
- SRE operational tooling
- Faster root cause analysis
- CI/CD validation workflows

---

# ⚠️ Limitations

- Requires valid kubeconfig
- Requires OpenAI API key
- Current implementation focuses on pods

---

# 🚀 Future Improvements

- [ ] Deployment diagnostics
- [ ] Node health checks
- [ ] Prometheus integration
- [ ] Slack notifications
- [ ] Grafana integration
- [ ] Helm support
- [ ] Docker image support
- [ ] GitHub Actions integration

---

# 🔐 Security Recommendations

- Never hardcode API keys
- Use Kubernetes RBAC
- Limit cluster permissions
- Rotate credentials regularly

---

# 📦 requirements.txt

```txt
kubernetes
openai
colorama
```

---

# 🤝 Contributing

1. Fork repository
2. Create feature branch
3. Submit pull request

---

# 📜 License

MIT License

---

# 💡 About

Built for DevOps & SRE engineers to reduce Kubernetes troubleshooting time using automation and AI.

---

# ⭐ Support

If this project helped you:
- Give it a ⭐
- Share it with the DevOps community
- Contribute improvements 🚀
