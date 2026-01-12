# Learning Goals: IT Architecture - Agile Development Course

Based on comprehensive analysis of the **Kea IT-Arkitektur - Agil Udvikling 2024 Spring** course repository.

---

## **1. Version Control & Collaboration (Git & GitHub)**

### **Foundational Skills:**
- Use Git for version control (clone, commit, push, pull)
- Navigate Git history and understand commit SHAs
- Configure `.gitignore` files for proper file management
- Understand what files should never be committed (secrets, OS files, IDE configs)

### **Advanced Collaboration:**
- Create and manage Git branches effectively
- Resolve merge conflicts manually
- Use Git stash for temporary work storage
- Apply different branching strategies (Feature Branching, Gitflow, Trunk-based Development)
- Create and review Pull Requests professionally
- Understand merge vs. rebase workflows
- Use squash commits for cleaner history
- Create annotated tags and GitHub Releases with semantic versioning
- Implement Git hooks for quality enforcement

## **2. DevOps Culture & Philosophy**

### **Conceptual Understanding:**
- Explain the historical evolution from Waterfall to Agile to DevOps
- Understand the Dev vs. Ops paradigm and how DevOps bridges them
- Apply the DevOps 8 framework principles
- Differentiate between Continuous Integration, Continuous Delivery, and Continuous Deployment
- Critically analyze Agile methodology adoption challenges in organizations
- Understand the business value of DevOps practices

### **Cultural Competencies:**
- Embrace automation and "infrastructure as code" mindset
- Practice "making work visible" through status badges and monitoring
- Apply continuous improvement principles
- Understand organizational challenges (culture clash, silos) in DevOps adoption

## **3. Terminal & Command Line Proficiency**

### **Basic Operations:**
- Navigate file systems using `pwd`, `cd`, `ls`
- Create, move, copy, and delete files/directories
- Read file contents with `cat` and text editors
- Understand differences between *nix and Windows terminals

### **Text Editors:**
- Use Nano for simple editing tasks
- Understand Vim modes (Normal, Insert, Visual, Command)
- Perform basic text manipulation in terminal environments

### **Advanced Tools:**
- Use `jq` for JSON processing
- Use GitHub CLI (`gh`) for repository management
- Apply cross-platform file naming best practices

## **4. Configuration & Data Formats**

### **YAML:**
- Write syntactically correct YAML files
- Understand indentation and data structure rules
- Create configuration files for CI/CD workflows

### **Markdown:**
- Format documentation with headers, lists, emphasis
- Insert links, images, and code blocks
- Create professional README files and documentation

### **JSON:**
- Understand JSON structure
- Process JSON data programmatically

## **5. CI/CD Pipeline Development**

### **GitHub Actions:**
- Understand workflows, jobs, steps, and runners
- Create automated workflows triggered by events
- Use GitHub Actions Marketplace
- Access GitHub context and metadata
- Use secrets (GITHUB_TOKEN) securely
- Implement matrix builds for multi-version testing
- Configure workflow permissions properly

### **Continuous Integration:**
- Set up automated testing for Node.js applications
- Use `npm ci` for reproducible builds
- Implement linting with ESLint/Standard.js
- Use Super Linter for multi-language projects
- Create status badges for repository visibility

### **Quality Gates:**
- Configure branch protection rules
- Require status checks before merging
- Mandate code reviews
- Use pull request templates

## **6. Build Tools & Package Management**

### **Cross-Platform Package Managers:**
- Use Chocolatey (Windows), Homebrew (macOS), apt (Linux)
- Understand OS-level vs. language-specific package managers

### **Language-Specific Tools:**
- Work with npm and `package.json`
- Understand pip, cargo, go mod, maven/gradle equivalents
- Use PM2 for production Node.js process management

## **7. Cloud Computing (Microsoft Azure Focus)**

### **Cloud Fundamentals:**
- Differentiate between SaaS, PaaS, IaaS, FaaS, DaaS, STaaS
- Understand public, private, and hybrid cloud deployments
- Navigate Azure regions and data centers
- Manage Azure resource groups
- Monitor and optimize cloud costs

