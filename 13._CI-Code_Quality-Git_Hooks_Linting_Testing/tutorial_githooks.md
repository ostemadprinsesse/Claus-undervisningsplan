# Tutorial: Git Hooks

## Introduction
Git hooks are scripts that run automatically before or after specific Git events such as commits, pushes, and merges. They help enforce coding standards and catch issues early in the development process.

---

## Step 1: Initialize a Git Repository
Before creating a Git hook, ensure you have a Git repository initialized:

```bash
$ git init
```

---

## Step 2: Create Your First Git Hook
Git hooks are stored in the `.git/hooks` directory. Let's create a simple `pre-commit` hook:

1. Navigate to the `.git/hooks` folder:
   ```bash
   $ cd .git/hooks
   ```

2. Create a file named `pre-commit`:
   ```bash
   $ touch pre-commit
   ```

3. Add an echo statement to the file:
   ```bash
   $ echo "Hello, world!" > pre-commit
   ```

4. Make the file executable:
   ```bash
   $ chmod +x pre-commit
   ```

5. Try to commit and see the result:
   ```bash
   $ git add .
   $ git commit -m "Test commit"
   ```

You should see the message "Hello, world!" displayed before the commit proceeds.

---

## Step 3: Add a Linter to Your Hook
Let's integrate a linter like `Standard` to enforce code style. First, install `Standard` globally:

```bash
$ npm install -g standard
```

Now, replace the content of the `pre-commit` file with the following script:

```bash
#!/bin/sh

# Get the list of staged JavaScript files
git diff --name-only --cached --relative | grep -E '\.jsx?$' | while read -r file; do
  # Run Standard on each file
  npx standard "$file"
  
  # If Standard fails, exit with an error
  if [ $? -ne 0 ]; then
    echo "JavaScript Standard Style errors were detected in $file. Aborting commit."
    exit 1
  fi
done
```

---

## Step 4: Test the Hook
1. Stage a JavaScript file with incorrect formatting:
   ```bash
   $ git add example.js
   ```

2. Attempt to commit:
   ```bash
   $ git commit -m "Test linter"
   ```

If the file does not meet the `Standard` style guidelines, the commit will be aborted, and you will see an error message.

---

## Step 5: Bypass the Hook (If Needed)
If you need to bypass the hook for a specific commit, use the `--no-verify` flag:

```bash
$ git commit --no-verify -m "Bypass hook"
```

---

## Pros and Cons of Git Hooks

### Pros
- **Early Error Detection**: Catch issues before they enter the repository.
- **Immediate Feedback**: Developers receive instant feedback on their code.
- **Prevent Bad Commits**: Ensure only high-quality code is committed.

### Cons
- **Local Only**: Hooks are not version-controlled and must be manually configured on each machine.
- **Manual Configuration**: Each developer must set up hooks individually.
- **Bypassable**: Developers can bypass hooks using the `--no-verify` flag.
- **Cross-Platform Issues**: Bash scripts may not work on all operating systems (e.g., Windows).

---

## Advanced Tools

### Pre-commit Library
The `pre-commit` library simplifies managing Git hooks:
- [pre-commit.com](https://pre-commit.com/)

### Devenv
`Devenv` provides built-in support for Git hooks:
- [devenv.sh](https://devenv.sh/)

---

## Conclusion
Git hooks are a powerful tool for enforcing code quality and catching issues early. While they require manual setup and are local to each machine, they provide immediate feedback and help maintain a high standard of code.
