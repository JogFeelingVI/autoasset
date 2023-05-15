# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-05-15 20:56:57
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-05-15 20:58:45
import os, sys
from pathlib import Path, PurePath
from typing import Union


class ospath:
    '''
    get os path /data/data/com.termux.com/file
    '''

    @staticmethod
    def path() -> str:
        '''
        huo qu li jing
        '''
        path, _ = os.path.split(os.path.realpath(sys.argv[0]))
        return path

    @staticmethod
    def file_path(file: str) -> str:
        '''
        huo qu wen jian lu jing
        '''
        path = ospath.path()
        fp = f'{PurePath(path, file)}'
        return fp if Path(fp).exists() else ''


