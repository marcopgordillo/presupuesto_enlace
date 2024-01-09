# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class LinkBudget(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def calc_FM(self):
        pass

    @abstractmethod
    def get_Rss(self):
        pass

    @abstractmethod
    def get_Loss_EL(self):
        pass
    
    @abstractmethod
    def get_total_loss(self):
        pass