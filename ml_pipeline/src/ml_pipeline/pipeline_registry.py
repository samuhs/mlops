"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline

from ml_pipeline.pipelines import training as t

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    training = t.create_pipeline()
    
    return {"__default__": training,
            "training": training
    }
