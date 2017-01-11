#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
import re
import os
from html.parser import HTMLParser

class RemConverterCommand(sublime_plugin.TextCommand):
    def __init__(self,*args,**kw):
        super(RemConverterCommand, self).__init__(*args, **kw)
        self.remUnit = sublime.load_settings('RemConverter.sublime-settings').get('remUnit', 20)

    def run(self, edit,**kw):
        fileExtension = os.path.splitext(self.view.file_name())[1][1:].lower()
        toRem = kw.get('toRem',True)
        region = sublime.Region(0,self.view.size())
        textOfView = self.view.substr(region)
        if re.match(r'^html?$', fileExtension):
            httpParser = MyHTMLParser()
            httpParser.feed(textOfView)
            items = httpParser.getItems()
            for str in items:
                _transformResult = self.transform(str,toRem)
                region = self.view.find(self.patternToString(str),0)
                self.view.replace(edit, region, _transformResult)
        elif re.match(r'^(css|less|s[ca]ss)$', fileExtension):
            _transformResult = self.transform(textOfView,toRem)
            self.view.replace(edit, region, _transformResult)

    def transform(self,str='',toRem=True):
        def repl(m):
            gd = m.groupdict()
            if toRem:
                # px -> rem
                if gd.get('unit', None) == 'px':
                    ret = '%3.4f' % (float(gd.get('qty')) / float(self.remUnit))
                    while ret[-1] == '0':
                        ret = ret[:-1]
                    if ret.endswith('.'):
                        ret = ret[:-1]
                    return ret + 'rem'
                else:
                    return gd.get('qty')+gd.get('unit', None)
            else:
                # rem -> px
                if gd.get('unit', None) == 'rem':
                    ret_val = float(gd.get('qty')) * float(self.remUnit)
                    ret = '%3.1f' % ret_val
                    if ret.endswith('.0'):
                        ret = ('%3.0f' % ret_val) + 'px'
                    else:
                        ret = ret + 'px'
                    return ret.strip()
                else:
                    return gd.get('qty')+gd.get('unit', None)

        return re.sub(r'((?P<qty>[0-9\.]+)(?P<unit>px|rem))',repl,str)

    def patternToString(self,pattern):
        _p = re.compile('\*|\.|\?|\+|\$|\^|\[|\]|\(|\)|\{|\}|\||\\|\/')
        return _p.sub(lambda m: '\\'+m.group(0), pattern)


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.items = [] #保存提取结果
        self.data_start = False
    def handle_starttag(self, tag, attrs):
        if tag == 'style':
            self.data_start = True
    def handle_data(self, data):
        if self.data_start:
            self.items.append(data)
            self.data_start = False
    def getItems(self):
        return self.items
