from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

posts = [
	{
 		'title': 'TârgulIT&C',
 		'image': 'media/targulitc.jpg',
 		'content': 'Peste 45 de companii de renume din România și din afară își vor face simțită prezența în cadrul evenimentului din acest an, oferind pasionaților de domeniul IT&C stagii de practică, internshipuri, joburi de junior și nu numai!',
 		'url': '/targulitc',
 		'date': '8 Aprilie'
 	},
 	{
 		'title': 'BESTEM-20',
 		'image': 'media/bestem.jpg',
 		'content': '1 day of teamwork, 24 hours to find innovative solutions for challenging problems, 1440 minutes of fun, delicious food and ingenuity, only at BEST Engineering Marathon aka BESTEM, a 24 hour-long hackathon at its 10th edition.',
 		'url': '/bestem',
 		'date': '8 Aprilie'
 	},
 	{
 		'title': 'HackITall',
 		'image': 'media/hackitall.jpg',
 		'content': 'Ești pasionat de domeniul IT&C și vrei să surprinzi prin pasiunea și aptitudinile tale? A șaptea ediție a hackathon-ului organizat de LSAC București s-a lăsat așteptată, dar v-a pregatit 24 de ore memorabile în care creativitatea și skill-urile de programare vă vor ajuta sa faceți față provocării pregatite.',
 		'url': '/hackitall',
 		'date': '8 Aprilie'
 	},
 	{
 		'title': 'ELI-NP',
 		'image': 'media/eli-np.png',
 		'content': 'Va invitam sa vizitati platforma ELI-NP (laserul de la Magurele). Scopul vizitei este atat prezentarea platformei de cercetare, cat si atragerea studentilor spre potentiale proiecte de licenta/dizertatie, stagii de practica sau angajare. Vizitele vor avea loc in zilele de 3 si 4 Decembrie.',
 		'url': '/eli-np',
 		'date': '8 Aprilie'
 	},
 	{
 		'title': '3D_UPB',
 		'image': 'media/3dupb.png',
 		'content': 'Dragi studenti, Avem placerea sa va invitam la a 13-a editie a scolii de vara 3DPub, ce gazduieste, in perioada 15 Iunie - 7 August, ~15 workshop-uri in domeniile: - Game Development (programare & conceptie) - Grafica 3D (programare & modelare 3D) - Realitate virtuala si Realitate augmentata - GPGPU - 3D Computer vision (camere 3D, algoritmi)',
 		'url': '/3dupb',
 		'date': '8 Aprilie'
 	},
 	{
 		'title': 'Admitere ACS',
 		'image': 'media/acs.jpg',
 		'content': 'Concursul de admitere pentru studiile de licență la Facultatea de Automatică și Calculatoare, începând din anul universitar 2020-2021, constă în două probe scrise: proba 1 - Algebră şi elemente de analiză matematică, proba 2 – la alegere între Fizică și Informatică.',
 		'url': '/acs',
 		'date': '8 Aprilie'
 	}
 ]

# Create your views here.
def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'avizier/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'avizier/home.html'
	context_object_name = 'posts'


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