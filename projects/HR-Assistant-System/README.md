- Overview:

- Prerequisite installation
  - Claude Desktop
  - Install uv: powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  - HRMS folder for api integration
  - In cli of ide: uv add mcp[cli]
	- Update the details at 2 places pyproject.toml and uv.lock file

- Technical Architecture
![img.png](resources/Technical-Architecture.png)

- HR-Management-System Project Structure
  - hrms: Include all the api for HR management systems to perform task
  - resources: It includes all the resources needed like image, file, document etc.
  - utils.py: This file is use to seeds all the services means initilize all the require classes.
  - server.py: The file will interact with HRMS system, Emailing System, Databases etc and get things done via Claude Desktop client.

- HR Assist application
HR Assist Client Home Page
![img.png](resources/HR-Assist-Client-Home-Page.png)

HR Assist Response
![img.png](resources/HR-Assist-Response.png)