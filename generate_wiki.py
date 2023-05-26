# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-05-26 09:00:55
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-05-26 10:17:26

import pathlib as plib


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


def main():
    _wiki = plib.Path('./generated_wiki')
    if _wiki.exists():
        _md = markdown()
        fre_md = _wiki / 'frequency.md'
        with fre_md.open(mode='w', encoding='utf-8') as fre:
            fre.write(_md.plan('hello word~', 'x'))


if __name__ == "__main__":
    main()
