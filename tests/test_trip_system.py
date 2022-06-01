from unittest import TestCase

from core.models.trip_system import TripSystem
from core.types.role_types import RoleTypes


class TestTripSystem(TestCase):
    def test_get_trips_for_coordinator_should_get_only_his_trip(self):
        # arrange
        trip_system = TripSystem(False)
        coordinator = "coordinator1"
        trip_system.login(coordinator, "12345")
        # act
        trips = trip_system.get_trips()
        # assert
        self.assertEqual(trips[0].coordinator.name, coordinator)

    def test_get_trip(self):
        # for other than coordinator role, should get all trips
        # arrange
        trip_system = TripSystem(False)
        trip_system.login('a', "a")
        # act
        trips = trip_system.get_trips()
        # assert
        self.assertTrue(len(trips) > 0, "should have trips for demo data setup")

    def test_login_should_fail_when_credential_is_wrong(self):
        # arrange
        trip_system = TripSystem(False)
        # act, assert
        with self.assertRaises(Exception):
            trip_system.login("a", "12")

    def test_login_should_success_when_credential_is_correct(self):
        # arrange
        trip_system = TripSystem(False)
        # act, assert
        trip_system.login("a", "a")

    def test_accepted_role_or_throw_exception_should_allow_when_user_login_have_correct_role(self):
        # arrange
        trip_system = TripSystem(False)
        trip_system.login("coordinator1", "12345")
        # act
        result = trip_system.is_accepted_role(RoleTypes.coordinator)
        # assert
        self.assertTrue(result)

    def is_accepted_role_should_return_false_when_user_login_not_have_correct_role(self):
        # arrange
        trip_system = TripSystem(False)
        trip_system.login("coordinator1", "12345")
        # act
        result = trip_system.is_accepted_role(RoleTypes.manager)
        # assert
        self.assertFalse(result)
