<h2 align="center">mylearn: my Machine Learning framework</h2>

<p align="center">
<a href="https://pypi.org/project/mylearn"><img src="https://img.shields.io/pypi/v/mylearn.svg"></a>
<a href="https://pypi.org/project/mylearn"><img src="https://img.shields.io/pypi/pyversions/mylearn.svg"></a>
<a href="https://github.com/MichaelKarpe/mylearn/blob/main/LICENSE"><img src="https://img.shields.io/pypi/l/mylearn.svg"></a>
<a href="https://github.com/MichaelKarpe/mylearn/actions"><img src="https://github.com/MichaelKarpe/mylearn/workflows/ci/badge.svg"></a>
<a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

___

[mylearn](https://github.com/MichaelKarpe/mylearn) is a Machine Learning framework based on
[Airflow](https://github.com/apache/airflow) and [MLflow](https://github.com/mlflow/mlflow) for designing machine
learning systems in a production perspective.

**Work in progress... Stay tuned!**

# Index

1. [Recommended prerequisites](#prerequisites)
2. [Installation & Setup](#installation-setup)
3. [Usage](#usage)

# Recommended prerequisites

## Git

```commandline
sudo apt-get install git
```

## pyenv

Install [binary dependencies and build tools](https://github.com/pyenv/pyenv/wiki#suggested-build-environment):
```commandline
sudo apt update
sudo apt install build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev curl libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

Install pyenv:
```commandline
curl https://pyenv.run | bash
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc
```

Install a Python version and set it as default:
```commandline
pyenv install 3.11.2
pyenv global 3.11.2
```

## poetry

```commandline
curl -sSL https://install.python-poetry.org | python3 -
echo 'export PATH="~/.local/bin:$PATH"' >> ~/.bashrc
```

# Installation & Setup

mylearn leverages [poetry](https://github.com/python-poetry/poetry) and [poethepoet](https://github.com/nat-n/poethepoet)
to make its installation and setup surprisingly simple.

## Installation

It is recommended to install requirements within a `virtualenv` located at the project root level, although not required.
```commandline
poetry config virtualenvs.in-project true
```

Installation is run with:
```commandline
poetry install
```

Should you install from the `requirements.txt` file instead of the `poetry.lock` file:
```commandline
pyenv shell 3.11.2
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
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
