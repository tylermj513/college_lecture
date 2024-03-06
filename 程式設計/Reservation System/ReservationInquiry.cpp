#include <iostream>
using namespace::std;

#include "ReservationInquiry.h"

extern int inputAnInteger(int begin, int end);

ReservationInquiry::ReservationInquiry(ReservationDatabase& theReservationDatabase,
	AvailTableDatabase& theAvailTableDatabase)
	: reservationDatabase(theReservationDatabase),
	availTableDatabase(theAvailTableDatabase)
{
}

// reservation inquiry
void ReservationInquiry::execute()
{
	if (reservationDatabase.empty())
	{
		cout << "\nNo reservations!\n";
		return;
	}

	string  choice;
	string reservationnumber;
	cout << "\nEnter reservation number: ";
	cin >> reservationnumber;
	cout << "\n";
	string password;

	cout << "Enter reservation password: ";
	cin >> password;
	cout << "\n";
	cin.ignore();

	if (reservationDatabase.exist(reservationnumber))
	{
		if (reservationDatabase.legal(reservationnumber, password))
		{
			reservationDatabase.displayReservationInfo(reservationnumber);

			cout << "\nCancel this reservation? (y/n) ";
			cin >> choice;
			cin.ignore();

			if (choice == "y")
			{
				int numCostumer = reservationDatabase.getNumCustomers(reservationnumber);
				Date date = reservationDatabase.getDate(reservationnumber);
				int time = reservationDatabase.getTime(reservationnumber);

				availTableDatabase.increaseAvailTables(numCostumer, date, time);
				reservationDatabase.cancelReservation(reservationnumber);

				cout << "\nThis reservation has been canceled." << endl;
			}
		}
	}
	else
		cout << "No reservations with this reservation number!" << endl;
}