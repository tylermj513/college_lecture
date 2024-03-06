#include <iostream>
#include <fstream>
using namespace::std;

#include "AvailTableDatabase.h"

// tableTypes[ i ] is the table type for i customers
const int tableTypes[13] = { 0, 1, 1, 2, 2, 3, 4, 4, 0, 0, 5, 5, 5 };

extern Date computeCurrentDate();

// calls loadAvailTables(), removes outdated available table informations and
// adds new available table informations
AvailTableDatabase::AvailTableDatabase()
{
	/*Date current;
	computeCurrentDate();
	Date date;
	date = current + 1;*/

	loadAvailTables();
	Date today = computeCurrentDate();
	int theNumAvailTable[4] = { 0, 2, 2, 2 };

	if (availTables.size() == 0)
	{
		for (int i = 0; i < 30; i++, today = today.operator+(1))
		{
			AvailTable temp(today, theNumAvailTable);
			availTables.push_back(temp);
		}
	}

	else
	{
		vector<AvailTable>::iterator it = availTables.begin();
		vector<AvailTable>::iterator end = availTables.end();
		end--;

		for (; it != availTables.end() && it->getDate() < today; end--)
		{
			vector<AvailTable>::iterator temp = it;
			temp++;
			availTables.erase(it);
			it = temp;
			AvailTable Temp(end->getDate().operator+(1), theNumAvailTable);
			availTables.push_back(Temp);
		}
	}
}

// call storeAvailTables
AvailTableDatabase::~AvailTableDatabase()
{
	storeAvailTables();
}

// increases the number of available tables by one on date and timeCode for corresponding table type
void AvailTableDatabase::increaseAvailTables(int numCustomers, Date date, int timeCode)
{
	int tableType = tableTypes[numCustomers];
	vector< AvailTable >::iterator it = getAvailTable(date);
	it->increaseAvailTables(timeCode, tableType);
}

// decreases the number of available tables by one on date and timeCode for corresponding table type
void AvailTableDatabase::decreaseAvailTables(int numCustomers, Date date, int timeCode)
{
	int tableType = tableTypes[numCustomers];
	vector< AvailTable >::iterator it = getAvailTable(date);
	it->decreaseAvailTables(timeCode, tableType);
}

// returns true if there are available tables on date for corresponding table type
bool AvailTableDatabase::availableTables(int numCustomers, Date date)//opposite
{
	int tabletype = tableTypes[numCustomers];
	vector<AvailTable>::iterator it = getAvailTable(date);

	for (int i = 1; i < 4; i++)
		if (it->getNumAvailTables(i, tabletype) != 0)
			return true;

	return false;
}

// returns true if there are available tables on date and timeCode for corresponding table type
bool AvailTableDatabase::availableTables(int numCustomers, Date date, int timeCode)//opposite
{
	int tabletype = tableTypes[numCustomers];
	vector<AvailTable>::iterator it = getAvailTable(date);

	if (it->getNumAvailTables(timeCode, tabletype) != 0)
		return true;
	else
		return false;
}

void AvailTableDatabase::loadAvailTables()
{
	ifstream file("AvailTables.dat", ios::in | ios::binary);

	AvailTable temp;
	while (file.peek() != EOF)
	{
		file.read(reinterpret_cast<char*> (&temp), sizeof(AvailTable));
		availTables.push_back(temp);
	}
	file.close();
}

void AvailTableDatabase::storeAvailTables()
{
	ofstream file("AvailTables.dat", ios::out | ios::binary);

	for (int i = 0; i < availTables.size(); i++)
		file.write(reinterpret_cast<char*> (&availTables[i]), sizeof(AvailTable));
}

// returns an iterator that points to the AvailTable object containing specified date
vector< AvailTable >::iterator AvailTableDatabase::getAvailTable(Date date)
{
	vector< AvailTable >::iterator it = availTables.begin();
	for (int i = 0; i < availTables.size(); i++, it++) {
		if (availTables[i].getDate() == date)
			return it;
	}
	return availTables.end();
}