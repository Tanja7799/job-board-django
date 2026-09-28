from django.shortcuts import render
from .services import fetch_jobs

def job_list_view(request):
    jobs = fetch_jobs()

    context = {
        'jobs': jobs
    }
    return render(request, 'jobs/job_list.html',context)



