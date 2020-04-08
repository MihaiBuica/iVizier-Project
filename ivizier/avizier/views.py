from django.shortcuts import render
#from django.http import HttpResponse

posts = [
	{
		'author': 'Ruxi Stancioi',
		'title': 'Ruxi afis',
		'content': 'primul proiect',
		'date': '8 Aprilie'
	},
	{
		'author': 'Angi',
		'title': 'Angi gogosi',
		'content': 'reteta',
		'date': '10 Aprilie'
	}
]
# Create your views here.
def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'avizier/home.html', context)

def about(request):
	return render(request, 'avizier/about.html')#HttpResponse('<h1>Afis about</h1>')