# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.settings import SITE_NAME
from posts.models import Category, Post
from common.models import PageElement, SiteLink, RecommendedLink, SocialMediaLink


tag_line = PageElement.objects.get(name='Tag Line', is_visible=True)
footer_text = PageElement.objects.get(name='Footer Text', is_visible=True)


def index(request):

    post_list = Post.objects.all().order_by('-published')
    category_list = Category.objects.filter(display=True)
    site_link_list = SiteLink.objects.filter(is_visible=True)
    recommended_link_list = RecommendedLink.objects.filter(is_visible=True)
    social_media_link_list = SocialMediaLink.objects.filter(is_visible=True)

    return render(
        request,
        'common_index.html',
        {
            'category_list': category_list,
            'footer_text': footer_text,
            'page_title': SITE_NAME,
            'post_list': post_list,
            'recommended_link_list': recommended_link_list,
            'site_link_list': site_link_list,
            'social_media_link_list': social_media_link_list,
            'tag_line': tag_line,
        },
    )


def about(request):
    category_list = Category.objects.filter(display=True)
    site_link_list = SiteLink.objects.filter(is_visible=True)
    recommended_link_list = RecommendedLink.objects.filter(is_visible=True)
    social_media_link_list = SocialMediaLink.objects.filter(is_visible=True)

    return render(
        request,
        'common_about.html',
        {
            'category_list': category_list,
            'footer_text': footer_text,
            'page_title': 'About Harlin',
            'recommended_link_list': recommended_link_list,
            'site_link_list': site_link_list,
            'social_media_link_list': social_media_link_list,
            'tag_line': tag_line,
        }
    )
