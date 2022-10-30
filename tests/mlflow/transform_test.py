from __future__ import annotations

from mlflow.steps.transform import transformer_fn


def test_tranform_fn_returns_object_with_correct_spec():
    transformer = transformer_fn()
    assert callable(getattr(transformer, "fit", None))
    assert callable(getattr(transformer, "transform", None))
