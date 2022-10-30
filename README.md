<h2 align="center">mylearn: my Machine Learning framework</h2>

<p align="center">
<a href="https://circleci.com/gh/MichaelKarpe/mylearn"><img alt="Build Status" src="https://circleci.com/gh/MichaelKarpe/mylearn.svg?style=shield"></a>
<a href="https://github.com/psf/black/blob/master/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

___

[mylearn](https://github.com/MichaelKarpe/mylearn) is a Machine Learning framework based on
[Airflow](https://github.com/apache/airflow) and [MLflow](https://github.com/mlflow/mlflow) for designing machine
learning systems in a production perspective.

**Work in progress... Stay tuned!**

# Index

1. [Prerequisites](#prerequisites)
2. [Installation & Setup](#installation-setup)
3. [Usage](#usage)

# Prerequisites

## pyenv

To be completed with how to install and setup pyenv

## poetry

To be completed with how to install and setup poetry

# Installation & Setup

mylearn leverages [poetry](https://github.com/python-poetry/poetry) and [poethepoet](https://github.com/nat-n/poethepoet)
to make its installation and setup surprisingly simple.

## Installation

It is recommended to install requirements within a virtualenv located at the project root level, although not required.
```commandline
poetry config virtualenvs.in-project true
```

Installation is run with
```commandline
poetry install
```

## Airflow Setup

Airflow setup is initialized via a `poe` command
```commandline
poe airflow-init
```

Airflow Scheduler & Webserver can be run with
```commandline
poe airflow-scheduler
poe airflow-webserver
```

Airflow UI can be opened at [localhost](0.0.0.0:8080) (port 8080), and you can login with username and password `admin`.

If you want to clean your Airflow setup before rerunning `poe airflow-init`, you need to kill Airflow Scheduler &
Webserver and run
```commandline
poe airflow-clean
```

## MLflow Setup

MLflow UI can be opened at [localhost](0.0.0.0:5000) (port 5000) after execution of the following command:
```commandline
poe mlflow-ui
```

# Usage

## MLflow Pipelines Regression Template

The *mlflow-template* pipeline, based on the
[MLflow Pipelines Regression Template](https://github.com/mlflow/mlp-regression-template), can be run independently with
```commandline
poe mlflow-run
```

or via an Airflow Directed Acyclic Graph (DAG) by triggering the *mlflow-template* DAG via Airflow UI or with
```commandline
TO BE COMPLETED
```

## Other examples

**Work in progress... Stay tuned!**
