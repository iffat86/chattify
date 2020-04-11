# # # chat/views.py
# # from django.shortcuts import render, redirect
# # from django.contrib.auth.forms import UserCreationForm
# # from django.contrib.auth.decorators import login_required
# # from .forms import CreateUserForm
# # from django.contrib.auth import authenticate, login, logout


# # def index(request):
# #     context = {}
# #     return render(request, 'registration/index.html', context)



# # def room(request, room_name):
# #     return render(request, 'registration/room.html', {'room_name': room_name})


# # def signup(request):
# #     if request.method == 'POST':
# #         form = CreateUserForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             user = form.cleaned_data.get('username')
# #             messages.success(request, 'acoount was created for' + user)
# #             return redirect('registration/login_url')
# #     else:
# #         form = CreateUserForm()
# #         return render(request, 'registration/signup.html', {'form':form})


# # def login(request):
# #     return render(request, 'login')

# from django.shortcuts import render, redirect 
# from django.http import HttpResponse
# from django.forms import inlineformset_factory
# from django.contrib.auth.forms import UserCreationForm
# from .forms import CreateUserForm
# from django.contrib.auth import authenticate, login, logout

# from django.contrib import messages

# from django.contrib.auth.decorators import login_required

# def signup(request):
# 	if request.user.is_authenticated:
# 		return redirect('index')
# 	else:
# 		form = CreateUserForm()
# 		if request.method == 'POST':
# 			form = CreateUserForm(request.POST)
# 			if form.is_valid():
# 				form.save()
# 				user = form.cleaned_data.get('username')
# 				messages.success(request, 'Account was created for ' + user)

# 				return render(request, registration/login.html)
			

# 		context = {'form':form}
# 		return render(request, 'registration/signup.html', context)

# def login(request):
# 	if request.user.is_authenticated:
# 		return redirect('room.html')
# 	else:
# 		if request.method == 'POST':
# 			username = request.POST.get('username')
# 			password =request.POST.get('password')

# 			user = authenticate(request, username=username, password=password)

# 			if user is not None:
# 				return render(request, 'registration/room.html')
# 			else:
# 				messages.info(request, 'Username OR password is incorrect')

# 		context = {}
# 		return render(request, 'login.html', context)

# def logoutUser(request):
# 	logout(request)
# 	return redirect('registration/login.html')


# @login_required(login_url='login')
# def index(request, room_name):
#      return render(request, 'registration/room.html', {'room_name': room_name})


from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
def index(request):
      return render(request, 'registration/index.html')

def signup(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return render(request, 'registration/login.html')
			

		context = {'form':form}
		return render(request, 'registration/signup.html', context)

def login(request):
	if request.user.is_authenticated:
		return render(request, 'registration/room.html')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:

				return render(request, 'registration/room.html')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('registration/login.html')


# @login_required(login_url='login')
# # def index(request):
# #      return render(request, 'registration/room.html')

