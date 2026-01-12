# GitHub Actions Teaching Topics - Comprehensive Outline

Based on comprehensive analysis of both DevOps course repositories at KEA.

---

## **Module 1: Foundations (Week 1)**

### **1.1 Introduction to CI/CD**
- What is Continuous Integration?
- What is Continuous Delivery?
- What is Continuous Deployment?
- Why automate workflows?
- The DevOps feedback loop

### **1.2 GitHub Actions Basics**
- What are GitHub Actions?
- When and why to use GitHub Actions?
- Comparison with other CI/CD tools (GitLab CI, Jenkins, CircleCI)
- GitHub Actions pricing and limitations
- Free tier for public repositories

### **1.3 Core Concepts**
- **Workflows**: The automated process
- **Events**: What triggers workflows
- **Jobs**: Groups of steps
- **Steps**: Individual tasks
- **Actions**: Reusable units of code
- **Runners**: Where workflows execute (GitHub-hosted vs self-hosted)

### **1.4 YAML Fundamentals**
- YAML syntax review
- Indentation rules (2 spaces for GitHub Actions)
- Key-value pairs, lists, and nested structures
- Common YAML pitfalls

---

## **Module 2: Creating Your First Workflows (Week 2)**

### **2.1 Workflow Structure**
- `.github/workflows` directory
- Workflow file naming conventions
- Basic workflow anatomy
- `name`, `on`, `jobs` keywords

### **2.2 Event Triggers**
- `push` - trigger on code push
- `pull_request` - trigger on PRs
- `workflow_dispatch` - manual triggers
- Branch and path filtering
- Multiple event triggers

### **2.3 Hello World Workflow**
- Creating your first workflow
- Using `runs-on` to specify runners
- Available runners: Ubuntu, Windows, macOS
- Simple shell commands with `run`

### **2.4 The Checkout Action**
- Understanding `actions/checkout@v4`
- Why you need to checkout code
- Checkout options and configurations
- Hash-pinning vs semantic versioning

---

## **Module 3: Working with Actions (Week 3)**

### **3.1 GitHub Actions Marketplace**
- Exploring the marketplace
- Community vs verified actions
- Reading action documentation
- Action inputs and outputs

### **3.2 Common Actions**
- `actions/checkout` - checking out code
- `actions/setup-node` - Node.js setup
- `actions/setup-python` - Python setup
- `actions/upload-artifact` - artifact storage
- `actions/download-artifact` - artifact retrieval

### **3.3 Using Actions in Workflows**
- `uses` keyword
- Specifying action versions
- Passing inputs with `with`
- Capturing outputs

---

## **Module 4: Secrets and Security (Week 4)**

### **4.1 Managing Secrets**
- What are GitHub Secrets?
- Creating secrets via UI
- Creating secrets via `gh secret set`
- Accessing secrets with `${{ secrets.SECRET_NAME }}`
- Secret masking in logs

### **4.2 GITHUB_TOKEN**
- Automatic token provisioning
- Token permissions and scopes
- Using GITHUB_TOKEN for API calls
- Permission best practices

### **4.3 Security Best Practices**
- Never expose secrets in logs
- Hash-pinning third-party actions for security
- Avoiding risky third-party actions
- Using native commands over actions when possible
- Scoping workflow permissions
- Security hardening checklist

---

## **Module 5: Context and Expressions (Week 5)**

### **5.1 GitHub Context**
- Understanding `${{ github }}` object
- Accessing event information
- Repository metadata
- Workflow run information

### **5.2 Common Context Variables**
- `github.event_name`
- `github.ref`
- `github.sha`
- `github.actor`
- `github.repository`

### **5.3 Expressions and Functions**
- Using expressions in workflows
- `toJson()` for debugging
- String functions
- Logical operators

---

## **Module 6: Jobs and Dependencies (Week 6)**

### **6.1 Multiple Jobs**
- Defining multiple jobs
- Parallel execution by default
- Job naming and identification

### **6.2 Job Dependencies**
- Using `needs` to create dependencies
- Sequential execution with `needs`
- Quality gates pattern
- Job outputs and inputs

### **6.3 Conditional Execution**
- `if` conditions
- `success()`, `failure()`, `always()`
- Conditional steps
- Conditional jobs

---

## **Module 7: Continuous Integration (Week 7)**

### **7.1 CI Fundamentals**
- What makes good CI?
- Fast feedback loops
- Fail fast principle

### **7.2 Linting in CI**
- Why lint in CI?
- Language-specific linters (ESLint, Standard.js, Pylint)
- Super Linter for multi-language projects
- Hadolint for Dockerfiles
- Setting up linting jobs

### **7.3 Testing in CI**
- Running unit tests
- Running integration tests
- Test result reporting
- Test coverage

