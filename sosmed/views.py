from django.shortcuts import render,redirect

# Create your views here.
from .models import instagram
from .forms import instagramform
from django.views.generic.base import TemplateView,RedirectView,View

class SosmedListView(TemplateView):
	template_name = 'sosmed/list.html'

	def get_context_data(self,*args,**kwargs):
		semua_akun = instagram.objects.all()
		context = {
			'page_title':'Sosial Media Memakai Class Bases View',
			'semua_akun':semua_akun
		}
		return context


class SosmedDeleteView(RedirectView):
	pattern_name = 'sosmed:list'

	def get_redirect_url(self,*args,**kwargs):
		delete_id = kwargs['delete_id']

		instagram.objects.filter(id=delete_id).delete()
		return super().get_redirect_url()


"""def delete(request,delete_id):
	instagram.objects.filter(id=delete_id).delete()
	return redirect('sosmed:list')"""


class SosmedFormView(View):
	template_name = 'sosmed/create.html'
	form = None
	context = {}

	def get(self,*args,**kwargs):
		print('ini adalah get')



def create(request):
	akun_form = instagramform(request.POST or None)#, initial='nama_depan':'bento'# membuat seperti insial atau rekomendasis

	if request.method == 'POST':
		if akun_form.is_valid():
			akun_form.save()

		return redirect('sosmed:list')

	context = {
		'page_title':'Tambah akun',
		'akun_form':akun_form
	}
	return render(request,'sosmed/create.html',context)


def update(request,update_id):
	akun_update = instagram.objects.get(id=update_id)

	data={
		'nama_depan':akun_update.nama_depan,
		'nama_belakang':akun_update.nama_belakang,
		'username':akun_update.username,
	}
	akun_form = instagramform(request.POST or None,initial=data, instance=akun_update)# instance untuk menyambungkan dengan akun_update

	if request.method == 'POST':
		if akun_form.is_valid():
			akun_form.save()
		return redirect('sosmed:list')

	context = {
		'page_title':'Update akun',
		'akun_form':akun_form
	}
	return render(request,'sosmed/create.html',context)
