from dataclasses import dataclass


@dataclass
class Project:
    def get_file_summary(self, file_path: str) -> str:
        pass

    def get_project_summary(self) -> str:
        pass
