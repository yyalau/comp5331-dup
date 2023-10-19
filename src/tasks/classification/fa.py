from __future__ import annotations

from collections.abc import Callable, Iterable

import torch
from torch.optim import Optimizer
from torch.optim.lr_scheduler import LRScheduler

from ...models.classification.fa import FA_X, FAModel

from .base import ClassificationTask

__all__ = ['FATask', 'FA_X']


class FATask(ClassificationTask[FA_X]):
    def __init__(
        self,
        classifier: FAModel,
        *,
        optimizer: Callable[[Iterable[torch.nn.Parameter]], Optimizer],
        scheduler: Callable[[Optimizer], LRScheduler],
    ) -> None:
        super().__init__(
            classifier=classifier,
            optimizer=optimizer,
            scheduler=scheduler,
        )