from __future__ import annotations

from sklearn.utils.estimator_checks import check_estimator

from mlflow.steps.train import estimator_fn


def test_train_fn_returns_object_with_correct_spec():
    regressor = estimator_fn()
    assert callable(getattr(regressor, "fit", None))
    assert callable(getattr(regressor, "predict", None))


def test_train_fn_passes_check_estimator():
    regressor = estimator_fn()
    check_estimator(regressor)
