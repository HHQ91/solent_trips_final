from unittest import TestCase

from core.models.trip_system import TripSystem
from core.types.role_types import RoleTypes


class TestTripSystem(TestCase):
    def test_get_trips_for_coordinator_should_get_only_his_trip(self):
        # arrange
        trip_system = TripSystem(False)
        coordinator = "coordinator1"
        trip_system.logging_in(coordinator, "12345")
        # act
        trips = trip_system.get_trips()
        # assert
        self.assertEqual(len(trips), 1, "each coordinator assign to one trip")
        self.assertEqual(trips[0].coordinator.name, coordinator)

    def test_get_trip(self):
        # for other than coordinator role, should get all trips
        # arrange
        trip_system = TripSystem(False)
        trip_system.logging_in('a', "a")
        # act
        trips = trip_system.get_trips()
        # assert
        self.assertTrue(len(trips) > 0, "should have trips for demo data setup")

    def test_logging_in_should_fail_when_credential_is_wrong(self):
        # arrange
        trip_system = TripSystem(False)
        # act, assert
        with self.assertRaises(Exception):
            trip_system.logging_in("a", "12")

    def test_logging_in_should_success_when_credential_is_correct(self):
        # arrange
        trip_system = TripSystem(False)
        # act, assert
        trip_system.logging_in("a", "a")

    def test_accepted_role_or_throw_exception_should_throw_exception_when_user_login_not_have_correct_role(self):
        # arrange
        trip_system = TripSystem(False)
        trip_system.logging_in("coordinator1", "12345")
        # act, assert
        with self.assertRaises(Exception):
            trip_system.accepted_role_or_throw_exception(RoleTypes.manager)

    def test_accepted_role_or_throw_exception_should_allow_when_user_login_have_correct_role(self):
        # arrange
        trip_system = TripSystem(False)
        trip_system.logging_in("coordinator1", "12345")
        # act, assert
        trip_system.accepted_role_or_throw_exception(RoleTypes.coordinator)
