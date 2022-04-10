from django.shortcuts import render, redirect
#pytub package for download youtube video
from pytube import YouTube
import os
from django.http import FileResponse
import pafy
import pytube
def ytb_down(request):      
    if request.method == 'POST':
        url = request.POST.get('ylink')
        video = pafy.new(url)
        embedlink = url.replace("watch?v=", "embed/")
        context = {
        'yobj': video,
        'embedlink': embedlink,
        }
        return render(request, 'ytb_main.html', context)
            
 
    return render(request, 'ytb_main.html')

def home(request):
    if request.method == 'POST':
        url = request.POST.get('ylink')
        video = pafy.new(url)
        embedlink = url.replace("watch?v=", "embed/")
        context = {
            'yobj': video,
            'embedlink': embedlink,
        }
        return render(request, 'ytb_main.html', context)
    return render(request, 'home.html')

def music(request):
    if request.method == 'POST':
        url = request.POST.get('ylink')
        video = pafy.new(url)
        embedlink = url.replace("watch?v=", "embed/")
        context = {
            'yobj': video,
            'embedlink': embedlink,
        }
        return render(request, 'music_download.html', context)
    elif ValueError:
        return render(request, 'music_download.html', {'error':'Please input a valid video url or link'} )
    return render(request, 'music_download.html')

def thumbnail(request):
    if request.method == 'POST':
        url = request.POST.get('ylink')
        video = pafy.new(url)
        embedlink = url.replace("watch?v=", "embed/")
        context = {
            'yobj': video,
            'embedlink': embedlink,
        }
        return render(request, 'ytb_main.html', context)
    return render(request, 'ytb_main.html')