### **7.4 Build Automation**
- Building applications in CI
- Using `npm ci` for Node.js
- Dependency caching
- Build artifacts

### **7.5 Status Badges**
- Adding workflow status badges
- README documentation
- Making CI visible

---

## **Module 8: Matrix Builds (Week 8)**

### **8.1 Matrix Strategy**
- What are matrix builds?
- When to use matrices?
- Performance considerations

### **8.2 Creating Matrices**
- `strategy.matrix` syntax
- Testing across Node versions
- Testing across operating systems
- Testing across environments

### **8.3 Matrix Variables**
- Accessing matrix values
- `${{ matrix.variable }}`
- Matrix combinations

---

## **Module 9: Advanced Triggers and Scheduling (Week 9)**

### **9.1 Advanced Event Triggers**
- `workflow_run` - chaining workflows
- `schedule` - cron-based triggers
- `repository_dispatch` - external triggers
- Webhook events

### **9.2 Cron Scheduling**
- Cron syntax basics
- Using crontab.guru
- Scheduled maintenance tasks
- Periodic testing

### **9.3 Path and Branch Filtering**
- `paths` - trigger on specific file changes
- `paths-ignore` - exclude paths
- `branches` - specific branch triggers
- `tags` - tag-based triggers

---

## **Module 10: Docker Integration (Week 10)**

### **10.1 Building Docker Images**
- Docker build in workflows
- Multi-stage builds
- Build optimization
- Layer caching

### **10.2 Container Registry**
- GitHub Container Registry (ghcr.io)
- Authentication with CR PAT
- Pushing images to registry
- Image tagging strategies

### **10.3 Docker in CI/CD**
- Running tests in containers
- Docker Compose in workflows
- Container security scanning

---

## **Module 11: Continuous Delivery (Week 11)**

### **11.1 CD Fundamentals**
- CI vs CD vs CD
- Deployment readiness
- Build once, deploy many

### **11.2 Artifact Management**
- Creating build artifacts
- Uploading artifacts
- Downloading artifacts
- Artifact retention policies

### **11.3 Release Automation**
- GitHub Releases
- Automated release notes
- Semantic versioning
- Git tags and releases

---

## **Module 12: Continuous Deployment (Week 12)**

### **12.1 Deployment Strategies**
- Push-based vs pull-based deployment
- GitOps principles
- Zero-downtime deployments

### **12.2 SSH Deployment**
- Managing SSH keys in secrets
- SSH key setup in workflows
- SCP file transfer
- Remote command execution
- Cleanup and security

### **12.3 Full CD Pipeline**
- Automated deployment workflow
- Docker deployment pattern
- Configuration management
- Smoke testing post-deployment

### **12.4 Deployment to Cloud**
- Deploying to Azure VMs
- Cloud authentication
- Multi-environment deployments

---

## **Module 13: Testing Strategies (Week 13)**

### **13.1 Test Types in CI/CD**
- Unit testing
- Integration testing
- End-to-end testing
- Smoke testing

### **13.2 E2E Testing with Playwright**
- Setting up Playwright in workflows
- Running browser tests
- Test parallelization
- Screenshot and video artifacts

### **13.3 Continuous Testing**
- Testing at every stage
- Test pyramid in CI/CD
- Performance testing
- Security testing integration

---

## **Module 14: Security Integration (DevSecOps) (Week 14)**

### **14.1 Shift-Left Security**
- DevSecOps principles
- Integrating security in CI/CD
- SAST vs DAST

### **14.2 SAST (Static Analysis)**
- Code scanning tools
- Vulnerability detection
- License compliance
- Quality gates

### **14.3 DAST (Dynamic Analysis)**
- Runtime security testing
- Penetration testing automation
- API security testing

### **14.4 Dependency Scanning**
- Dependabot integration
- Automated dependency updates
- Vulnerability alerts
- Supply chain security

### **14.5 Container Security**
- Docker image scanning
- Base image selection
- Vulnerability remediation

---

## **Module 15: Branch Protection and Quality Gates (Week 15)**

### **15.1 Branch Protection Rules**
- Requiring status checks
- Required reviews
- Protecting main/master
- Integration with workflows

### **15.2 Quality Gates**
- Multiple jobs as gates
- Using `needs` for gates
- Preventing bad code from merging
- Custom quality metrics

### **15.3 PR Workflows**
- PR templates
- Automated PR checks
- Comment automation
- PR labeling

---

## **Module 16: Workflow Optimization (Week 16)**

### **16.1 Performance Optimization**
- Caching dependencies
- `actions/cache`
- Docker layer caching
- Artifact reuse

### **16.2 Parallel Execution**
- Running jobs in parallel
- Splitting tests
- Matrix parallelization
- Resource considerations

