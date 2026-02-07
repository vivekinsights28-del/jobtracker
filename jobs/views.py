from django.shortcuts import render, redirect
from .models import Job
from .forms import JobForm
from django.contrib.auth.decorators import login_required


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


def add_job(request):
    form = JobForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'jobs/add_job.html', {'form': form})

def edit_job(request, id):
    job = Job.objects.get(id=id)
    form = JobForm(request.POST or None, instance=job)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'jobs/add_job.html', {'form': form})

def delete_job(request, id):
    job = Job.objects.get(id=id)
    job.delete()
    return redirect('/')

