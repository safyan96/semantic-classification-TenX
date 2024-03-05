from locust import HttpUser, task, between
import json


class MyUser(HttpUser):
    wait_time = between(1, 5)  # Wait time between requests

    @task
    def query_endpoint(self):
        payload = {
            "sentence": "feeling like a million bucks",
            "labels": ["happy", "sad", "rich"],
        }
        headers = {"Content-Type": "application/json"}

        # Send POST request to the endpoint
        response = self.client.post(
            "/query/details", data=json.dumps(payload), headers=headers
        )

        # Print response status code and content
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")
