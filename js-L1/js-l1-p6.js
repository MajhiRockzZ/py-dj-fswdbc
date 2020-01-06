// While Loop

var x = 0;

while (x < 5) {
  console.log("x is currently: " + x);

  if (x === 3) {
    console.log("x IS EQUAL TO THREE!");
    break;
  }

  console.log("x is still less than 5, adding 1 to x");

  x = x + 1;
}

// Write a while Loop that prints out
// only the even numbers from 1 to 10.

var x = 0;

while (x <= 10) {
  if (x % 2 == 0) {
    console.log(x);
  }
  //   x = x + 1;
  x += 1;
}
