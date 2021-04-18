from django.contrib import admin
from .models import service
from .models import review
from .models import service_cost
from .models import fast_online_order
from .models import our_gallery

# Register your models here.
admin.site.register(service)
admin.site.register(review)
admin.site.register(service_cost)
admin.site.register(fast_online_order)
admin.site.register(our_gallery)