from __future__ import annotations

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

# The DAG object; we'll need this to instantiate a DAG
# Operators; we need this to operate!

with DAG(
    "mlflow",
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 0,
        "retry_delay": timedelta(seconds=5),
        # 'queue': 'bash_queue',
        # 'pool': 'backfill',
        # 'priority_weight': 10,
        # 'end_date': datetime(2016, 1, 1),
        # 'wait_for_downstream': False,
        # 'sla': timedelta(hours=2),
        # 'execution_timeout': timedelta(seconds=300),
        # 'on_failure_callback': some_function,
        # 'on_success_callback': some_other_function,
        # 'on_retry_callback': another_function,
        # 'sla_miss_callback': yet_another_function,
        # 'trigger_rule': 'all_success'
    },
    description="MLflow DAG",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2022, 8, 28),
    catchup=False,
    tags=["mlflow"],
) as dag:

    # t1, t2 and t3 are examples of tasks created by instantiating operators
    t1 = BashOperator(
        task_id="ingest",
        bash_command="""
        cd ${AIRFLOW_HOME};
        cd ..;
        mlflow pipelines run --step ingest;
        """,
    )

    t2 = BashOperator(
        task_id="split",
        bash_command="""
        cd ${AIRFLOW_HOME};
        cd ..;
        mlflow pipelines run --step split;
        """,
    )

    t3 = BashOperator(
        task_id="transform",
        bash_command="""
        cd ${AIRFLOW_HOME};
        cd ..;
        mlflow pipelines run --step transform;
        """,
    )

    t4 = BashOperator(
        task_id="train",
        bash_command="""
        cd ${AIRFLOW_HOME};
        cd ..;
        mlflow pipelines run --step train;
        """,
    )

    t5 = BashOperator(
        task_id="evaluate",
        bash_command="""
        cd ${AIRFLOW_HOME};
        cd ..;
        mlflow pipelines run --step evaluate;
        """,
    )

    t6 = BashOperator(
        task_id="register",
        bash_command="""
        cd ${AIRFLOW_HOME};
        cd ..;
        mlflow pipelines run --step register;
        """,
    )

    t1 >> t2
    t2 >> t3
    t3 >> t4
    t4 >> t5
    t5 >> t6
