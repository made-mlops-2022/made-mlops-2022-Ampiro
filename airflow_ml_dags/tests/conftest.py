import pytest
from airflow.models import DagBag, DAG


@pytest.fixture()
def dagbag():
    return DagBag()


def assert_dag_dict_equal(source: dict, dag: DAG):
    assert dag.task_dict.keys() == source.keys()
    for task_id, downstream_list in source.items():
        assert dag.has_task(task_id)
        task = dag.get_task(task_id)
        assert task.downstream_task_ids == set(downstream_list)
