from models import Person
all_categories = ['Wishlist','Tech','Clothing','Accesories','Pets','Antiquity','Collectibles','Vehicles','Musical Instruments']

def categories(request):
    me = Person.objects.get(user=request.user.pk)
    categories = [e.name for e in me.belongings.all()]
    notAdded = [e for e in all_categories if e not in categories]
    return {'categories':notAdded}
