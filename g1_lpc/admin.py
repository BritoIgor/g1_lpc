from django.contrib import admin

from .models import Usuario
admin.site.register(Usuario)

from .models import Tipo
admin.site.register(Tipo)

from .models import Compromisso
admin.site.register(Compromisso)

from .models import Agenda
admin.site.register(Agenda)

from .models import Convite
admin.site.register(Convite)

from .models import Resposta_Convite
admin.site.register(Resposta_Convite)
