from django.shortcuts import render, get_object_or_404
from .models import Post, Tag

# Create your utils here.


class ObjectDetailMixim:
	model = None
	tempiate = None	

	def get(self, request, slug):
		obj = get_object_or_404(self.model, slug__iexact=slug)
		return render(request, self.template, context={self.model.__name__.lower(): obj})
