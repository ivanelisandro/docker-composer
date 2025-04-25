from pathlib import Path

import yaml
from hstest import StageTest, dynamic_test, CheckResult
from yaml.parser import ParserError
from yaml.scanner import ScannerError

docker_file = "docker-compose.yaml"
stage = Path(__file__).parent.parent


class DockerTest(StageTest):

    @staticmethod
    def load_yaml(file_path):
        """Loads a yaml file from the given path"""
        try:
            with open(file_path, 'r') as file:
                return yaml.safe_load(file)
        except ScannerError:
            return "Could not open"
        except ParserError:
            return "Could not parse"
        except FileNotFoundError:
            return "Could not find"

    def compare_dicts(self, dict1, dict2):
        """Compares two dictionaries and returns on the first mismatch"""
        for key in dict1:
            if key not in dict2:
                return f"Key `{key}` is missing."
            else:
                if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                    result = self.compare_dicts(dict1[key], dict2[key])
                    if result:
                        return result
                elif dict1[key] != dict2[key]:
                    return f"Value for the key `{key}` is wrong. It should be `{dict1[key]}`"

    @dynamic_test()
    def test1(self):
        """Tests if two yaml files are equal"""
        file1 = f"{stage}/test/test-docker-compose.yaml"
        file2 = f"{stage}/task-manager/docker-compose.yaml"

        dict1 = self.load_yaml(file1)
        if not isinstance(dict1, dict):
            return CheckResult.wrong(f"{dict1} `{file1}`")
        dict2 = self.load_yaml(file2)
        if not isinstance(dict2, dict):
            return CheckResult.wrong(f"{dict2} `{file2}``")

        result = self.compare_dicts(dict1, dict2)
        if result:
            return CheckResult.wrong(result)

        return CheckResult.correct()


if __name__ == '__main__':
    DockerTest().run_tests()
