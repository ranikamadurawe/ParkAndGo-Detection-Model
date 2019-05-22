from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):

    @task
    def put_tests(self):
        self.client.post("/?url=['a.mp4','a.mp4','a.mp4','a.mp4']", {
            "name": "load testing"
        })


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
