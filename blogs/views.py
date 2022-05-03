from django.shortcuts import render


def blogs_index(request):
	blogs = [
		{'name':'my firs blog', 'author':{'name': 'admin'},'publication_date':
		'14.04.22' },
		{'name':'my second blog', 'author':{'name': 'admin'},'publication_date':
		'15.04.22'},
		{'name':'my therd blog', 'author':{'name': 'admin'},'publication_date':
		'16.04.22'},
	]

	context = {
			'blogs': blogs
	}

	return render(request, 'blogs/blogs_index.html', context)


def user_page(request):
	user_data = {
		'user_name': 'salavat',
		'user_age': 15
	}
	context = {
		'user_data': user_data
	}
	return render(request, 'blogs/user_page.html', context)

def first_blog(request):
	first_blog = "мой первй блог"
	context = {
		'first_blog': first_blog
	}
	return render(request, 'blogs/first_blog.html', context)


def first_blog(request):
	first_blog = "мой первй блог"
	context = {
		'first_blog': first_blog
	}
	return render(request, 'blogs/first_blog.html', context)


def phone_models(request):
	phone_models = "мой первй блог"
	context = {
		'phone_models': phone_models
	}
	return render(request, 'blogs/phone_models.html', context)