### **Virtual Machines:**
- Create and configure Ubuntu VMs on Azure
- Generate and use SSH keys (RSA 4096-bit) securely
- Configure network security (inbound/outbound port rules)
- Assign static IP addresses
- Install runtime environments (Node.js via nvm, MySQL)

### **Networking:**
- Understand Virtual Networks (VPC/VNET)
- Configure private and public subnets
- Use Network Access Control Lists (NACL) and Security Groups
- Work with Internet Gateways, NAT, VPC Peering
- Understand Load Balancers (NLB, ALB)

### **Azure Storage:**
- Work with Azure Blob Storage and containers
- Manage access control (Anonymous, Azure AD, SAS tokens)
- Generate and use Shared Access Signatures (SAS)
- Compare with AWS S3

### **Serverless Computing:**
- Create Azure Functions
- Understand triggers and bindings
- Compare serverless subscription models (Consumption, Premium, App Service)
- Handle cold start performance considerations
- Develop and test Azure Functions locally

### **Azure Services:**
- Use Azure Key Vault for secrets management
- Work with Azure Service Bus (Queues and Topics)
- Use Azure SQL Database
- Understand Azure CDN, VPN Gateways, API Gateways
- Use Azure CLI (`az`) for infrastructure management

## **8. Software Architecture Patterns**

### **Architectural Decisions:**
- Compare monolithic vs. microservices architectures
- Evaluate monorepo vs. polyrepo strategies
- Understand internal communication patterns in distributed systems
- Make informed architecture choices based on project needs

## **9. Professional Development Practices**

### **Code Quality:**
- Implement and enforce linting standards
- Use pre-commit hooks for quality checks
- Write meaningful commit messages
- Perform thorough code reviews
- Create comprehensive issue and PR templates

### **Project Management:**
- Use GitHub Projects with Kanban boards
- Track issues effectively
- Organize work into manageable tasks
- Document decisions and progress

### **Security:**
- Never commit secrets or sensitive data
- Use environment variables and secrets management
- Generate and manage SSH keys properly
- Apply least-privilege access principles
- Use SAS tokens with appropriate permissions and expiration

## **10. Automation & Infrastructure**

### **Infrastructure as Code (IaC):**
- Understand different infrastructure management approaches (Console UI, CLI/API, SDK/CDK, IaC)
- Use Vagrant for local VM provisioning
- Automate infrastructure setup and teardown

### **Deployment Automation:**
- Deploy applications to cloud VMs
- Automate release processes
- Create automated release notes
- Implement continuous deployment pipelines

## **11. Problem-Solving & Debugging**

### **Technical Skills:**
- Troubleshoot merge conflicts
- Debug CI/CD pipeline failures
- Diagnose cloud deployment issues
- Navigate complex technical documentation
- Research and evaluate technical solutions independently

### **Growth Mindset:**
- Progress from following single solutions to exploring multiple approaches
- Handle increasing complexity throughout the semester
- Build resilience in debugging difficult problems
- Learn to fail fast and iterate

## **12. Team Collaboration**

### **Communication:**
- Use version control for team coordination
- Write clear PR descriptions and commit messages
- Provide constructive code review feedback
- Document decisions for team visibility

### **Workflow Practices:**
- Follow established branching strategies
- Respect code review processes
- Use issue tracking for accountability
- Collaborate through GitHub Projects

---

## **Meta-Learning Goals**

Beyond technical skills, students would develop:

- **Self-directed learning**: Progress from guided exercises to independent problem-solving
- **Tool proficiency**: Comfort with professional developer toolchain
- **Industry readiness**: Exposure to real-world DevOps practices used in software companies
- **Cross-platform awareness**: Understanding of Windows, macOS, and Linux environments
- **Cost consciousness**: Awareness of cloud resource costs and optimization
- **Documentation skills**: Ability to create and maintain professional technical documentation
- **Critical thinking**: Evaluating trade-offs between different technical approaches
- **Integration thinking**: Understanding how DevOps supports broader IT architecture goals

