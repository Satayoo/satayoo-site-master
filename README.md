# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

## Deployment Options

Short answer: you **don't** run `npm install` "on the web." You either (a) push to GitHub and **Vercel runs it**, or (b) use a **cloud dev env** (Codespaces/StackBlitz) to run it, then push.

### Your options

1. **Standard (recommended)**
   - Edit locally → `npm install` → commit/push → Vercel auto builds & deploys.

2. **Web-only dev (no local)**
   - Open **GitHub Codespaces** (or StackBlitz) → run `npm install` in its terminal → commit/push → Vercel builds.

3. **CI-run (explicit)**
   Add a GitHub Action (if you want a CI step to run it):

```yaml
# .github/workflows/build.yml
name: build
on: [push, workflow_dispatch]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20', cache: 'npm' }
      - run: npm ci
      - run: npm run build
```

4. **Force redeploy (no code change)**
   - Use a **Vercel Deploy Hook** URL; hitting it triggers Vercel to pull repo and run `npm install` + build.

**Key idea:** your local clone is just a workspace.
**The always-online site = Vercel**, which installs deps during each deploy.

---

# Satayoo Website

This repository contains the source code for the Satayoo website. It is a React application bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Branching Strategy

- **main** — production-ready code. Deployments to the live website are built from this branch.
- **dev** — active development happens here. Pull requests and changes should be merged into this branch first. When changes are stable and tested, they can be merged into `main`.

## Continuous Integration / Continuous Deployment (CI/CD)

We use GitHub Actions (`.github/workflows/deploy.yml`) to automatically build and test the project on every push:

- **Development (`dev`) branch** — the workflow installs dependencies, runs tests and builds the project to ensure nothing is broken.
- **Production (`main`) branch** — in addition to building and testing, this job can trigger deployment to your hosting provider. Add your deployment commands/secrets to the workflow file (e.g., to deploy to Vercel, GitHub Pages or another platform).

## Project Structure

- `public/` — static assets such as HTML files and images. Partner logos live in `public/logos/`.
- `src/` — React components and application logic. The `App.tsx` file controls the layout of the main page.
- `.github/workflows/` — CI/CD pipeline definitions.
mentation](https://reactjs.org/).
