from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404


SECONDS_IN_HOUR = 3600


def is_visit_strange(visit):
    more_than_hour = visit.get_duration() > SECONDS_IN_HOUR
    return more_than_hour


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []

    for visit in visits:
        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': visit.format_duration(visit.get_duration()),
            'is_strange': is_visit_strange(visit),
        })
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
