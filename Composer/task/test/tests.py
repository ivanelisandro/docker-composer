import docker
from hstest import StageTest, dynamic_test, CheckResult

test_network = "task-manager-network"
test_volume = "task-manager-data"
test_containers = ["task-manager-db", "task-manager-app"]
test_images = ["task-manager-app"]


def is_docker_running():
    """Check if the Docker daemon is running."""
    try:
        client = docker.from_env()
        client.ping()
        return True
    except docker.errors.DockerException:
        return False


class DockerTest(StageTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.output = None
        if is_docker_running():
            self.client = docker.from_env()
        else:
            self.client = None

    @dynamic_test()
    def test1(self):
        """Tests that containers has been deleted"""
        if not self.client:
            return CheckResult.wrong("Docker is not running. Please start the Docker daemon and try again.")
        container_names = "*".join(container.name for container in self.client.containers.list(all=True))
        for container in test_containers:
            if container in container_names:
                return CheckResult.wrong(f"You should delete the container `{container}`!")

        return CheckResult.correct()

    @dynamic_test()
    def test2(self):
        """Tests that images has been deleted"""
        image_names = "*".join(str(image) for image in self.client.images.list(all=True))
        for image in test_images:
            if image in image_names:
                return CheckResult.wrong(f"You should delete the image `{image}`!")

        return CheckResult.correct()

    @dynamic_test()
    def test3(self):
        """Tests that network does not exists in the system"""
        network_names = "*".join(network.name for network in self.client.networks.list())
        if test_network in network_names:
            return CheckResult.wrong(f"'{test_network}' should not be found in the system networks!")

        return CheckResult.correct()

    @dynamic_test()
    def test4(self):
        """Tests that volume does not exists in the system"""
        volume_names = "*".join(volume.name for volume in self.client.volumes.list())
        if test_volume in volume_names:
            return CheckResult.wrong(f"'{test_volume}' should not be found in the system volumes!")

        return CheckResult.correct()


if __name__ == '__main__':
    DockerTest().run_tests()
