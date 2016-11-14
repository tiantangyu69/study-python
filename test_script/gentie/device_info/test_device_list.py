#!/usr/bin/env
# -*- coding: utf-8 -*-
from urllib import request, parse
import unittest
import json


class TestDeviceInfo(unittest.TestCase):
    def setUp(self):
        self.url_prefix = 'http://comment.api.163.com/api/v1'
        self.product_key = 'aac69c917e1787ad7bd86cd86afe6efc'
        self.urs_id = 'D60926C92053992FE4BFD9014C0F57A2DEB1FE71F71E4E31A1F77A074ACB7BFD3584DDCBD24B84BBFA9B2728E58EE8C4'
        self.urs_token = '46D3878FFC4F0AE7A6FED8D794A86CABCFB266DC92956043C90411927A4F62DC9351103A7A634E31792A1A197015800B80B867551138E9107D61262FC699E9F74D42705072D7CA2DB904AFB8A7EB9984'

    # 测试根据 User-Agent 查询设备列表
    def test_device_list(self):
        print('-------------------------------------------- test device list ---------------------------------------')
        req = request.Request(
            self.url_prefix + '/products/' + self.product_key + '/app/ios/devicelist')
        req.add_header('User-Agent', 'NewsApp/4.3.3 Android/5.0.1(honor/g620s-ul00)')

        with request.urlopen(req) as f:
            print('Status:', f.status, f.reason)
            for k, v in f.getheaders():
                print('%s: %s' % (k, v))
            data = f.read().decode('utf-8')
            print('Data:', data)

    # 测试 app 发贴是否带有设备名称
    def test_comment_app(self):
        print('--------------------------------------------- test comment app --------------------------------------')
        req = request.Request(
            self.url_prefix + '/products/' + self.product_key + '/threads/BBB1NPJD00014AED/app/comments')
        req.add_header('User-Agent', 'NewsApp/4.3.3 Android/5.0.1(SONY)')

        comment_data = parse.urlencode([
            ('urstoken', self.urs_token),
            ('ursid', self.urs_id),
            ('body', '测试sony设备号'),
            ('board', 'ent2_bbs')
        ])

        with request.urlopen(req, data=comment_data.encode('utf-8')) as f:
            print('Status:', f.status, f.reason)
            for k, v in f.getheaders():
                print('%s: %s' % (k, v))
            data = f.read().decode('utf-8')
            print('Add Comment Data:', data)

            dict = json.loads(data)
            post_id = dict.get('postid')
            doc_comment = post_id.split('_')
            doc_id = doc_comment[0]
            comment_id = doc_comment[1]

            print(
                '---------------------------------- query one comment for app ---------------------------------------')
            req = request.Request(
                self.url_prefix + '/products/' + self.product_key + '/app/threads/' + doc_id + '/comments/' + comment_id)

            with request.urlopen(req) as f:
                print('Status:', f.status, f.reason)
                for k, v in f.getheaders():
                    print('%s: %s' % (k, v))
                data = f.read().decode('utf-8')
                print('Data:', data)

                # # 查询 app 单贴接口
                # def test_query_comment_app(self):
                #     print('---------------------------------- query one comment for app ---------------------------------------')
                #     req = request.Request(
                #         self.url_prefix + '/products/' + self.product_key + '/app/threads/BBB1NPJD00014AED/comments/15883223')
                #
                #     with request.urlopen(req) as f:
                #         print('Status:', f.status, f.reason)
                #         for k, v in f.getheaders():
                #             print('%s: %s' % (k, v))
                #         data = f.read().decode('utf-8')
                #         print('Data:', data)


if __name__ == '__main__':
    unittest.main()
