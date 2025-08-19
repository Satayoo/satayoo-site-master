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

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React docu

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
