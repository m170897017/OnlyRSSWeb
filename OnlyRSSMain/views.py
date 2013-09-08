#coding=utf-8
from django.shortcuts import render_to_response
from django.core import serializers
from django.http import HttpResponse
import feedparser
import json
from models import *


def index(request):
    """
    主页
    :param request:
    :return:
    """
    return render_to_response('index.html')


def get_all_feed_list(request):
    feeds = get_feed_list();

    return HttpResponse(feeds)


def get_feed_list():
    feed_list = Feed.objects.all()
    feeds_json = serializers.serialize("json", feed_list)

    return feeds_json


def get_feed_content(request):
    url = request.GET.get('url')
    id = request.GET.get('id')
    item_list = Item.objects.select_related().filter(feed_id=id)
    list = []

    for item in item_list:
        dicItem = {'title': item.title, 'content': item.content, 'url': item.url, 'feed_title': item.feed.title, 'feed_url': item.feed.url}
        list.append(dicItem)

    items_json = json.dumps(list)

    return HttpResponse(items_json)
