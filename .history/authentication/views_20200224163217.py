from django.shortcuts import render

# Create your views here.def login_view(request):
    html = "genericForm.html"

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data["username"],
                                password=data["password"])
            if user:
                login(request, user)
                return redirect(request.GET.get("next", "/"))
            else:
                return HttpResponse("invalid authentication")

    form = LoginForm()

    return render(request, html, {'form': form})
