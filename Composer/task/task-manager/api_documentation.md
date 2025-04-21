### Documentation
- If jq is not installed on your system, you can omit that part

#### Create a task

```bash
curl -X POST -H "Content-Type: application/json" -d '{"title":"Task title","description":"Task description"}' http://localhost:8000/tasks
```
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/tasks" -Method Post -ContentType "application/json" -Body '{"title":"Task title","description":"Task description"}' 
```

#### Get task by ID

```bash
curl --silent http://localhost:8000/tasks/{task_id} | jq
```
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/tasks/$task_id" -Method Get | ConvertTo-Json
```

#### Get task by Title

```bash
curl --silent http://localhost:8000/tasks/title/{task_title} | jq
```
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/tasks/$task_title" -Method Get | ConvertTo-Json
```

#### Get all tasks

```bash
curl --silent http://localhost:8000/tasks | jq
```
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/tasks" -Method Get | ConvertTo-Json
```

#### Delete task by ID

```bash
curl --silent -X DELETE  http://localhost:8000/tasks/{task_id} | jq
```
```powershell
$task_id = "your_task_id_here"  # Replace with the actual task ID
Invoke-RestMethod -Uri "http://localhost:8000/tasks/$task_id" -Method Delete | ConvertTo-Json
```
