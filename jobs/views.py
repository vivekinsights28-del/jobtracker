from django.shortcuts import get_object_or_404, render, redirect
from .models import Job
from .forms import JobForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


@login_required
def job_list(request):
    jobs = Job.objects.filter(user=request.user)

    context = {
        'jobs': jobs,
        'total': jobs.count(),
        'applied': jobs.filter(status='Applied').count(),
        'interview': jobs.filter(status='Interview').count(),
        'offer': jobs.filter(status='Offer').count(),
    }

    return render(request, 'jobs/job_list.html', context)


@login_required
def add_job(request):
    form = JobForm(request.POST or None)

    if form.is_valid():
        job = form.save(commit=False)
        job.user = request.user
        job.save()
        return redirect('/')

    return render(request, 'jobs/add_job.html', {'form': form})

@login_required
def edit_job(request, id):
    job = get_object_or_404(Job, id=id, user=request.user)
    form = JobForm(request.POST or None, instance=job)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'jobs/add_job.html', {'form': form})

@login_required
def delete_job(request, id):
    job = get_object_or_404(Job, id=id, user=request.user)
    job.delete()
    return redirect('/')


def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('/')

    return render(request, 'jobs/register.html', {'form': form})

