#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import json
import MultipartPostHandler
import settings
from settings import *


class PhotoZoOperator:

    def __init__(self):
        auth_handler = urllib2.HTTPBasicAuthHandler()
        auth_handler.add_password(BASIC_AUTH['realm'], API_HOST, BASIC_AUTH['username'], BASIC_AUTH['password'])
        opener = urllib2.build_opener(auth_handler, MultipartPostHandler.MultipartPostHandler)
        urllib2.install_opener(opener)

    # user_id 取得
    def get_user_id(self):
        url = API_HOST + '/rest/nop.json'
        f = urllib2.urlopen(url)
        res_dict = json.loads(f.read())
        user_id = res_dict['info']['user_id']
        return user_id

    # アルバム名とIDの一覧を取得
    def get_album_list(self):
        url = API_HOST + '/rest/photo_album.json'
        f = urllib2.urlopen(url)
        res_dict = json.loads(f.read())
        res = []
        for album in res_dict['info']['album']:
            res.append({'name': album['name'], 'album_id': album['album_id']})
        return res

    # アルバム名からアルバムIDを取得
    def get_album_id(self, album_name):
        album_list = self.get_album_list()
        for album in album_list:
            if album['name'] == album_name:
                return album['album_id']
        return None

    def get_album_photo_list(slef, album_id):
        url = API_HOST + '/rest/photo_album_photo.json'
        params = {'album_id': album_id}
        f = urllib2.urlopen(url, params)
        res_dict = json.loads(f.read())
        res = []
        for photo in res_dict['info']['photo']:
            res.append({'photo_id': photo['photo_id'], 'original_image_url':  photo['original_image_url'], 'image_url':  photo['image_url']})
        return res

    # フォトをアルバムに追加
    def add_photo(self, album_id, file_path, photo_title=''):
        url = API_HOST + '/rest/photo_add.json'
        img_f = open(file_path, 'rb')
        params = {'album_id': album_id, 'photo': img_f, 'photo_title': photo_title}
        f = urllib2.urlopen(url, params)
        res_dict = json.loads(f.read())
        img_f.close()
        img_url = self.get_photo_url(res_dict['photo_id'], 'original')
        return img_url

    # フォトIDからフォトのurlを取得
    def get_photo_url(self, photo_id, type='defult'):
        url = API_HOST + '/rest/photo_info.json'
        params = {'photo_id': photo_id}
        f = urllib2.urlopen(url, params)
        res_dict = json.loads(f.read())
        if type == 'default':
            return res_dict['info']['photo']['image_url']
        elif type == 'thumbnail':
            return res_dict['info']['photo']['thumbnail_image_url']
        elif type == 'original':
            return res_dict['info']['photo']['original_image_url']
        else:
            return None
