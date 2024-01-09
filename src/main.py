#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Interface.LinkBudget import LinkBudget
from Impl.LinkBudgetImpl import LinkBudgetImpl


def main():
    print('##### PRESUPUESTO DEL ENLACE #####')

    # Create a LinkBudget object
    linkBudget: LinkBudget = LinkBudgetImpl('configuration.yaml')

    # Calc Fade Margin
    total_loss: float = linkBudget.get_total_loss()
    print(f"La perdida total de potencia es: {total_loss:4.2f} dB")

    # Calc Rss
    rss: float = linkBudget.get_Rss()

    print(f"La potencia de recepción es: {rss:4.2f} dBm")


if (__name__ == '__main__'):
    main()