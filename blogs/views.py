from django.shortcuts import render


def index(request):
	blogs = [
	'первый блог',
	'второй блог',
	'третий блог',
	'четвертый блог'
	]

	context = {
	'blogs': blogs
	}

	return render(request, 'blogs/index.html', context)


def user(request):
	user_name = 'salavat'
	age = '15'
	context = {
		'user_name': user_name,
		'age': age
	}
	return render(request, 'blogs/user.html', context)
