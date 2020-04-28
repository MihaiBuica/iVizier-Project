from django.shortcuts import render
from .models import Post

# posts = [
# 	{
# 		'author': 'Ruxi Stancioi',
# 		'title': 'Ruxi afis',
# 		'content': 'primul proiect',
# 		'date': '8 Aprilie'
# 	},
# 	{
# 		'author': 'Angi',
# 		'title': 'Angi gogosi',
# 		'content': 'reteta',
# 		'date': '10 Aprilie'
# 	}
# ]
# Create your views here.
def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'avizier/home.html', context)

def targulitc(request):
	return render(request, 'avizier/targulitc.html') # HttpResponse('<h1>Afis about</h1>')

def bestem(request):
	return render(request, 'avizier/bestem.html')

def hackitall(request):
	return render(request, 'avizier/hackitall.html')

def eli_np(request):
	return render(request, 'avizier/eli-np.html')

def _3dupb(request):
	return render(request, 'avizier/3dupb.html')

def acs(request):
	return render(request, 'avizier/acs.html')