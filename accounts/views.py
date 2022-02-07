from django.shortcuts import render, redirect
from sqlalchemy import true
from .forms import RegisterForm

def register(res):
	if res.method == "POST":
		form = RegisterForm(res.POST)
		if form.is_valid():	
			form.save()
			return redirect("https://sciencium-dev.web.app/")

		dev = False
		
		if dev:
			return redirect("http://localhost:8000/register")
		else:
			return redirect("http://scienciumauth.pythonanywhere.com/register")

	form = RegisterForm()
	params = {
		"form": form
	}

	return render(res, "register/register.html", params)