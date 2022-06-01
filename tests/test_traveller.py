from datetime import datetime
from unittest import TestCase

from core.models.payment import Payment
from core.models.traveller import Traveller
from core.models.trip import Trip
from core.types.duration_types import DurationTypes
from core.types.government_id_types import GovernmentIdTypes


class TestTraveller(TestCase):
    def test_add_payment(self):
        # arrange
        traveller = Traveller("traveller 1", "address", "1996/1/1", "+9647734018021")
        trip = Trip("trip 1", datetime.now, DurationTypes.weekend)
        payment = Payment(trip, 10.5)
        # act
        traveller.add_payment(payment)
        # assert
        self.assertEqual(len(traveller.payments), 1, "should have 1")
        self.assertEqual(traveller.payments[0], payment, "should be the same as declared above")

    def test_remove_payment(self):
        # arrange
        traveller = Traveller("traveller 1", "address", "1996/1/1", "+9647734018021")
        trip = Trip("trip 1", datetime.now, DurationTypes.weekend)
        payment1 = Payment(trip, 10.5)
        payment2 = Payment(trip, 12.5)
        traveller.assign_payments([payment1, payment2])
        # act
        traveller.remove_payment(payment1.id)
        # assert
        self.assertEqual(len(traveller.payments), 1, "should have 1")

    def test_assign_payments(self):
        # arrange
        traveller = Traveller("traveller 1", "address", "1996/1/1", "+9647734018021")
        trip = Trip("trip 1", datetime.now, DurationTypes.weekend)
        payment1 = Payment(trip, 10.5)
        payment2 = Payment(trip, 12.5)
        # act
        traveller.assign_payments([payment1, payment2])
        # assert
        self.assertEqual(len(traveller.payments), 2, "should have 2")

    def test_add_government_id(self):
        # arrange
        traveller = Traveller("traveller 1", "address", "1996/1/1", "+9647734018021")
        gov_id = "Gov_Id"
        gov_id_type = GovernmentIdTypes.passport
        # act
        traveller.add_government_id(gov_id, gov_id_type)
        # assert
        self.assertEqual(traveller.government_id, gov_id)
        self.assertEqual(traveller.government_id_type, gov_id_type)