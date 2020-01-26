var countries = [
  "USA",
  "Germany",
  "India",
  "Nepal",
  "Sri Lanka",
  "Canada",
  "Korea"
];

console.log(countries);

countries[2] = "France";

// immutable
let country_1 = "USA";
console.log(country_1[2]);
// country_1[2] = "B" // TypeError: Cannot assign to read only property.
console.log(country_1[2]);
// mutable
countries[2] = "Spain";

console.log("-------------------------");

var mixed = [true, 20, "string"];
mixed;
mixed.length;

var myArr = ["one", "two", "three"];
var lastItem = myArr.pop();
lastItem;
myArr;
myArr.push("new_item");
myArr;
myArr[myArr.length - 1];
var matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];
matrix;

// Array Iteration
var arr = ["A", "B", "C"];

arr;

for (var i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}

for (letter of arr) {
  console.log(letter);
}

arr.forEach(alert)

function addAwesome(name) {
    console.log(name + " is awesome!");
}

addAwesome("django")

var topics = ["python", "django", "science"]
topics.forEach(addAwesome)
