from airflow.models import DagBag


def test_generator_loaded(dagbag: DagBag):
    dag = dagbag.get_dag(dag_id="Data_generator")
    assert dagbag.import_errors == {}
    assert dag is not None
    assert len(dag.tasks) == 1


def test_trainer_loaded(dagbag: DagBag):
    dag = dagbag.get_dag(dag_id="Trainer")
    assert dagbag.import_errors == {}
    assert dag is not None
    assert len(dag.tasks) == 6


def test_predictor_loaded(dagbag: DagBag):
    dag = dagbag.get_dag(dag_id="Predictor")
    assert dagbag.import_errors == {}
    assert dag is not None
    assert len(dag.tasks) == 4
