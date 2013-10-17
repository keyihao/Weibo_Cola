#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Copyright (c) 2013 Ke Yihao <sheepke@gmail.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Created on 2013-10-17

@author: Felixke
'''

import time

from cola.core.unit import Bundle

class WeiboUserBundle(Bundle):
    def __init__(self, uid):
        super(WeiboUserBundle, self).__init__(uid)
        self.uid = uid
        self.exists = True
        
        self.last_error_page = None
        self.last_error_page_times = 0
        
        self.weibo_user = None
        self.last_update = None
        self.newest_mids = []
        self.current_mblog = None
        
        self.fetched_weibo_num = 0
        self.fetched_follow_num = 0
        self.fetched_fans_num = 0
        self.fetched_weibo_comment_num = 0
        self.fetched_weibo_forward_num = 0
        self.fetched_weibo_like_num = 0
 
        self.fetched_last_comment_id = None
        self.fetched_last_forward_id = None
        self.fetched_last_like_id = None

        
    def urls(self):
        start = int(time.time() * (10**6))
        return [
            'http://weibo.com/%s/follow' % self.uid,
            'http://weibo.com/%s/info' % self.uid,
            'http://weibo.com/aj/mblog/mbloglist?uid=%s&_k=%s' % (self.uid, start),
            # remove because some user's link has been http://weibo.com/uid/follow?relate=fans
            # 'http://weibo.com/%s/fans' % self.uid
        ]
