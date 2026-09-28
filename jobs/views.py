from django.shortcuts import render
from .services import fetch_and_save_jobs
from .models import Job

def job_list_view(request):
    fetch_and_save_jobs()  #запускається парсер для оновлення бази новими вакансіями
    jobs = Job.objects.all()

    context = {
        'jobs': jobs
    }
    return render(request, 'jobs/job_list.html',context)