### **16.3 Debugging Workflows**
- Using `ACTIONS_STEP_DEBUG`
- Viewing logs
- Troubleshooting failures
- Common pitfalls

---

## **Module 17: Advanced Patterns (Week 17)**

### **17.1 Reusable Workflows**
- Creating reusable workflows
- Workflow composition
- Organization-level workflows
- Template repositories

### **17.2 Composite Actions**
- Creating custom actions
- Action metadata
- JavaScript vs Docker actions
- Publishing actions

### **17.3 Workflow Orchestration**
- Chaining workflows with `workflow_run`
- Cross-repository workflows
- Complex pipelines
- Event propagation

---

## **Module 18: Monitoring and Observability (Week 18)**

### **18.1 Workflow Monitoring**
- Monitoring workflow runs
- Failure notifications
- Slack/email integration
- Metrics and analytics

### **18.2 GitHub API Integration**
- Using `gh api` in workflows
- Accessing GitHub data
- Creating issues from workflows
- Updating project boards

### **18.3 Logging Best Practices**
- Structured logging
- Log analysis
- Debugging production issues

---

## **Module 19: Self-Hosted Runners (Week 19)**

### **19.1 When to Use Self-Hosted**
- GitHub-hosted vs self-hosted
- Cost considerations
- Security implications
- Use cases

### **19.2 Setting Up Runners**
- Runner installation
- Runner configuration
- Scaling runners
- Runner maintenance

---

## **Module 20: Real-World Scenarios (Week 20)**

### **20.1 Monorepo CI/CD**
- Path-based workflows
- Selective builds
- Dependency management

### **20.2 Microservices Deployment**
- Multi-service workflows
- Service dependencies
- Coordinated deployments

### **20.3 GitOps Workflows**
- Infrastructure as Code integration
- Terraform in workflows
- Kubernetes deployments

### **20.4 Rollback Strategies**
- Automated rollbacks
- Health checks
- Deployment verification

---

## **Bonus Topics (Advanced/Optional)**

### **Environment Management**
- GitHub Environments
- Environment protection rules
- Environment secrets
- Deployment approvals

### **GitHub Apps Integration**
- Using GitHub Apps in workflows
- App authentication
- Advanced permissions

### **Cost Optimization**
- Managing runner minutes
- Optimizing workflow efficiency
- Self-hosted vs hosted cost analysis

### **Compliance and Auditing**
- Audit logs
- Compliance requirements
- SOC 2/ISO compliance

---

## **Suggested Teaching Progression**

### **Beginner Level (Modules 1-7)**
Focus on fundamentals, creating basic workflows, and implementing simple CI pipelines.

**Learning Outcomes:**
- Understand CI/CD concepts
- Create basic workflows
- Use common actions
- Implement secrets management
- Build simple CI pipelines

### **Intermediate Level (Modules 8-14)**
Introduce more complex patterns, security integration, and deployment automation.

**Learning Outcomes:**
- Implement matrix builds
- Create complex workflows with dependencies
- Integrate Docker into pipelines
- Deploy applications automatically
- Implement security scanning

### **Advanced Level (Modules 15-20)**
Cover optimization, advanced patterns, and real-world production scenarios.

**Learning Outcomes:**
- Optimize workflow performance
- Create reusable workflows and actions
- Implement production-grade pipelines
- Handle complex deployment scenarios
- Monitor and debug workflows effectively

---

## **Hands-On Projects to Include**

### **Project 1: Basic CI Pipeline**
**Objective:** Create a basic CI workflow for a Node.js app
- Set up linting
- Run unit tests
- Display status badge

### **Project 2: Matrix Testing**
**Objective:** Implement matrix builds across multiple environments
- Test across Node.js versions (14.x, 16.x, 18.x, 20.x)
- Test across operating systems (Ubuntu, Windows, macOS)
- Generate test reports

### **Project 3: Docker Integration**
**Objective:** Build and push Docker images to GitHub Container Registry
- Create optimized Dockerfile
- Build multi-stage images
- Push to ghcr.io
- Tag with semantic versions

### **Project 4: Full CI/CD Pipeline**
**Objective:** Create a complete CI/CD pipeline with deployment to a VM
- Run linting and tests
- Build Docker image
- Deploy to Azure VM via SSH
- Implement smoke tests

### **Project 5: Security Scanning**
**Objective:** Implement security scanning (SAST/DAST)
- Integrate dependency scanning
- Add container vulnerability scanning
- Set up Dependabot
- Create security quality gates

### **Project 6: E2E Testing**
**Objective:** Set up E2E testing with Playwright
- Configure Playwright in workflows
- Run browser tests
- Capture screenshots on failure
- Generate test reports

### **Project 7: Reusable Workflows**
**Objective:** Create reusable workflows for your organization
- Extract common patterns
- Create composite actions
- Share across repositories
- Document usage

