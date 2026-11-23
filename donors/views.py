from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .models import BloodDonor
from .forms import DonorForm
# Create your views here.

# Display all donors and search donors
def donor_list(request):

    donors = BloodDonor.objects.all().order_by('-registered_date')

    blood_group = request.GET.get('blood_group')
    city = request.GET.get('city')

    if blood_group:
        donors = donors.filter(blood_group=blood_group)

    if city:
        donors = donors.filter(city__icontains=city)

    context = {
        'donors': donors,
        'blood_groups': BloodDonor.BLOOD_GROUPS,
    }

    return render(request, 'donors/donor_list.html', context)


# Register a new donor
def register_donor(request):

    if request.method == 'POST':

        form = DonorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('donor_list')

    else:
        form = DonorForm()

    return render(request, 'donors/register.html', {
    'form': form
})



# Change donor availability
@require_POST
def toggle_availability(request, donor_id):

    donor = get_object_or_404(BloodDonor, id=donor_id)

    donor.available = not donor.available

    donor.save()

    return redirect('donor_list')