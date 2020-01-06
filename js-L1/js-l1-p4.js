// Greater Than
3 > 2;
2 > 3;

// Less Than
1 < 2;

// Greater than or equal to
2 >= 2;

// Less than or equal to
1 <= 3;

// Let's now discuss equality and it's quirk

// Equality
2 == 2;
"username" == "username";

// Inequality
2 != 3;

// Hold on a second! What happens with this.
"2" == 2;

// true and false
true == 1; // true
true === 1; // false

false == 0; // true
false === 0; // false

// Weird behaviour for null, undefined, and NaN
null == undefined; // true
null === undefined; // false
NaN == NaN; // false

// Logical Operators

// AND is written with &&
1 === 1 && 2 === 2;

// OR is written with ||
1 === 2 || 1 === 1;

// NOT is written with !
!(1 === 1);
!!(1 === 1);
