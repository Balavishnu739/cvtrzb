from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
def index(request):
    message = ""
    if request.method == "POST":
        if request.POST.get("password","") == "123":
            return redirect("/house")
        else:
            message = "Incorrect password"
    context = {"message": message}
    return render(request, "index.html", context)
def house(request):
    return render(request,"page2.html")
