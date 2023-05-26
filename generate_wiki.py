# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-05-26 09:00:55
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-05-26 23:00:15

import pathlib as plib
from types import MethodType
from Codex import md, datav


class wikigo:
    __wiki_init = False
    __wiki = None
    __run_work = {}

    def __init__(self) -> None:
        _wiki = plib.Path('./generated_wiki')
        if _wiki.exists() == False:
            _wiki.mkdir()
        self.__wiki = _wiki
        self.__wiki_init = True
        self.__md = md.markdown()
        self.__datav = datav.data_visualization(datav.LoadJson().toLix)
        self.__run_work.update({
            'frequency': self.__frequency,
            '2': 'glns',
        })

    def __frequency(self):
        if self.__wiki is not None and self.__wiki_init:
            fre_md = self.__wiki / 'frequency.md'
            with fre_md.open(mode='w', encoding='utf-8') as fre:
                for key in 'RB':
                    fre.write(self.__md.title(f'Frequency for {key}'))
                    matrix = self.__datav.frequency(key=key)
                    for line in matrix:
                        fre.write(self.__md.plan(line, 'x'))
                    fre.write(self.__md.Dividing_line())
                    fre.write(self.__md.time())

    def run_work(self):
        for k, lab in self.__run_work.items():
            print(f'work {k} runing... {type(lab)}')

            if isinstance(lab, MethodType):
                lab()
            elif isinstance(lab, str):
                print(f'Echo {lab}')
            else:
                print('unhandled type')


def main():
    _wiki = wikigo()
    _wiki.run_work()


if __name__ == "__main__":
    main()
