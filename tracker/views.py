from django.shortcuts import render, redirect
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from .models import Arm
from django.db.models import CharField
from django.db.models import Count
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, "You are now logged in")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

@login_required(login_url='login')
def home(request):
    arm_count = Arm.objects.count()
    total_revolver = Arm.objects.filter(arm_type='revolver').count()
    total_pistol = Arm.objects.filter(arm_type='pistol').count()
    total_holster = Arm.objects.filter(arm_type='holster').count()
    total_machine_gun = Arm.objects.filter(arm_type='machine_gun').count()
    total_shot_gun = Arm.objects.filter(arm_type='shot_gun').count()
    total_rifle = Arm.objects.filter(arm_type='rifle').count()
    total_air_gun = Arm.objects.filter(arm_type='air_gun').count()
    total_grenade_launcher = Arm.objects.filter(arm_type='grenade_launcher').count()
    total_smg = Arm.objects.filter(arm_type='smg').count()
    total_lmg = Arm.objects.filter(arm_type='lmg').count()
    total_mortar = Arm.objects.filter(arm_type='mortar').count()
    total_craft_gun = Arm.objects.filter(arm_type='craft_gun').count()
    total_sniper_rifle = Arm.objects.filter(arm_type='sniper_rifle').count()

    context = {
        'arm_count': arm_count,
        'total_revolver': total_revolver,
        'total_pistol': total_pistol,
        'total_holster': total_holster,
        'total_machine_gun': total_machine_gun,
        'total_shot_gun': total_shot_gun,
        'total_rifle': total_rifle,
        'total_air_gun': total_air_gun,
        'total_grenade_launcher': total_grenade_launcher,
        'total_smg': total_smg,
        'total_lmg': total_lmg,
        'total_mortar': total_mortar,
        'total_craft_gun': total_craft_gun,
        'total_sniper_rifle': total_sniper_rifle,
    }

    return render(request, 'home.html', context)


class ArmListJson(BaseDatatableView):
    model = Arm
    columns = ['regimental_number', 'name', 'rank', 'unit', 'arm_type', 'arm_status', 'location']

    def render_column(self, row, column):
        if column == 'name':
            return row.name.upper() if row.name else ''
        elif column == 'rank':
            field = Arm._meta.get_field('rank')
            display_value = dict(field.flatchoices).get(getattr(row, column), '')
            return display_value
        elif column == 'regimental_number':
            return row.regimental_number if row.regimental_number else ''
        elif column == 'unit':
            return row.unit if row.unit else ''
        elif column == 'arm_type':
            field = Arm._meta.get_field('arm_type')
            display_value = dict(field.flatchoices).get(getattr(row, column), '')
            return display_value
        elif column == 'arm_status':
            field = Arm._meta.get_field('arm_status')
            display_value = dict(field.flatchoices).get(getattr(row, column), '')
            return display_value
        elif column == 'location':
            field = Arm._meta.get_field('location')
            display_value = dict(field.flatchoices).get(getattr(row, column), '')
            return display_value
        # Handle other columns similarly
        elif column == 'field_name':  # Replace 'field_name' with the actual field name
            return row.field_name if row.field_name else ''
        # Add more elif statements for other columns as needed
        else:
            return ''  # Default value if column not found

    
    def get_initial_queryset(self):
        return self.model.objects.all()

@login_required(login_url='login')
def arms_list(request):
    arms = Arm.objects.all()
    context = {'arms': arms}
    return render(request, 'arm_list.html', context)




def logoutUser(request):
	logout(request)
	return redirect('login')
