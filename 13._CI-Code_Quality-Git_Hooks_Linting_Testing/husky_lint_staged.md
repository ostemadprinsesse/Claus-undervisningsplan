For **Node.js** applications, you can use **[husky](https://typicode.github.io/husky/)** and **[lint-staged](https://github.com/okonet/lint-staged)** to achieve similar functionality to `pre-commit` in Python. These tools allow you to run scripts (like linting and testing) automatically before commits or pushes, using Git hooks.

---

## **1. Husky**
Husky is a popular tool for managing Git hooks in Node.js projects. It makes it easy to add and configure hooks.

### **Installation**
```bash
npm install husky --save-dev
```
Then, enable Git hooks:
```bash
npx husky install
```
To automatically set up hooks for new contributors, add this to your `package.json`:
```json
{
  "scripts": {
    "prepare": "husky install"
  }
}
```

### **Adding a Hook**
To add a `pre-commit` hook:
```bash
npx husky add .husky/pre-commit "npm test"
```
This will create a `.husky/pre-commit` file with the command `npm test`.

---

## **2. lint-staged**
lint-staged allows you to run scripts on staged files (only the files you’re about to commit). This is useful for running linters or formatters only on changed files, which is much faster.

### **Installation**
```bash
npm install lint-staged --save-dev
```

### **Configuration**
Add a `lint-staged` configuration to your `package.json`:
```json
{
  "lint-staged": {
    "*.{js,jsx,ts,tsx}": [
      "eslint --fix",
      "prettier --write"
    ]
  }
}
```
Then, update your `pre-commit` hook to use `lint-staged`:
```bash
npx husky add .husky/pre-commit "npx lint-staged"
```

---

## **3. Example: Linting and Testing**
Here’s how you can set up both **linting** and **testing** for a Node.js project:

### **Install Dependencies**
```bash
npm install eslint prettier husky lint-staged --save-dev
```

### **Configure ESLint and Prettier**
- Set up `.eslintrc.js` and `.prettierrc` as needed.

### **Update `package.json`**
```json
{
  "scripts": {
    "prepare": "husky install",
    "lint": "eslint .",
    "test": "jest"
  },
  "lint-staged": {
    "*.{js,jsx,ts,tsx}": [
      "eslint --fix",
      "prettier --write"
    ]
  }
}
```

### **Set Up Husky Hooks**
```bash
npx husky add .husky/pre-commit "npx lint-staged"
npx husky add .husky/pre-push "npm test"
```

---

## **Summary Table**


Node.js Git Hooks Setup


| Tool         | Purpose                          | Command to Install/Enable       |
|--------------|----------------------------------|----------------------------------|
| husky        | Manage Git hooks                 | `npm install husky --save-dev`  |
| lint-staged  | Run scripts on staged files      | `npm install lint-staged --save-dev` |
| ESLint       | Lint JavaScript/TypeScript       | `npm install eslint --save-dev` |
| Prettier     | Format code                      | `npm install prettier --save-dev` |

---

### **Key Benefits**
- **Husky:** Easy to set up and manage Git hooks.
- **lint-staged:** Run scripts only on staged files, improving performance.
- **ESLint/Prettier:** Standard tools for linting and formatting Node.js code.

