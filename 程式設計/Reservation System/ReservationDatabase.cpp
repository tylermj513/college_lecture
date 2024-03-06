#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
using namespace::std;

#include "ReservationDatabase.h" // ReservationDatabase class definition

extern Date computeCurrentDate();

// call loadReservations and removes outdated reservation informations
ReservationDatabase::ReservationDatabase()
{
	loadReservations();
	Date today = computeCurrentDate();

	if (reservations.size() != 0)
	{
		vector<Reservation>::iterator it = reservations.begin();

		for (; it != reservations.end() && it->getDate() < today;)
		{
			vector<Reservation>::iterator temp = it;
			temp++;
			reservations.erase(it);
			it = temp;
		}
	}
}

// call storeReservations
ReservationDatabase::~ReservationDatabase()
{
	storeReservations();
}

bool ReservationDatabase::empty()
{
	return (reservations.size() == 0);
}

// returns true if there is a Reservation object containing specified reservationNumber
bool ReservationDatabase::exist(string reservationNumber)
{
	vector<Reservation>::iterator it = reservations.begin();

	for (; it != reservations.end(); it++)
		if (it->getReservationNumber() == reservationNumber)
			return true;

	return false;
}

// returns true if there is a Reservation object containing specified reservationNumber and password
bool ReservationDatabase::legal(string reservationNumber, string password)
{
	vector<Reservation>::iterator  it = reservations.begin();

	for (; it != reservations.end(); it++)
	{
		if (it->getReservationNumber() == reservationNumber)
		{
			if (it->getPassword() == password)
				return true;
			else
				return false;
		}
	}
	return false;
}

// returns numCustomers in the Reservation object containing specified reservationNumber
int ReservationDatabase::getNumCustomers(string reservationNumber)
{
	vector< Reservation >::iterator it = getReservation(reservationNumber);
	return it->getNumCustomers();
}

// returns date in the Reservation object containing specified reservationNumber
Date ReservationDatabase::getDate(string reservationNumber)
{
	vector< Reservation >::iterator it = getReservation(reservationNumber);
	return it->getDate();
}

// returns time in the Reservation object containing specified reservationNumber
int ReservationDatabase::getTime(string reservationNumber)
{
	vector< Reservation >::iterator it = getReservation(reservationNumber);
	return it->getTime();
}

// cancels the Reservation object containing specified reservationNumber,
void ReservationDatabase::cancelReservation(string reservationNumber)
{
	vector< Reservation >::iterator it = getReservation(reservationNumber);
	reservations.erase(it);
}

// for the Reservation object containing specified reservationNumber,
// displays all the reservation informations
void ReservationDatabase::displayReservationInfo(string reservationNumber)
{
	cout << setfill(' ') << setw(11) << "Mobile No." << setw(10) << "Name"
		<< setw(14) << "Date" << setw(9) << "Time" << setw(30) << "Email"
		<< setw(19) << "No of Customers" << setw(12) << "Password"
		<< setw(19) << "Reservation No." << endl;

	vector< Reservation >::iterator it = getReservation(reservationNumber);
	it->displayReservationInfo();
}

// adds newReservation at the end of reservations
void ReservationDatabase::pushBack(Reservation newReservation)
{
	reservations.push_back(newReservation);
}

// loads reservations from the file Reservations.dat
void ReservationDatabase::loadReservations()
{
	fstream file("Reservations.dat", ios::in | ios::binary);
	while (!file.eof()) {
		Reservation buf;
		file.read(reinterpret_cast<char*>(&buf), sizeof(buf));
		reservations.push_back(buf);
	}
}

// stores reservations into the file Reservations.dat
void ReservationDatabase::storeReservations()
{
	fstream file("Reservations.dat", ios::out | ios::binary | ios::trunc);
	for (int i = 0; i < reservations.size(); i++) {
		file.write(reinterpret_cast<const char*>(&reservations[i]), sizeof(Reservation));
	}
}

// returns an iterator that points to the Reservation object containing specified reservationNumber
vector< Reservation >::iterator ReservationDatabase::getReservation(string reservationNumber)
{
	vector<Reservation>::iterator it = reservations.begin();

	for (; it != reservations.end(); it++)
		if (it->getReservationNumber() == reservationNumber)
			break;

	return it;
}