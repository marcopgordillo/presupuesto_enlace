# -*- coding: utf-8 -*-

import yaml, math
from Interface.LinkBudget import LinkBudget

class LinkBudgetImpl(LinkBudget):
    
    def __init__(self, file_input: str) -> None:
        super().__init__()
        self.configuration = self.__read_parameters(file_input)

    def __read_parameters(self, file_input: str) -> tuple:
        with open(file_input) as file:
            try:
                configuration = yaml.safe_load(file)
                return configuration['config']
            except yaml.YAMLError as exc:
                print(exc)

    def calc_FM(self):
        return 30 * math.log(self.configuration['distancia'], 10) + 10 * math.log(6 * self.configuration['FM']['A'] * self.configuration['FM']['B'] * self.configuration['frecuencia'], 10) - 10 * math.log(1 -  self.configuration['FM']['R'] ,10) - 70

    def __loss_cables(self):
        return (self.configuration['ht'] + self.configuration['hr']) * self.configuration['perdida_cable']
    
    def __loss_conectores(self):
        return self.configuration['perdida_conector'] * 4

    def get_Loss_EL(self):
        return 32.45 + 20 * math.log(self.configuration['distancia'], 10) + 20 * math.log(self.configuration['frecuencia'], 10)
    
    def get_total_loss(self):
        return self.get_Loss_EL() + self.calc_FM() + self.__loss_cables() + self.__loss_conectores()

    def get_Rss(self):
        return self.configuration['Ptx'] + self.configuration['Gtx'] + self.configuration['Grx'] - self.get_total_loss()
