from django.shortcuts import redirect

def login_redirect(request):
    return redirect('/patient_info/login')