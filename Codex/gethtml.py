# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-05-15 20:42:54
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-05-16 20:25:49

import urllib.request
import ssl,zlib

class get_html:
    ''' get download url '''
    text: str = ''
    headers_cjw = {
        'GET': '/zoushitu/cjwssq/hqfgzglclrw.html HTTP/1.1',
        'Cookie':
        'wzws_sessionid=gWYwOTdkMIJhM2UyZmWgZEXfGYAxNzEuNDMuNzAuMTM3; PHPSESSID=6345a3df94ae7a3e9cfc807c26ce6a23; Hm_lvt_17c098d74ec9e8dd63ced946aa8ac16d=1682231834,1682235355',
        'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Host': 'm.cjcp.cn',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }
    headers_360 = {
        'GET':'/kaijiang/ssq HTTP/1.1',
        'Cookie': 'test_cookie_enable=null; util-api-mid=d9d8ba7d85d05476dd5a8dc450c8444d; monitor_count=2; __guid=234711244.2937109531416237000.1684170869492.859; lguid=9B21C686-3711-C021-C60A-4819498AE883',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Host': 'chart.cp.360.cn',
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
    }
    headers_zhcw ={
        'GET': '/c/2019-08-19/580134.shtml HTTP/1.1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-cn',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate, br',
        'Host': 'www.zhcw.com'
    }

    def __init__(self, url: str) -> None:
        if url == None:
            raise ValueError("url cannot be None")
        try:
            context = ssl._create_unverified_context()
            req = urllib.request.Request(
                url,
                headers=self.headers_360,
            )
            response = urllib.request.urlopen(url=req, context=context)
            if response.status == 200:
                html_content = zlib.decompress(response.read(), wbits=zlib.MAX_WBITS | 16)
                self.text = html_content.decode('gb2312')
            else:
                self.text = f"Error: {response.status}"
        except Exception as e:
            raise ValueError(
                f"Failed to retrieve content from URL ({url}), error: {str(e)}"
            )

    @property
    def neirong(self) -> str:
        ''' get text '''
        return self.text