---

## **Course Overview**

### **Course Details**
- **Course Name:** Agil Udvikling (Agile Development)
- **Institution:** KEA (Copenhagen School of Design and Technology)
- **Program:** IT-Arkitektur (IT Architecture)
- **Semester:** Spring 2024
- **Duration:** 6 weeks (January 30th - March 19th, 2024)

### **Module Structure**

**Module 1: Introduction (Week 1)**
- Git and GitHub fundamentals
- DevOps Introduction
- CI/CD/CD Fundamentals
- YAML and Terminal Commands

**Module 2: Agile (Week 2)**
- Agile Methodology
- DevOps Deep Dive
- Markdown
- Build Tools and Package Managers

**Module 3: GitHub Actions (Week 3)**
- Git Branching
- GitHub Actions Fundamentals
- CI/CD Platforms Comparison
- Workflow Creation

**Module 4: Continuous Integration (Week 4)**
- Git Tagging and Releases
- Branching Strategies
- Monorepos
- Linting and Quality Control

**Module 5: Cloud (Week 5)**
- Cloud Providers and Models
- Azure Fundamentals
- Virtual Machines and Networking
- Serverless Computing

### **Course Philosophy**

The course follows a deliberate progression model:

| Aspect | Beginning | End of Semester |
|--------|-----------|-----------------|
| Reading | First two weeks only | None |
| Workload | High | None (focus on exam project) |
| Knowledge Acquisition | Many new things | Cementing knowledge |
| Topic Complexity | Shallow | Complex |
| Solution Space | One way | Large number of solutions |
| Ease of Debugging | Easy | Very hard |

**Key Course Values:**
- Hands-on learning over theory
- Early problem detection (fail fast)
- Creating value for users
- Infrastructure automation
- Reproducibility
- Security consciousness
- Professional best practices

---

This course provides a comprehensive foundation in modern DevOps practices, preparing students for professional software development environments where automation, collaboration, and cloud infrastructure are essential daily skills.

---

## **Learning Goals Mind Maps**

### **1. Version Control & Git Mind Map**

```mermaid
mindmap
  root((Version Control<br/>& Git))
    Foundational Skills
      Git Basics
        clone
        commit
        push
        pull
      .gitignore
        Configuration
        File exclusion rules
      Git History
        Navigate commits
        Commit SHAs
        Understanding history
      File Management
        Never commit secrets
        No OS files
        No IDE configs
    Advanced Collaboration
      Branching
        Create branches
        Switch branches
        Manage branches
      Merge Strategies
        Merge conflicts
        Conflict resolution
        Merge vs Rebase
      Git Stash
        Temporary storage
        Work preservation
      Pull Requests
        Create PRs
        Review PRs
        Professional workflow
      Branching Strategies
        Feature Branching
        Gitflow
        Trunk-based Development
      Commit Management
        Squash commits
        Cleaner history
        Meaningful messages
      Releases
        Annotated tags
        Semantic versioning
        GitHub Releases
      Quality Enforcement
        Git hooks
        Pre-commit hooks
        Automated checks
```

### **2. DevOps Culture & Philosophy Mind Map**

```mermaid
mindmap
  root((DevOps Culture<br/>& Philosophy))
    Conceptual Understanding
      Historical Evolution
        Waterfall model
        Agile methodology
        DevOps emergence
      Dev vs Ops Paradigm
        Traditional separation
        DevOps bridge
        Unified approach
      DevOps 8 Framework
        Framework principles
        Implementation
      CI/CD/CD
        Continuous Integration
        Continuous Delivery
        Continuous Deployment
        Pipeline concepts
      Agile Challenges
        Adoption issues
        Organizational resistance
        Culture clash
      Business Value
        Value delivery
        Customer focus
        ROI understanding
    Cultural Competencies
      Automation Mindset
        Infrastructure as Code
        Automate everything
        Reduce manual work
      Making Work Visible
        Status badges
        Monitoring
        Transparency
      Continuous Improvement
        Iterative progress
        Learn from failures
        Kaizen approach
      Organizational Challenges
        Siloed teams
        Culture clash
        Change management
        Breaking barriers
```

