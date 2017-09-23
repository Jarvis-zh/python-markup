#!/usr/bin/env python3
#coding:utf-8
#author: jarvis_zh@163.com

"""
文本块生成器。
"""

def lines(file):
    """
    生成器，在文本最后一行加一空行
    """
    for line in file:
        yield line
    yield '\n'


def blocks(file):
    """
    生成器，生成单独的文本块
    """
    block = []
    for line in lines(file):
        if line.strip(): #非空行
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []

