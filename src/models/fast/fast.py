from __future__ import annotations

from typing import Generic, TypeVar

from torch import Tensor
import torch.nn as nn

from modelops.dependencies import ClassificationModel, FAST_X, Classification_Y

__all__ = ['FAST']

NST = TypeVar('NST', bound=nn.Module)

Classification_Output = TypeVar('Classification_Output', bound=Classification_Y)

class FAST(nn.Module, Generic[NST, Classification_Output]):
    def __init__(self,
                style_transfer: NST,
                classifer: ClassificationModel[FAST_X],
                device: str = 'cpu', # "cpu" for cpu, "cuda" for gpu
                gamma: float = 2.0, # Controls importance of StyleLoss vs ContentLoss, Loss = gamma*StyleLoss + ContentLoss
                training: bool =True, # Wether or not network is training
                scr_temperature: float = 0.1,
                ) -> None:
        super(FAST).__init__()


        self.style_transfer = style_transfer(gamma, training, scr_temperature).to(device)
        self.classifier = classifer


    def forward(self, input: FAST_X) -> Classification_Output:
        content = input.get('content')
        styles = input.get('styles')

        transferred_contents: Tensor = self.style_transfer(content, styles)

        classifier_input: FAST_X = {'content': transferred_contents, 'styles': styles}
        predictions: Classification_Output = self.classifier(classifier_input)

        return predictions