### **3. Terminal & Command Line Proficiency Mind Map**

```mermaid
mindmap
  root((Terminal & CLI<br/>Proficiency))
    Basic Operations
      File Navigation
        pwd
        cd
        ls
      File Manipulation
        Create files touch
        Move files mv
        Copy files cp
        Delete files rm
      Directory Management
        mkdir
        rmdir
      Read Files
        cat
        Text editor viewing
      Platform Differences
        nix terminals
        Windows terminals
        Cross-platform awareness
    Text Editors
      Nano
        Simple editing
        Basic commands
        Beginner friendly
      Vim
        Normal mode
        Insert mode
        Visual mode
        Command mode
        Advanced editing
      Terminal Manipulation
        Efficient editing
        Keyboard shortcuts
    Advanced Tools
      jq
        JSON processing
        Query JSON data
        Transform data
      GitHub CLI gh
        Repository management
        PR management
        Issue handling
        Automation
      Best Practices
        Cross-platform naming
        File conventions
        Hidden files awareness
```

### **4. Configuration & Data Formats Mind Map**

```mermaid
mindmap
  root((Configuration<br/>& Data Formats))
    YAML
      Syntax
        Indentation rules
        Data structure
        Key-value pairs
      Use Cases
        CI/CD workflows
        Configuration files
        Docker Compose
      Best Practices
        Consistent formatting
        Comments
        Validation
    Markdown
      Documentation
        Headers
        Lists
        Emphasis
        Links
      Code Blocks
        Inline code
        Fenced blocks
        Syntax highlighting
      Images
        Image insertion
        Alt text
      Professional Use
        README files
        Project documentation
        Wiki pages
    JSON
      Structure
        Objects
        Arrays
        Key-value pairs
        Data types
      Programmatic Processing
        Parsing
        Generation
        Transformation
      Use Cases
        API responses
        Configuration
        Data exchange
```

### **5. CI/CD Pipeline Development Mind Map**

```mermaid
mindmap
  root((CI/CD Pipeline<br/>Development))
    GitHub Actions
      Core Concepts
        Workflows
        Jobs
        Steps
        Runners
      Workflow Creation
        YAML syntax
        Event triggers
        workflow_dispatch
      Actions Marketplace
        Reusable actions
        Community actions
        Action integration
      GitHub Context
        Metadata access
        github object
        Environment variables
      Secrets Management
        GITHUB_TOKEN
        Secure storage
        Access control
      Matrix Builds
        Multi-version testing
        Parallel execution
      Permissions
        Workflow permissions
        Token scopes
    Continuous Integration
      Automated Testing
        Node.js testing
        Test frameworks
        Test automation
      Build Process
        npm ci
        Reproducible builds
        Dependency management
      Linting
        ESLint
        Standard.js
        Super Linter
        Multi-language support
      Visibility
        Status badges
        Build status
        Quality metrics
    Quality Gates
      Branch Protection
        Protection rules
        Required checks
        Status enforcement
      Code Reviews
        Required reviewers
        Review process
        Approval workflow
      PR Templates
        Standardized format
        Checklists
        Consistent information
      Status Checks
        Automated checks
        Manual approvals
        Quality enforcement
```

### **6. Build Tools & Package Management Mind Map**

```mermaid
mindmap
  root((Build Tools &<br/>Package Management))
    Cross-Platform Package Managers
      Windows
        Chocolatey
        Package installation
        System-wide tools
      macOS
        Homebrew
        Cask support
        Formula management
      Linux
        apt Debian/Ubuntu
        yum RHEL/CentOS
        pacman Arch
      Understanding
        OS-level managers
        vs Language-specific
        Use cases
    Language-Specific Tools
      Node.js
        npm
        package.json
        Dependencies
        Scripts
      Python
        pip
        requirements.txt
        Virtual environments
      Other Languages
        cargo Rust
        go mod Go
        maven/gradle Java
      Production Management
        PM2
        Process management
        Node.js apps
        Monitoring
```

