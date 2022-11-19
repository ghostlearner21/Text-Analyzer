# I had created this file - Devansh
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # Creating the home page
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def contactus(request):
    return render(request, 'contactus.html')

def Analyze(request):
    text = request.POST.get('user-text', '404: no text found')
    checkpnc = request.POST.get('removepunc', 'off')
    checknewline = request.POST.get('removenewline', 'off')
    checkupper = request.POST.get('uppercase', 'off')
    checkextraspace = request.POST.get('removeextraspaces', 'off')
    count = request.POST.get('charcount', 'off')
    purpose = ''
    analyzed = ''

    if text=="":
        text = '404: no text found'

    if checkpnc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        purpose += 'check punctuations || '
        for char in text:
            if char not in punctuations:
                analyzed += char
        text = analyzed

    if checknewline == 'on':
        purpose += 'remove new line || '
        analyzed = ''
        for char in text:
            if char != "\n" and char != "\r":
                analyzed += char
        text = analyzed

    if checkupper == 'on':
        purpose += 'uppercase || '
        text = text.upper()

    if checkextraspace == 'on':
        purpose += 'remove extra spaces || '
        analyzed = ''
        text = text.strip()
        for index, char in enumerate(text):
            if not (text[index] == ' ' and text[index + 1] == ' '):
                analyzed += char
        text = analyzed

    if count == 'on':
        purpose += 'count characters || '
        text += ' [ characters : ' + str(len(text)) + ']'

    if purpose == '':
        purpose = 'no purpose found'

    params = {'purpose': purpose, 'output_text': text}
    return render(request, 'analyzed.html', params)

