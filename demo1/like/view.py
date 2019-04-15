from django.http import HttpResponse

def index(request):
    return HttpResponse('老铁来了啊，双击666')
def cat(request):
    return HttpResponse('我会抓老鼠')
def dog(request):
    return HttpResponse('爱还没来，天地间风云突然变，天狗食日，必有大难，须有人杰出世方能拯救世界')
def mouse(request):
    return  HttpResponse('鼠，十二生肖之一。鼠的第一个象征意义是灵性，又包括它的机灵和性能通灵两个方面；鼠的第二个象征意义是生命力强。鼠之所以排在生肖榜上的第一位主要有三个原因：一是民间传说故事中的生肖排列。二是中国古代学者从古代昼夜十二时辰的角度解说地支和肖兽的配属关系。三是按中国人信阴阳的观念，将十二种动物分为阴阳两类，动物的阴与阳是按动物足趾的奇偶参差排定的。动物的前后左右足趾数一般是相同的，而鼠独是前足四，后足五，奇偶同体 ，物以稀为贵，当然排在第一。')