### **7. Cloud Computing (Azure) Mind Map**

```mermaid
mindmap
  root((Cloud Computing<br/>Microsoft Azure))
    Cloud Fundamentals
      Service Models
        SaaS Software as a Service
        PaaS Platform as a Service
        IaaS Infrastructure as a Service
        FaaS Function as a Service
        DaaS Desktop as a Service
        STaaS Storage as a Service
      Deployment Models
        Public cloud
        Private cloud
        Hybrid cloud
      Azure Basics
        Regions
        Data centers
        Resource groups
      Cost Management
        Cost monitoring
        Budget alerts
        Optimization
    Virtual Machines
      VM Creation
        Ubuntu VMs
        VM configuration
        Instance types
      Security
        SSH keys
        RSA 4096-bit
        Key management
      Network Security
        Inbound rules
        Outbound rules
        Port management
      Networking
        Static IP addresses
        DNS configuration
      Runtime Setup
        Node.js via nvm
        MySQL installation
        Application deployment
    Networking
      Virtual Networks
        VPC/VNET
        Network isolation
        IP addressing
      Subnets
        Private subnets
        Public subnets
        Subnet design
      Security
        NACL
        Security Groups
        Firewall rules
      Gateways
        Internet Gateway
        NAT Gateway
        VPC Peering
      Load Balancing
        Network Load Balancer
        Application Load Balancer
        Traffic distribution
    Azure Storage
      Blob Storage
        Containers
        Blobs
        Storage tiers
      Access Control
        Anonymous access
        Azure AD
        SAS tokens
      SAS Tokens
        Token generation
        Permissions
        Expiration
      Comparison
        AWS S3 comparison
        Use cases
    Serverless Computing
      Azure Functions
        Function creation
        Event-driven
        Scaling
      Triggers & Bindings
        HTTP triggers
        Queue triggers
        Input/Output bindings
      Subscription Models
        Consumption plan
        Premium plan
        App Service plan
      Performance
        Cold starts
        Warm instances
        Optimization
      Development
        Local development
        Testing tools
        Debugging
    Azure Services
      Azure Key Vault
        Secrets management
        Key management
        Certificate storage
      Service Bus
        Queues
        Topics
        Messaging patterns
      Azure SQL Database
        Managed database
        Scaling
        Backup
      Other Services
        Azure CDN
        VPN Gateways
        API Gateways
      Azure CLI
        az commands
        Infrastructure management
        Automation
```

### **8. Software Architecture Patterns Mind Map**

```mermaid
mindmap
  root((Software<br/>Architecture Patterns))
    Architectural Decisions
      Monolithic Architecture
        Single codebase
        Tight coupling
        Simpler deployment
        Pros & cons
      Microservices Architecture
        Distributed services
        Loose coupling
        Independent scaling
        Pros & cons
      Comparison
        When to use each
        Migration strategies
        Trade-offs
      Repository Strategies
        Monorepo
        Polyrepo
        Advantages/disadvantages
      Communication Patterns
        Internal APIs
        Message queues
        Event-driven
        Synchronous vs Asynchronous
      Project-Based Choices
        Context matters
        Team size
        Scalability needs
        Maintenance considerations
```

### **9. Professional Development Practices Mind Map**

```mermaid
mindmap
  root((Professional<br/>Development Practices))
    Code Quality
      Linting
        Linting standards
        ESLint/Standard.js
        Consistent style
      Pre-commit Hooks
        Quality checks
        Automated validation
        Prevent bad commits
      Code Reviews
        Thorough reviews
        Constructive feedback
        Knowledge sharing
      Commit Messages
        Meaningful messages
        Conventional commits
        Clear history
      Templates
        Issue templates
        PR templates
        Standardization
    Project Management
      GitHub Projects
        Project boards
        Kanban workflow
        Visual organization
      Issue Tracking
        Effective tracking
        Prioritization
        Assignment
      Task Organization
        Manageable tasks
        Sprint planning
        Backlog management
      Documentation
        Decision documentation
        Progress tracking
        Knowledge base
    Security
      Secrets Management
        Never commit secrets
        Environment variables
        Key Vault usage
      SSH Keys
        Key generation
        Secure storage
        Proper usage
      Access Control
        Least-privilege principle
        Role-based access
        Permission management
      Token Management
        SAS tokens
        Expiration
        Scope limitation
```

