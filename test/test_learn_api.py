import requests

ENDPOINT = "https://todo.pixegami.io"

def test_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_create_task():
    payload ={
        "content": "Testing API",
        "user_id": "Muhammad Fajar Al Fath",
        "is_done": False
    }
    response_create_task = requests.put(ENDPOINT + "/create-task",json=payload)
    assert response_create_task.status_code == 200
    data = response_create_task.json()
    print(data)

    # Get data after the creation
    task_id = data["task"]["task_id"]
    response_get_task = requests.get(ENDPOINT + f"/get-task/{task_id}")

    assert response_get_task.status_code == 200
    get_task_data = response_get_task.json()
    # Verify the data is the same
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]

# test Update task
def test_can_update_task():
    # get and validate the change
    pass

def create_task(payload):
    return  requests.put(ENDPOINT)

