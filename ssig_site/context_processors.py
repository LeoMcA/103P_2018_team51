from django.conf import settings as s

def settings(request):
  return {
    'GOOGLE_MAPS_KEY': s.GOOGLE_MAPS_KEY,
  }