### **10. Automation & Infrastructure Mind Map**

```mermaid
mindmap
  root((Automation &<br/>Infrastructure))
    Infrastructure as Code
      Management Approaches
        Console UI
        CLI/API
        SDK/CDK
        IaC frameworks
      Local Provisioning
        Vagrant
        VirtualBox
        Development environments
      Automation Benefits
        Reproducibility
        Version control
        Documentation
        Consistency
      Infrastructure Setup
        Automated setup
        Configuration management
        Teardown automation
    Deployment Automation
      Cloud Deployment
        VM deployment
        Application deployment
        Configuration automation
      Release Automation
        Automated releases
        Release notes
        Version management
      CD Pipelines
        Continuous deployment
        Automated testing
        Production deployment
        Rollback strategies
      Monitoring
        Deployment monitoring
        Health checks
        Alert configuration
```

### **11. Problem-Solving & Debugging Mind Map**

```mermaid
mindmap
  root((Problem-Solving<br/>& Debugging))
    Technical Skills
      Merge Conflicts
        Conflict identification
        Resolution strategies
        Testing after resolution
      CI/CD Debugging
        Pipeline failures
        Log analysis
        Workflow debugging
      Cloud Troubleshooting
        Deployment issues
        Network problems
        Resource constraints
      Documentation Navigation
        Reading docs
        Finding solutions
        API references
      Independent Research
        Solution evaluation
        Technology comparison
        Best practices
    Growth Mindset
      Multiple Approaches
        Single to multiple solutions
        Exploring alternatives
        Creative thinking
      Increasing Complexity
        Progressive difficulty
        Handling complexity
        Breaking down problems
      Resilience
        Debugging persistence
        Learning from failures
        Problem ownership
      Fail Fast Iterate
        Quick feedback
        Rapid iteration
        Continuous learning
```

### **12. Team Collaboration Mind Map**

```mermaid
mindmap
  root((Team<br/>Collaboration))
    Communication
      Version Control Coordination
        Shared repository
        Coordination through Git
        Avoiding conflicts
      PR Descriptions
        Clear descriptions
        Context provision
        Change explanation
      Code Review Feedback
        Constructive feedback
        Specific suggestions
        Learning opportunities
      Documentation
        Team visibility
        Decision records
        Knowledge sharing
    Workflow Practices
      Branching Strategies
        Team agreements
        Strategy adherence
        Consistent workflow
      Review Processes
        Respect review time
        Address feedback
        Quality focus
      Issue Tracking
        Accountability
        Progress visibility
        Assignment clarity
      GitHub Projects
        Collaboration boards
        Shared visibility
        Team coordination
```

### **13. Meta-Learning Goals Mind Map**

```mermaid
mindmap
  root((Meta-Learning<br/>Goals))
    Self-Directed Learning
      Guided to independent
      Problem-solving autonomy
      Research skills
    Tool Proficiency
      Professional toolchain
      Developer workflows
      Productivity tools
    Industry Readiness
      Real-world practices
      Professional standards
      Job preparation
    Cross-Platform Awareness
      Windows
      macOS
      Linux
      Platform differences
    Cost Consciousness
      Cloud costs
      Resource optimization
      Budget awareness
    Documentation Skills
      Technical writing
      Professional docs
      Maintenance
    Critical Thinking
      Trade-off evaluation
      Decision making
      Technical judgment
    Integration Thinking
      DevOps & IT Architecture
      System thinking
      Holistic approach
```
