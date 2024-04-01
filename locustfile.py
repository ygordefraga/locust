from locust import HttpUser, task, between
import random

class QuickstartUser(HttpUser):
    wait_time = between(0, 1)

    def on_start(self):
        self.client.cookies.clear()

    @task
    def hello(self):
        self.client.get("/hello")

    @task
    def delayed(self):
        self.client.get("/delayed")

    @task
    def throw_exception(self):
        self.client.post("/throw-exception")

    @task
    def get_users(self):
        random_number = random.randint(0, 6)
        self.client.get(f"/users/{random_number}", name="/get-users")