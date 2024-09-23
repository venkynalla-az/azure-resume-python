This is a simple Azure Function (HTTP Trigger), which communicates with Azure Cosmos DB. When the Function URL is invoked, the count item in Azure Cosmos DB Container is incremented by 1 and the result is returned. 

Pre-requisites:
1. Azure Function App is up and running. Azure Insights and Logs are optional.
2. GitHub has a repo set up.
3. I used VS Code as code editor, which has plugins to talk to Azure Portal and GitHub.
4. Azure Function App and GitHub are tied thru Azure Function App 'Deployment Center'.
5. Ensure GitHub Workflow read and write permissions are enabled. By default, only read permission is enabled.
6. Add/Commit/Push local git code to GitHub Repo.
7. Enable GitHub actions and review the .YML file. It should contain Azure credentials, which are stored in GitHub repo>Settings>Secrets and variables>Actions>Repository secrets.
8. When code is pushed to the repo, the GitHub actions is triggered. It builds and deploys code to the Azure Funtion. 
