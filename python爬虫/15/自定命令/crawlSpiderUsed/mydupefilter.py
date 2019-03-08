from __future__ import print_function
import os
import logging

from scrapy.utils.job import job_dir
from scrapy.utils.request import request_fingerprint

from scrapy.dupefilters import BaseDupeFilter

class MyDupeFilter(BaseDupeFilter):
    """Request Fingerprint duplicates filter"""

    def __init__(self, path=None, debug=False):
        #fingerprints指纹集合，保存url的指纹信息
        self.fingerprints = set()

    def request_seen(self, request):
        print('自定义去重')
        #url去重实现的方法
        fp = self.request_fingerprint(request)
        if fp in self.fingerprints:
            return True
        self.fingerprints.add(fp)

    def request_fingerprint(self, request):
        #返回一个指纹信息（根据hashlib生成的）
        return request_fingerprint(request)
