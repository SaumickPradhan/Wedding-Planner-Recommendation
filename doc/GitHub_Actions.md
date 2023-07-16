# Markdown File to Explain the GitHub Actions

This file documents and explains, in detail, the GitHub Actions that this project has.</br>
</br>

## Explanation of the `Track Repository Activity` GitHub Action

The workflow code, [linked here](https://github.com/EECE3093C/team-project-cyber-tech/blob/main/.github/workflows/track_repository_activity.yml), is also copied below for reference while reading this document:

```yaml
name: Track Repository Activity
run-name: ${{ github.actor }} has activity in the main branch

on:
  push:
    branches: [ main ]
  pull_request:
    types: [ opened, reopened, synchronize, closed ]
  issues:
    types: [ opened, closed ]

jobs:
  track-activity:
    runs-on: ubuntu-latest
    steps:
      - name: Set up Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '16'
      
      - name: Track push event
        uses: actions/github-script@v4
        with:
          script: |
            console.log(`Push event by ${context.actor} to ${context.payload.repository.full_name}`);
            if (context.payload.commits) {
              console.log(`Commits: ${JSON.stringify(context.payload.commits.map(commit => commit.message))}`);
            } else {
              console.log('No commits in this push event.');
            }

      - name: Track pull_request event
        uses: actions/github-script@v4
        with:
          script: |
            console.log(`Pull request event ${context.payload.action} by ${context.actor} in ${context.payload.repository.full_name}`);
            if (context.payload.pull_request) {
              console.log(`Pull request number: ${context.payload.pull_request.number}`);
              if (context.payload.pull_request.title) {
                console.log(`Title: ${context.payload.pull_request.title}`);
              } else {
                console.log('Pull request title not available.');
              }
              if (context.payload.pull_request.body) {
                console.log(`Body: ${context.payload.pull_request.body}`);
              } else {
                console.log('Pull request body not available.');
              }
            } else {
              console.log('Pull request not available.');
            }

      - name: Track issue event
        uses: actions/github-script@v4
        with:
          script: |
            console.log(`Issue event ${context.payload.action} by ${context.actor} in ${context.payload.repository.full_name}`);
            if (context.payload.issue) {
              console.log(`Issue number: ${context.payload.issue.number}`);
              if (context.payload.issue.title) {
                console.log(`Title: ${context.payload.issue.title}`);
              } else {
                console.log('Issue title not available.');
              }
              if (context.payload.issue.body) {
                console.log(`Body: ${context.payload.issue.body}`);
              } else {
                console.log('Issue body not available.');
              }
            } else {
              console.log('Issue not available.');
            }
  check-bats-version:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '14'
      - run: npm install -g bats
      - run: bats -v
      
```
</br>

The `Track Repository Activity` GitHub Action is intended to track repository activity by printing out messages to the console. 
It listens for push, pull request, and issue events and logs the relevant information when triggered. It is divided into several components, as follows: </br></br>

### Name and Run-Name

The `name` component specifies the name of the GitHub Action, while the `run-name` component specifies a custom name for the job that will be displayed in the Actions tab of the repository. </br>

```yaml
name: Track Repository Activity
run-name: ${{ github.actor }} has activity in the main branch
```

In this case, the `run-name` includes the name of the user who initiated the activity in the repository.

</br>

### Events

The `on` component specifies the events that will trigger the GitHub Action. </br>

```yaml
on:
  push:
    branches: [ main ]
  pull_request:
    types: [ opened, reopened, synchronize, closed ]
  issues:
    types: [ opened, closed ]
```

In this case, the GitHub Action will be triggered by any push requests to the _main_ branch, pull requests (opening, reopening, synchronizing, and closing), and issues (opening and closing). </br>
</br> The `branches: [ main ]` attribute specifies that the GitHub Action will only be triggered for events that occur on the main branch. 
The `types: [ opened, reopened, synchronize, closed ]` and `types: [ opened, closed ]` attributes restricts this action to only trigger for these specific types of pull request and issues events. 

</br>

### Jobs

The `jobs` component contains one or more jobs that the GitHub Action will perform. </br>

```yaml
jobs:
  track-activity:
    runs-on: ubuntu-latest
    steps:
      ...
  check-bats-version:
    runs-on: ubuntu-latest
    steps:
      ...
```

In this case, there are two jobs: `track-activity` and `check-bats-version`. 
The `runs-on` component specifies the environment in which the jobs will run, which is _**ubuntu-latest**_ in this case.

</br>

### The ```track-activity``` Job

The ```track-activity``` job runs on an _**ubuntu-latest**_ runner and contains a series of steps that track repository activity.

### Steps

The `steps` component contains the specific actions that the GitHub Action will perform. </br>

```yaml
steps:
      - name: Set up Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '16'
```

In this case, the first step is to set up **Node.js** by using the `actions/setup-node` action and specifying a version of `16`.

```yaml
      - name: Track push event
        uses: actions/github-script@v4
        with:
          script: |
            console.log(`Push event by ${context.actor} to ${context.payload.repository.full_name}`);
            if (context.payload.commits) {
              console.log(`Commits: ${JSON.stringify(context.payload.commits.map(commit => commit.message))}`);
            } else {
              console.log('No commits in this push event.');
            }
```

The second step is to track the ```push``` event by using the ```actions/github-script@v4``` action. The script component specifies the code that will be executed to track the ```push``` event. 
In this case, the code will log the name of the user who initiated the ```push``` event, as well as the commit messages associated with the ```push``` event, if available. 
If there are no commit messages associated with the ```push``` event, the code logs it too.

```yaml
      - name: Track pull_request event
        uses: actions/github-script@v4
        with:
          script: |
            console.log(`Pull request event ${context.payload.action} by ${context.actor} in ${context.payload.repository.full_name}`);
            if (context.payload.pull_request) {
              console.log(`Pull request number: ${context.payload.pull_request.number}`);
              if (context.payload.pull_request.title) {
                console.log(`Title: ${context.payload.pull_request.title}`);
              } else {
                console.log('Pull request title not available.');
              }
              if (context.payload.pull_request.body) {
                console.log(`Body: ${context.payload.pull_request.body}`);
              } else {
                console.log('Pull request body not available.');
              }
            } else {
              console.log('Pull request not available.');
            }
```

The third step is to track the ```pull_request``` event by using the ```actions/github-script@v4``` action. The script component specifies the code that will be executed to track the ```pull_request``` event. 
In this case, the code will log the name of the user who initiated the ```pull_request``` event, as well as the number of the pull-request (example: #61, #62), 
the title of the pull-request, and the body of the pull-request, if available.

```yaml
      - name: Track issue event
        uses: actions/github-script@v4
        with:
          script: |
            console.log(`Issue event ${context.payload.action} by ${context.actor} in ${context.payload.repository.full_name}`);
            if (context.payload.issue) {
              console.log(`Issue number: ${context.payload.issue.number}`);
              if (context.payload.issue.title) {
                console.log(`Title: ${context.payload.issue.title}`);
              } else {
                console.log('Issue title not available.');
              }
              if (context.payload.issue.body) {
                console.log(`Body: ${context.payload.issue.body}`);
              } else {
                console.log('Issue body not available.');
              }
            } else {
              console.log('Issue not available.');
            }
```

The fourth step is to track the ```issue``` event, using the ```actions/github-script@v4``` action to log information about ```issue``` events. 
The script component specifies the code that logs the type of ```issue``` event, the actor who triggered the event, and the repository name. 
It also checks whether an ```issue``` object is available in the payload, and logs additional information if it is. 
Specifically, it logs the issue number, title, and body, if they are available. If any of these values are not available, it logs a message indicating that they are not available.


</br>

### The ```check-bats-version``` Job

The ```check-bats-version``` job runs on an _**ubuntu-latest**_ runner and checks the version of the _**bats**_ testing framework that is installed on the runner.

### Steps

The `steps` component contains the specific actions that the GitHub Action will perform. </br>

```yaml
  check-bats-version:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '14'
      - run: npm install -g bats
      - run: bats -v
```
The specific actions performed by this job can be listed as follows: </br>
1. **Checkout:** The ```- uses: actions/checkout@v3``` step checks out the repository code on the virtual machine using the ```actions/checkout@v3``` action.
2. **Set up Node.js:** The ```- uses: actions/setup-node@v3
        with:
          node-version: '14'``` step sets up Node.js 14 on the virtual machine using the `actions/setup-node@v3` action.
3. **Install Bats:** The ```- run: npm install -g bats``` step installs the _**bats**_ command-line testing tool using the _**npm**_ package manager.
4. **Run Bats:** The ```- run: bats -v``` step runs the ```bats -v``` command to verify that the _**bats**_ command-line tool has been installed successfully.

</br>

## Conclusion
This GitHub Action has a simple workflow that tracks activity in the GitHub repository for our project and run tests on an Ubuntu virtual machine using Node.js and the _**bats**_ command-line tool.
