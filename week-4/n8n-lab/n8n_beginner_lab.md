# n8n Beginner Self-Paced Lab

Welcome to the n8n Beginner Lab! This self-paced workshop will introduce you to workflow automation using n8n. By the end of this lab, you'll understand core concepts and build your first automation workflows.

## Prerequisites

- Basic familiarity with APIs and webhooks (helpful but not required)
- Access to a web browser
- A free n8n Cloud account or local n8n instance
- [n8n Quick Start Tutorial: Build Your First Workflow [2025]](https://www.youtube.com/watch?v=4cQWJViybAQ&list=PLlET0GsrLUL5HKJk1rb7t32sAs_iAlpZe)

## What is n8n?

n8n is an open-source workflow automation platform that connects different applications and services. Instead of writing code, you build visual workflows using nodes to automate repetitive tasks.

## Lab Structure

This lab is divided into self-contained sections. You can work through them sequentially or skip to sections that interest you most.

---

## Section 1: Getting Started with n8n

### Objectives

- Set up your n8n environment
- Understand the n8n interface
- Create your first simple workflow

### Tasks

1. **Set up n8n**

   - Visit https://app.n8n.cloud or set up a local instance
   - Create an account and log in
   - Explore the dashboard

2. **Explore the Interface**

   - Locate the workflow canvas (center area)
   - Find the node library (left sidebar)
   - Check out the execution history (bottom panel)
   - Navigate to the credentials section (Settings > Credentials)

3. **Create Your First Workflow**
   - Click "New Workflow"
   - Add a "Start" node (trigger)
   - Add a "Debug" node
   - Connect them together
   - Click the play button to test
   - Observe the output in the execution history

**Expected Result:** You should see output in the Debug node showing the execution data.

---

## Section 2: Working with Nodes and Connections

### Objectives

- Understand different node types
- Learn how to connect nodes
- Pass data between nodes

### Concepts

Nodes are building blocks in n8n workflows. Common types include:

**Trigger nodes:** Start a workflow (Webhook, Schedule, Manual, etc.)

**Action nodes:** Perform tasks (HTTP Request, Send Email, etc.)

**Data transformation:** Manipulate and format data (Function, Set, Switch, etc.)

**Conditional nodes:** Make decisions based on data

### Tasks

1. **Build a Data Transformation Workflow**

   - Start with a "Start" trigger node
   - Add a "Set" node to create sample data
     - In the "Set" section, add a property: name with value John
     - Add another property: email with value john@example.com
   - Add a "Debug" node to see the output
   - Execute and observe the data structure

2. **Use a Function Node**
   - Add a "Function" node after your Set node
   - Write JavaScript to transform data:

```javascript
return [
  {
    ...item,
    name: item.data.name.toUpperCase(),
    greeting: `Hello, ${item.data.name}!`,
  },
];
```

- Connect it to Debug and execute
- Notice how the data has been transformed

3. **Experiment with Node Connections**
   - Try adding multiple output paths from a single node
   - Use a "Switch" node to route data conditionally
   - Observe how data flows through different paths

**Expected Result:** You understand how data moves through workflows and can transform it using nodes.

---

## Section 3: Working with APIs and HTTP Requests

### Objectives

- Make HTTP requests to external APIs
- Handle API responses
- Work with public APIs

### Tasks

1. **Make a Simple GET Request**

   - Create a new workflow
   - Add a "Webhook" trigger (Manual Trigger option)
   - Add an "HTTP Request" node
     - Set Method to "GET"
     - Use this URL: https://jsonplaceholder.typicode.com/posts/1
   - Add a Debug node to see the response
   - Execute and explore the data structure

2. **Parse and Transform API Data**

   - After the HTTP Request node, add a "Set" node
   - Extract specific fields from the API response:
     - title from the POST data
     - userId from the POST data
   - Add a Debug node to verify
   - Execute and check the extracted data

3. **Fetch Multiple Records**
   - Modify the HTTP Request URL to: https://jsonplaceholder.typicode.com/posts?_limit=5
   - Add a "Function" node to process the array of posts
   - Extract just the titles and IDs
   - Use Debug to see the results

**Expected Result:** You can retrieve data from APIs and transform the responses into usable formats.

---

## Section 4: Building a Practical Workflow

### Objectives

- Combine multiple concepts into a real workflow
- Use conditional logic
- Work with data processing

### Workflow: Simple Lead Alert System

This workflow checks for new leads and sends notifications for high-priority leads.

1. **Set Up the Trigger and Sample Data**
   - Create a new workflow
   - Start with a "Webhook" trigger
   - Add a "Set" node with sample lead data:

Property: lead
Value: { "name": "Alice Smith", "email": "alice@example.com", "budget": 50000, "priority": "high" }

2. **Add Conditional Logic**

   - Add a "Switch" node after Set
   - Configure it to check if lead.priority === "high"
   - Create two paths: one for high priority, one for others
   - Add Debug nodes to each path

3. **Format Output Data**
   - On the high priority path, add a "Set" node
   - Format a notification message:

Property: notification
Value: New high-priority lead: Alice Smith (Budget: $50000)

- Add a Debug node to verify

4. **Test the Workflow**
   - Execute the workflow
   - Verify the high-priority path is triggered
   - Change the priority to "low" and test again

**Expected Result:** Your workflow correctly identifies high-priority leads and formats appropriate messages.

---

## Section 5: Connecting to Real Services

### Objectives

- Authenticate with external services
- Send data to real applications
- Create an end-to-end automation

### Tasks

1. **Send an Email (Requires Setup)**

   - Create a new workflow
   - Add a Manual Trigger
   - Add an "Email Send" node
   - Click to create credentials for your email provider
   - Follow the authentication flow
   - Configure the email:
     - To: your email address
     - Subject: Test from n8n
     - Text: This is an automated message
   - Execute and check your inbox

2. **Create a Slack Integration** (Optional)

   - Add a new workflow
   - Trigger with Manual Trigger
   - Add a "Slack" node (send message)
   - Set up Slack credentials
   - Configure the message and channel
   - Execute and verify in Slack

3. **Combine Services**
   - Create a workflow that:
     - Receives data from a webhook
     - Processes the data
     - Sends an email notification
     - Sends a Slack message
   - Test with sample data

**Expected Result:** You can authenticate with external services and automate actions across multiple platforms.

---

## Section 6: Scheduling and Automation

### Objectives

- Schedule workflows to run automatically
- Use cron expressions for timing
- Automate recurring tasks

### Tasks

1. **Create a Scheduled Workflow**

   - Create a new workflow
   - Use a "Schedule" trigger instead of Manual
   - Set it to run "Every day" at 9:00 AM
   - Add a "Debug" node with a message: Daily job executed
   - Save the workflow
   - Note: In free tier, this will run at the configured time

2. **Understand Cron Expressions**

   - Experiment with different schedule options
   - Try: Every weekday at 9 AM
   - Try: Every Monday and Wednesday at 2 PM
   - Try: Every hour (useful for monitoring tasks)

3. **Build a Monitoring Workflow**
   - Use a "Schedule" trigger set to every 30 minutes
   - Add an HTTP Request to check a public API status
   - Add conditional logic to alert if something is down
   - Use Debug to simulate the alert

**Expected Result:** You understand scheduling options and can create recurring automation tasks.

---

## Advanced Concepts (Optional)

### Error Handling

Add error handling to your workflows:

Use "Catch" nodes to handle errors gracefully

Add fallback paths when operations fail

Log errors for debugging

### Loops and Batches

Process multiple items:

Use "Loop" nodes to iterate through arrays

Batch process large datasets

Handle pagination from APIs

### Custom Code

For complex logic:

Use "Function" nodes for JavaScript

Write reusable code snippets

Access the full n8n API in code

### Workflows as APIs

Turn workflows into endpoints:

Expose workflows via webhooks

Accept POST requests with parameters

Return formatted responses

---

## Troubleshooting Guide

### My workflow won't execute:

Check that you have a trigger node

Verify credentials are properly set up

Look at the execution history for error messages

### Data isn't passing between nodes:

Use Debug nodes to inspect data at each step

Check node output mapping (look for the node settings)

Ensure you're referencing the correct property names

### API requests are failing:

Test the API URL in your browser first

Check authentication credentials

Verify the request method (GET vs POST)

Look at the response body in the Debug output

### Scheduled workflows aren't running:

Confirm the workflow is activated (toggle in top-right)

Check your n8n instance is running (for self-hosted)

Review the execution history to see attempted runs

---

## Resources

https://docs.n8n.io/ - n8n Official Documentation

https://community.n8n.io/ - n8n Community

https://jsonplaceholder.typicode.com/ - JSONPlaceholder (Test API)

https://www.youtube.com/c/n8n - n8n YouTube Channel
