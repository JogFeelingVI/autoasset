# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-05-26 09:00:55
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-05-26 15:45:44

import pathlib as plib
from types import MethodType


class markdown:
    '''markdown'''

    @staticmethod
    def title(T: str, L: int = 1) -> str:
        '''
        # TITLE
        '''
        flg = '#' * L
        t_str = f'{T}'
        return f'{flg} {t_str}'

    @staticmethod
    def link(text: str, link: str) -> str:
        ''' link '''
        format_link = '[{t}}]({l}})'
        return format_link.format(a=text, l=link)

    @staticmethod
    def actualUrl(url: str) -> str:
        ''' actual <URL> '''
        formart_actual = '<{url}>'
        return formart_actual.format(url=url)

    @staticmethod
    def image(text: str, link: str) -> str:
        ''' image '''
        format_image = '![{t}}]({l})'
        return format_image.format(a=text, l=link)

    @staticmethod
    def bold(text: str) -> str:
        ''' Bold '''
        bold_format = '**{t}**'
        return bold_format.format(t=text)

    @staticmethod
    def ltalic(text: str) -> str:
        ''' ltalic '''
        ltalic_format = '_{t}_'
        return ltalic_format.format(t=text)

    @staticmethod
    def code(text: str) -> str:
        ''' code '''
        code_format = '`{t}`'
        return code_format.format(t=text)

    @staticmethod
    def unordered_list(text: str) -> str:
        ''' code '''
        unordered_list = '* {t}'
        return unordered_list.format(t=text)

    @staticmethod
    def ordered_list(text: str, sn: int = 1) -> str:
        ''' code '''
        ordered_list = '{s}. {t}'
        return ordered_list.format(t=text, s=sn)

    @staticmethod
    def blockquote(text: str) -> str:
        ''' blockquote > TEXT'''
        blockquote = '> {t}'
        return blockquote.format(t=text)

    @staticmethod
    def Dividing_line() -> str:
        ''' *** '''
        Dividing_line = '***'
        return Dividing_line

    @staticmethod
    def plan(text: str, stat: str) -> str:
        '''
        plan - [x] plan a
        stat un / x
        '''
        plan_format = '- [{s}] {t}'
        st = [' ', 'x'][stat in 'xdc1']
        return plan_format.format(t=text, s=st)


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
        self.__md = markdown()
        self.__run_work.update({
            'frequency': self.__frequency,
            '2': 'glns',
        })

    def __frequency(self):
        if self.__wiki is not None and self.__wiki_init:
            fre_md = self.__wiki / 'frequency.md'
            with fre_md.open(mode='w', encoding='utf-8') as fre:
                fre.write(self.__md.plan('hello word~', 'x'))

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
