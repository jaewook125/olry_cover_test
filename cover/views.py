from django.shortcuts import render, redirect
from django.http import HttpResponse
from PIL import Image
from .forms import CoverForm

def index(request):
	if request.method == "POST":
		form = CoverForm(request.POST)
		if form.is_valid():
			form.cleaned_data #이미지를 생성할 데이터는 여기에 있다
			return redirect("cover:index")
	else:
		form = CoverForm()
	return render(request, 'cover/index.html', {
			'form':form, 
		})


def image_generater(request):
	im = Image.new("RGB", (256,256))
	# im : 위 데이터를 받아서, 이미지는 여기에서 그림
	
	response = HttpResponse(content_type='image/jpeg') #file-like
	im.save(response, format='JPEG')
	return response