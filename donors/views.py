from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .models import BloodDonor
from .forms import DonorForm


# Read: display all donors, with search by blood group, city and name
def donor_list(request):

    donors = BloodDonor.objects.all().order_by('-registered_date')

    blood_group = request.GET.get('blood_group', '').strip()
    city = request.GET.get('city', '').strip()
    name = request.GET.get('name', '').strip()

    if blood_group:
        donors = donors.filter(blood_group=blood_group)

    if city:
        donors = donors.filter(city__icontains=city)

    if name:
        donors = donors.filter(name__icontains=name)

    context = {
        'donors': donors,
        'blood_groups': BloodDonor.BLOOD_GROUPS,
        'selected_blood_group': blood_group,
        'search_city': city,
        'search_name': name,
        'total_count': BloodDonor.objects.count(),
        'available_count': BloodDonor.objects.filter(available=True).count(),
    }

    return render(request, 'donors/donor_list.html', context)


# Create: register a new donor
def register_donor(request):

    if request.method == 'POST':
        form = DonorForm(request.POST)

        if form.is_valid():
            donor = form.save()

            messages.success(
                request,
                f'Donor "{donor.name}" was registered successfully.'
            )

            return redirect('donor_list')

        messages.error(
            request,
            'Please correct the errors below and try again.'
        )

    else:
        form = DonorForm()

    context = {
        'form': form,
        'form_title': 'Register New Donor',
        'submit_label': 'Register Donor',
    }

    return render(
        request,
        'donors/donor_form.html',
        context
    )


# Update: edit an existing donor
def update_donor(request, donor_id):

    donor = get_object_or_404(BloodDonor, id=donor_id)

    if request.method == 'POST':
        form = DonorForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            messages.success(request, f'Donor "{donor.name}" was updated successfully.')
            return redirect('donor_list')
    else:
        form = DonorForm(instance=donor)

    return render(request, 'donors/donor_form.html', {
        'form': form,
        'donor': donor,
        'form_title': f'Edit Donor: {donor.name}',
        'submit_label': 'Save Changes',
    })


# Delete: confirm page (GET) and actual deletion (POST)
def delete_donor(request, donor_id):

    donor = get_object_or_404(BloodDonor, id=donor_id)

    if request.method == 'POST':
        name = donor.name
        donor.delete()
        messages.success(request, f'Donor "{name}" was deleted.')
        return redirect('donor_list')

    return render(request, 'donors/donor_confirm_delete.html', {'donor': donor})


# Change donor availability
@require_POST
def toggle_availability(request, donor_id):

    donor = get_object_or_404(BloodDonor, id=donor_id)

    donor.available = not donor.available
    donor.save()

    status = 'available' if donor.available else 'unavailable'
    messages.info(request, f'{donor.name} is now marked as {status}.')

    return redirect('donor_list')
