// string class member-function definitions.

#include <iostream>
using std::cerr;

#include "string.h" // string class definition

string::string()
   : myData()
{
}

string::string( const char *const ptr, const size_type count )
   : myData()
{
	myData.mySize = count;//測茲的大小
	myData.myRes = (myData.mySize / 16) * 16 + 15;//我自己社的空間

	if (myData.myRes > 15)
		myData.bx.ptr = new char[myData.myRes + 1]();//設一個動態陣列放值

	for (unsigned int i = 0;i < myData.mySize;i++)
		myData.myPtr()[i] = ptr[i];//白色放到綠色
	myData.myPtr()[myData.mySize] = '\0';//string最後一個是空自原
}

string::string( const size_type count, const char ch )
   : myData()
{
	myData.mySize = count;//幾個
	myData.myRes = (myData.mySize / 16) * 16 + 15;

	if (myData.myRes > 15)
		myData.bx.ptr = new char[myData.myRes + 1]();//設一個動態陣列放值

	for (int i = 0;i < myData.mySize;i++)
		myData.myPtr()[i] = ch;//ch放進去的字
	myData.myPtr()[myData.mySize] = '\0';
}

string::string( const string &right )
   : myData()
{
	myData.mySize = right.myData.mySize;//幾個
	myData.myRes = (myData.mySize / 16) * 16 + 15;

	if (myData.myRes > 15)
		myData.bx.ptr = new char[myData.myRes + 1]();//設一個動態陣列放值

	for (int i = 0;i < myData.mySize;i++)
		myData.myPtr()[i] = right.myData.myPtr()[i];//ch放進去的字
	myData.myPtr()[myData.mySize] = '\0';
}

string::~string()
{
   if( myData.myRes > 15 )
      delete[] myData.bx.ptr;
}

string& string::operator=( const string &right )
{
   if( this != &right )
   {
	   int len = right.myData.mySize;
	   if (len > myData.myRes) {
		   size_type newMyRes = myData.myRes * 3 / 2;

		   if (newMyRes < (len / 16) * 16 + 15)
			   newMyRes = (len / 16) * 16 + 15;
		   int i = 0;
		   char* cap = new char[newMyRes + 1]();//設一個字元的動態陣列 +1 一開始沒有家是錯的 但後面家是錯的
		   for (;i < len;i++)
			   cap[i] = right.myData.myPtr()[i];//put str2 放進cap

		   cap[i] = '\0';

		   if (myData.mySize > 15)
			   delete[]myData.bx.ptr;//要把原本delete new one will come

		   myData.bx.ptr = cap;//str2 put str1
		   myData.mySize = len;// str 1 mysize
		   myData.myRes = newMyRes;//str1 myres
	   }
	   else {
		   for (int i = 0;i < right.myData.mySize;i++)
			   myData.myPtr()[i] = right.myData.myPtr()[i];

		   myData.myPtr()[len] = '\0';
		   myData.mySize = len;
	   }
   }

   return *this;
}

string& string::operator=( const char * const ptr )
{
   size_t count = strlen( ptr );
   if( count > 0 )
   {
	   if (count > myData.myRes) {
		   size_type newMyRes = myData.myRes * 3 / 2;

		   if (newMyRes < (count / 16) * 16 + 15)
			   newMyRes = (count / 16) * 16 + 15;

		   char* cap = new char[newMyRes + 1]();//設一個字元的動態陣列 +1 一開始沒有家是錯的 但後面家是錯的
		   for (int i = 0;i < count;i++)
			   cap[i] = ptr[i];//put str2 放進cap

		   cap[count] = '\0';

		   if (myData.mySize > 15)
			   delete[]myData.bx.ptr;//要把原本delete new one will come

		   myData.bx.ptr = cap;//str2 put str1
		   myData.mySize = count;// str 1 mysize
		   myData.myRes = newMyRes;//str1 myres
	   }
	   else {
		   for (int i = 0;i < count;i++)
			   myData.myPtr()[i] = ptr[i];//why don't need ()

		   myData.myPtr()[count] = '\0';
		   myData.mySize = count;
	   }
   }
   return *this;
}

string& string::erase( size_t off, size_t count )
{
   if( off < myData.mySize )
   {
	   int des = off + count - 1, back = myData.mySize - off - count;
	   if (back == 0) {
		   myData.myPtr()[off] = '\0';
	   }
	   else {
		   int j = des + 1, i = off;
		   for (;j < myData.mySize;i++, j++)
			   myData.myPtr()[i] = myData.myPtr()[j];//j移動到前面
		   myData.myPtr()[i] = '\0';
	   }
	   myData.mySize -= count;
   }

   return *this;
}

void string::clear()
{
   myData.mySize = 0;
   myData.myPtr()[ 0 ] = value_type();
}

string::iterator string::begin()
{
   return iterator( myData.myPtr() );
}

string::const_iterator string::begin() const
{
   return const_iterator( myData.myPtr() );
}

string::iterator string::end()
{
   return iterator( myData.myPtr() + static_cast< difference_type >( myData.mySize ) );
}

string::const_iterator string::end() const
{
   return const_iterator( myData.myPtr() + static_cast< difference_type >( myData.mySize ) );
}

string::reference string::operator[]( size_type off )
{
   // check for off out-of-range error
   if( off > myData.mySize )
   {
      cerr << "\nstring subscript out of range\n";
      system( "pause" );
      exit( 1 ); // terminate program; off out of range
   }

   return myData.myPtr()[ off ]; // returns copy of this element
}

string::const_reference string::operator[]( size_type off ) const
{
   // check for off out-of-range error
   if( off > myData.mySize )
   {
      cerr << "\nstring subscript out of range\n";
      system( "pause" );
      exit( 1 ); // terminate program; off out of range
   }

   return myData.myPtr()[ off ]; // returns copy of this element
}

string::const_pointer string::data() const
{
   return myData.myPtr();
}

string::size_type string::size() const
{
   return myData.mySize;
}

string::size_type string::find( char ch, size_type off ) const
{
	for (int i = off;i <myData.mySize;i++) {
		if (myData.myPtr()[i] == ch)
			return i;
	}

   return static_cast< size_t >( -1 );
}

string string::substr( size_type off, size_type count ) const
{
   if( off < myData.mySize)
   {
	   char* store;
	   store = new char[myData.mySize + 1];
	   string result;
	   for (int i = off, j = 0;j < count;i++, j++)
		   store[j] = myData.myPtr()[i];
	   store[count] = '\0';
	   result = store;
	   return result;
   }
   return string();
}

// compare [ 0, size() ) with right for equality
bool string::equal( const string &right ) const
{
	if (myData.mySize != right.myData.mySize)
		return false;
	for (int i = 0;i < right.myData.mySize;i++) {
		if (myData.myPtr()[i] != right.myData.myPtr()[i])
			return false;
	}
	return true;
}

bool operator==( const string &left, const string &right )
{
   return left.equal( right );
}

bool operator!=( const string &left, const string &right )
{
   return !left.equal( right );
}

ostream& operator<<( ostream &ostr, string &str )
{
   for( size_t i = 0; i < str.size(); i++ )
      ostr << str.data()[ i ];

   return ostr; // enables cout << x << y;
}