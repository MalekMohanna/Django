-- SQLite
Dojo.objects.create(name='Champions',city='NewYork',state='NY')
Dojo.objects.create(name='Kings',city='LosAngeles',state='LA')
Dojo.objects.create(name='Awesome',city='Huston',state='TX')
a=Dojos.objects.all()
a.delete()
Ninja.objects.create(dojo=Dojo.objects.get(id=4 ),first_name='Malek',last_name='Mhanna')
Ninja.objects.create(dojo=Dojo.objects.get(id=4),first_name='Ahmad',last_name='Mostafa')
Ninja.objects.create(dojo=Dojo.objects.get(id=4),first_name='Rick',last_name='Sanchez')
Ninja.objects.create(dojo=Dojo.objects.get(id=5 ),first_name='Jameel',last_name='Saad')
Ninja.objects.create(dojo=Dojo.objects.get(id=5),first_name='Martin',last_name='dell')
Ninja.objects.create(dojo=Dojo.objects.get(id=5),first_name='Rex',last_name='flex')
Ninja.objects.create(dojo=Dojo.objects.get(id=6),first_name='Morty',last_name='Smith')
Ninja.objects.create(dojo=Dojo.objects.get(id=6),first_name='Beth',last_name='Rick')
Ninja.objects.create(dojo=Dojo.objects.get(id=6),first_name='Ahmad',last_name='Salamah')
Dojo.objects.first().ninjas.all()
Dojo.objects.last().ninjas.all()
Dojo.objects.last().ninjas.last()
Dojo.objects.create(name="Axsos",city="Ramallah",state="PS",desc="New Dojo")