from home.models import login_auth
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

class myadminsite(AdminSite):
    site_title=ugettext_lazy('Koshinder Administration')
    site_header=ugettext_lazy('Koshinder Administration')
    index_title=ugettext_lazy('Koshinder Administration')

M_A_S=myadminsite()
M_A_S.register(login_auth)