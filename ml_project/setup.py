from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='Simple ML project for VK MLOps course.',
    author='Ampiro',
    entry_points={
        "console_scripts": [
            "train=src.models.console_functions.pipeline:commands_runner",
            "predict=src.models.console_functions.pipeline:commands_runner",
            "evaluate=src.models.console_functions.pipeline:commands_runner",
            "pipeline=src.models.console_functions.pipeline:pipeline_command"
        ]
    },
    scripts=[
        "tests/run_tests"
    ],
    license='',
)
