from core.models import *

class CoreMiddleware:
    def process_request(self, request):
        try:
            myUser = request.user
            me = Person.objects.get(user = myUser.pk)
            print "user name:",me.name
            me.save()
        except: pass
        return None