### **Project 8: Production Pipeline**
**Objective:** Build a complete production-ready workflow with monitoring
- Multi-environment deployment
- Approval gates
- Rollback capability
- Monitoring integration
- Incident notifications

---

## **Practical Workflow Examples**

### **Example 1: Basic CI Workflow**

```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm install
      - run: npm run lint

  test:
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm test
```

### **Example 2: Matrix Build Workflow**

```yaml
name: Matrix Testing
on: [push, pull_request]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        node-version: [14.x, 16.x, 18.x, 20.x]
        os: [ubuntu-latest, windows-latest, macos-latest]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'
      - run: npm ci
      - run: npm test
```

### **Example 3: Docker Build and Push**

```yaml
name: Docker Build and Push
on:
  push:
    branches: [main]
    tags: ['v*']

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Login to GitHub Container Registry
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: |
            ghcr.io/${{ github.repository }}:latest
            ghcr.io/${{ github.repository }}:${{ github.sha }}
```

### **Example 4: Deployment with SSH**

```yaml
name: Deploy to Production
on:
  workflow_run:
    workflows: ["CI"]
    types: [completed]
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    if: ${{ github.event.workflow_run.conclusion == 'success' }}
    steps:
      - name: Setup SSH
        run: |
          mkdir -p ~/.ssh/
          echo "${{ secrets.SSH_PRIVATE_KEY }}" > ~/.ssh/deploy_key
          chmod 600 ~/.ssh/deploy_key
          ssh-keyscan -H ${{ secrets.SERVER_HOST }} >> ~/.ssh/known_hosts

      - name: Deploy application
        run: |
          ssh -i ~/.ssh/deploy_key ${{ secrets.SERVER_USER }}@${{ secrets.SERVER_HOST }} << 'EOF'
            cd /app
            docker-compose pull
            docker-compose up -d
          EOF

      - name: Cleanup
        if: always()
        run: rm -f ~/.ssh/deploy_key
```

### **Example 5: Quality Gates**

```yaml
name: Quality Gates
on: [push, pull_request]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run security scan
        run: npm audit --audit-level=high

  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm install
      - run: npm run lint

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npm test

  build:
    runs-on: ubuntu-latest
    needs: [security, lint, test]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npm run build
```

---

## **Assessment and Evaluation**

### **Formative Assessment**
- Weekly hands-on exercises
- Code review of workflow files
- Troubleshooting challenges
- Peer review of workflows

### **Summative Assessment**
- Complete CI/CD pipeline project
- Written reflection on design decisions
- Oral presentation of pipeline architecture
- Individual contribution analysis (via Git commits)

### **Evaluation Criteria**
- **Technical Implementation (40%)**
  - Workflow correctness
  - Best practices followed
  - Security considerations

- **Understanding (30%)**
  - Ability to explain choices
  - Understanding of trade-offs
  - Problem-solving approach

- **Documentation (20%)**
  - Clear README
  - Workflow comments
  - System diagrams

- **Innovation (10%)**
  - Creative solutions
  - Optimization efforts
  - Going beyond requirements

---

## **Resources and References**

### **Official Documentation**
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)
- [Workflow syntax reference](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)

### **Tools**
- [Crontab Guru](https://crontab.guru/) - Cron schedule expressions
- [GitHub CLI (gh)](https://cli.github.com/)
- [Act](https://github.com/nektos/act) - Run GitHub Actions locally

### **Video Tutorials**
- GitHub Actions tutorial by TechWorld with Nana
- GitHub's official learning paths
- DevOps toolkit demonstrations

### **Books and Articles**
- The DevOps Handbook
- Continuous Delivery by Jez Humble
- GitHub Actions security best practices

### **Community**
- GitHub Community Discussions
- Stack Overflow `github-actions` tag
- DevOps subreddits

---

## **Teaching Tips**

### **Start Simple**
- Begin with hello world workflows
- Gradually introduce complexity
- Build on previous knowledge

### **Show Real Examples**
- Use real-world workflow files
- Analyze popular open-source projects
- Learn from mistakes (failed workflows)

### **Hands-On Learning**
- Live coding demonstrations
- Pair programming exercises
- Debugging sessions together

### **Emphasize Best Practices**
- Security from day one
- Documentation importance
- Code review culture

### **Connect to DevOps Culture**
- Not just tools, but philosophy
- Automation mindset
- Continuous improvement
- Blameless culture

### **Iterate and Improve**
- Start with basic pipelines
- Refine over time
- Learn from failures
- Optimize continuously

---

This comprehensive outline provides a complete roadmap for teaching GitHub Actions, from foundational concepts to advanced production patterns, preparing students for real-world DevOps workflows.
