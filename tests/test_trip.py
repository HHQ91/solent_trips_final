from datetime import datetime
from unittest import TestCase

from core.models.support_stuff import SupportStuff
from core.models.traveller import Traveller
from core.models.trip import Trip
from core.models.trip_leg import TripLeg
from core.models.user import User
from core.types.duration_types import DurationTypes
from core.types.role_types import RoleTypes
from core.types.transport_mode_types import TransportModeTypes


class TestTrip(TestCase):
    def test_assign_coordinator(self):
        # arrange
        trip = Trip("trip 1", datetime.now, DurationTypes.weekend)
        coordinator = User("username", "pass", RoleTypes.coordinator)
        # act
        trip.assign_coordinator(coordinator)
        # assert
        self.assertEqual(trip.coordinator, coordinator, "should have coordinator same as declared above")

    def test_add_traveller(self):
        # arrange
        trip = Trip("trip 1", datetime.now, DurationTypes.weekend)
        traveller = Traveller("traveller", "address", "1996/1/1", "+9647734018021")
        # act
        trip.add_traveller(traveller)
        # assert
        self.assertEqual(len(trip.travellers), 1, "should have 1")
        self.assertEqual(trip.travellers[0], traveller, "should be the same as declared above")

    def test_remove_traveller(self):
        # arrange
        trip = Trip("trip 1", datetime.now, DurationTypes.weekend)
        traveller1 = Traveller("traveller 1", "address", "1996/1/1", "+9647734018021")
        traveller2 = Traveller("traveller 2", "address", "1996/1/1", "+9647734018021")
        trip.assign_travellers([traveller1, traveller2])
        # act
        trip.remove_traveller(traveller1.id)
        # assert
        self.assertEqual(len(trip.travellers), 1, "should have 1")

    def test_assign_travellers(self):
        # arrange
        trip = Trip("trip 1", datetime.now, DurationTypes.weekend)
        traveller1 = Traveller("traveller 1", "address", "1996/1/1", "+9647734018021")
        traveller2 = Traveller("traveller 2", "address", "1996/1/1", "+9647734018021")
        # act
        trip.assign_travellers([traveller1, traveller2])
        # assert
        self.assertEqual(len(trip.travellers), 2, "should have 2")

    def test_add_trip_leg(self):
        # arrange
        trip = Trip("trip 1", datetime.now, DurationTypes.weekend)
        trip_leg = TripLeg("start location", "destination", TransportModeTypes.taxi)
        # act
        trip.add_trip_leg(trip_leg)
        # assert
        self.assertEqual(len(trip.trip_legs), 1, "should have 1")
        self.assertEqual(trip.trip_legs[0], trip_leg, "should be the same as declared above")

    def test_remove_trip_leg(self):
        # arrange
        trip = Trip("trip 1", datetime.now, DurationTypes.weekend)
        trip_leg1 = TripLeg("start location 1", "destination 1", TransportModeTypes.taxi)
        trip_leg2 = TripLeg("start location 2", "destination 2", TransportModeTypes.taxi)
        trip.assign_trip_legs([trip_leg1, trip_leg2])
        # act
        trip.remove_trip_leg(trip_leg1.id)
        # assert
        self.assertEqual(len(trip.trip_legs), 1, "should have 1")

    def test_assign_trip_legs(self):
        # arrange
        trip = Trip("trip 1", datetime.now, DurationTypes.weekend)
        trip_leg1 = TripLeg("start location 1", "destination 1", TransportModeTypes.taxi)
        trip_leg2 = TripLeg("start location 2", "destination 2", TransportModeTypes.taxi)
        # act
        trip.assign_trip_legs([trip_leg1, trip_leg2])
        # assert
        self.assertEqual(len(trip.trip_legs), 2, "should have 2")

    def test_add_support_stuff(self):
        # arrange
        trip = Trip("trip 1", datetime.now, DurationTypes.weekend)
        support_stuff = SupportStuff("stuff 1")
        # act
        trip.add_support_stuff(support_stuff)
        # assert
        self.assertEqual(len(trip.support_stuffs), 1, "should have 1")
        self.assertEqual(trip.support_stuffs[0], support_stuff, "should be the same as declared above")

    def test_remove_support_stuff(self):
        # arrange
        trip = Trip("trip 1", datetime.now, DurationTypes.weekend)
        support_stuff1 = SupportStuff("stuff 1")
        support_stuff2 = SupportStuff("stuff 2")
        trip.assign_support_stuffs([support_stuff1, support_stuff2])
        # act
        trip.remove_support_stuff(support_stuff1.id)
        # assert
        self.assertEqual(len(trip.support_stuffs), 1, "should have 1")

    def test_assign_support_stuffs(self):
        # arrange
        trip = Trip("trip 1", datetime.now, DurationTypes.weekend)
        support_stuff1 = SupportStuff("stuff 1")
        support_stuff2 = SupportStuff("stuff 2")
        # act
        trip.assign_support_stuffs([support_stuff1, support_stuff2])
        # assert
        self.assertEqual(len(trip.support_stuffs), 2, "should have 2")

