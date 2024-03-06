#ifndef POLYNOMIAL_H
#define POLYNOMIAL_H

// Represents a term of a polynomial
struct Term
{
	bool operator!=(const Term& right) const
	{
		return coef != right.coef || expon != right.expon;
	}
	int coef;
	int expon;
};

// Polynomial class template definition
template< typename T >
class Polynomial
{
	// Overloaded stream insertion operator
	template< typename T >
	friend ostream& operator<<(ostream& output, Polynomial< T > a);
public:

	// Constructs an empty polynomial, with no terms.
	Polynomial(size_t n = 0)
		: polynomial(n)
	{
	}

	// Constructs a polynomial with a copy of each of the terms in polynomialToCopy.
	Polynomial(const Polynomial& right)
		: polynomial(right.polynomial)
	{
	}

	// Destructor with empty body
	~Polynomial()
	{
	}

	// Copies all the terms from "right" into the polynomial
	const Polynomial< T > operator=(const Polynomial& right)
	{
		if (&right != this) // avoid self-assignment
			polynomial = right.polynomial;

		return *this; // enables x = y = z, for example
	}

	bool operator==(const Polynomial& right)
	{
		return polynomial == right.polynomial;
	}

	void setPolynomial(int coefficient[], int exponent[], int numTerms)
	{
		for (int i = 0; i < numTerms; i++)
		{
			polynomial[i].coef = coefficient[i];
			polynomial[i].expon = exponent[i];
		}
	}

	// addition assignment operator; Polynomial< T > += Polynomial< T >
	void operator+=(Polynomial& op2)
	{
		Polynomial< T > sum;

		int num = 0;
		int i = 0;
		int j = 0;

		for (; i < polynomial.size() && j < op2.polynomial.size();)
		{
			if (polynomial[i].expon < op2.polynomial[j].expon)
			{
				sum.attach(op2.polynomial[j].coef, op2.polynomial[j].expon);
				j++;
			}
			else if (polynomial[i].expon > op2.polynomial[j].expon)
			{
				sum.attach(polynomial[i].coef, polynomial[i].expon);
				i++;
			}
			else if (polynomial[i].expon == op2.polynomial[j].expon)
			{
				if (polynomial[i].coef + op2.polynomial[j].coef != 0)
					sum.attach(polynomial[i].coef + op2.polynomial[j].coef, polynomial[i].expon);
				j++;
				i++;
			}
		}

		if (i == polynomial.size())
		{
			for (; j < op2.polynomial.size(); j++)
				sum.attach(op2.polynomial[j].coef, op2.polynomial[j].expon);
		}
		else if (j == op2.polynomial.size())
		{
			for (; i < polynomial.size(); i++)
				sum.attach(polynomial[i].coef, polynomial[i].expon);
		}
		*this = sum;
	}

	// subtraction assignment operator; Polynomial< T > -= Polynomial< T >
	void operator-=(Polynomial& op2)
	{
		Polynomial< T > minus = -op2;
		*this += minus;
	}

	// multiplication operator; Polynomial< T > * Polynomial< T >
	Polynomial< T > operator*(Polynomial& op2)
	{
		Polynomial< T > product;

		for (int j = 0; j < op2.polynomial.size();j++)
		{
			Polynomial< T > buffer;
			for (int i = 0; i < polynomial.size(); i++)
			{
				buffer.attach(polynomial[i].coef * op2.polynomial[j].coef, polynomial[i].expon + op2.polynomial[j].expon);
			}
			product += buffer;
		}
		return product;
	}

	// modulus operator; Polynomial< T > / Polynomial< T > provided that the divisor is not equal to 0
	Polynomial< T > operator/(Polynomial& op2)
	{
		Polynomial quotient;
		Polynomial remainder(*this);
		Polynomial buffer;
		Polynomial monomial(1);
		int num = 0;
		for (int i = 0; i < remainder.polynomial.size(); i++)
		{
			if (remainder.polynomial[0].expon < op2.polynomial[0].expon)
				return quotient;
			monomial.polynomial[0].expon = (remainder.polynomial[0].expon - op2.polynomial[0].expon);
			monomial.polynomial[0].coef = (remainder.polynomial[0].coef / op2.polynomial[0].coef);
			quotient += monomial;
			buffer = op2 * monomial;
			remainder -= buffer;
			if (remainder.polynomial.empty())
				return quotient;
		}
		return quotient;
	}

	// modulus operator; Polynomial< T > % Polynomial< T > provided that the divisor is not equal to 0
	Polynomial< T > operator%(Polynomial& op2)
	{
		Polynomial quotient;
		Polynomial remainder(*this);
		Polynomial buffer;
		Polynomial monomial(1);
		int num = 0;
		for (int i = 0; i < remainder.polynomial.size(); i++)
		{
			if (remainder.polynomial[0].expon < op2.polynomial[0].expon)
				return remainder;
			monomial.polynomial[0].expon = (remainder.polynomial[0].expon - op2.polynomial[0].expon);
			monomial.polynomial[0].coef = (remainder.polynomial[0].coef / op2.polynomial[0].coef);
			quotient += monomial;;
			buffer = op2 * monomial;
			remainder -= buffer;
			if (remainder.polynomial.empty())
				return remainder;
		}
		return remainder;
	}

private:
	T polynomial; // a polynomial

	// Attaches a new term to the polynomial
	void attach(int coefficient, int exponent)
	{
		Term tempTerm;
		tempTerm.coef = coefficient;
		tempTerm.expon = exponent;
		polynomial.insert(polynomial.end(), tempTerm);
	}

	// Returns the minus of the current polynomial
	Polynomial< T > operator-()
	{
		Polynomial< T > minus(polynomial.size());
		typename T::iterator it2 = minus.polynomial.begin();
		typename T::iterator it1 = polynomial.begin();
		for (; it1 != polynomial.end(); ++it1, ++it2)
		{
			it2->coef = -it1->coef;
			it2->expon = it1->expon;
		}

		return minus;
	}

	// Returns true if and only if polynomial is a zero polynomial
	bool zero() const
	{
		return polynomial.empty();
	}

	// Returns the highest of degrees of polynomial's terms
	int degree() const
	{
		if (polynomial.empty())
			return 0;
		else
			return polynomial.begin()->expon;
	}

}; // end class template Polynomial

// Overloaded stream insertion operator
template< typename T >
ostream& operator<<(ostream& output, Polynomial< T > a)
{
	if (a.zero())
	{
		output << 0 << endl;
		return output;

	}

	typename T::iterator it = a.polynomial.begin();

	if (it->coef < 0)
		cout << "-" << -it->coef;
	else if (it->coef > 0)
		cout << it->coef;

	if (it->expon > 0)
	{
		if (it->expon == 1)
			cout << "x";
		else
			cout << "x^" << it->expon;
	}

	for (++it; it != a.polynomial.end(); ++it)
	{
		if (it->coef < 0)
			cout << " - " << -it->coef;
		else if (it->coef > 0)
			cout << " + " << it->coef;

		if (it->expon > 0)
		{
			if (it->expon == 1)
				cout << "x";
			else
				cout << "x^" << it->expon;
		}
	}

	return output; // enables cout << x << y;
} // end function operator<<

#endif

