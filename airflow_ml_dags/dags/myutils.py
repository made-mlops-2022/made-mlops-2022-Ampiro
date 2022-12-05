import os


def wait_for_file(file_path: str):
    return os.path.exists(file_path)
