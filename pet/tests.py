from django.test import TestCase

from .models import Breed , Pet , Order


  
class PetTest(TestCase):

    def setUp(self):
        Pet.objects.create(
            name='Casper', age_days=30, breed='afghani', color='Black',status='Available',description ="hrhwl"
            )
        Pet.objects.create(
          name='Muffin', age_days=60, breed='garden', color='golden',status='Available' ,description ="dada"
        )

    def test_Pets(self):
        pet_casper = Pet.objects.get(name='Casper')
        pet_muffin = Pet.objects.get(name='Muffin')
        self.assertEqual(str(name),"Casper")
   

