from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
import requests
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

API_URL = "http://192.168.10.132/api/v1/data"  # Externe API
class CustomLoginView(FormView):
    form_class = AuthenticationForm

    def get_template_names(self):
        """Kies het juiste template op basis van de URL"""
        if 'admin' in self.request.path:  # Controleer of de URL '/admin/login/' is
            return ['admin_login.html']
        return ['login.html']

    def form_valid(self, form):
        """Verifieer gebruiker en stuur door naar juiste dashboard"""
        user = form.get_user()
        login(self.request, user)

        # Stuur admins naar de admin-site, gewone gebruikers naar hun dashboard
        return redirect('/admin/' if user.is_staff else '/dashboard/')

# ✅ Verplaats `user_dashboard` BUITEN de class
@login_required
@login_required
def user_dashboard(request):
    """Haalt alle API-gegevens op en stuurt ze naar de template"""
    username = request.user.username
    try:
        response = requests.get(f"{API_URL}?username={username}", timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        data = {"error": f"API-fout: {str(e)}"}

    return render(request, 'dashboard.html', {'data': data})
@login_required
def realtime_energie_view(request):
    """Haalt real-time energiegegevens op voor de ingelogde gebruiker."""
    username = request.user.username  # Haal de username van de ingelogde gebruiker op

    try:
        response = requests.get(f"{API_URL}?username={username}", timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        data = {"error": f"API-fout: {str(e)}"}

    return JsonResponse(data)  # JSON response teruggeven
