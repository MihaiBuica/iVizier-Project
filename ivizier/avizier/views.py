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

def about(request):
	return render(request, 'avizier/about.html')#HttpResponse('<h1>Afis about</h1>')