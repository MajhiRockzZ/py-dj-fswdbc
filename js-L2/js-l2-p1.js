function hello() {
  console.log("hello world!");
}

hello();

function helloYou(name) {
  console.log("Hello " + name);
}

helloYou("JavaScript");

function addNum(num1, num2) {
  console.log(num1 + num2);
}

addNum(1, 2);
addNum("Hello", " World");

function helloSomeone(name = "Frankie") {
  console.log("Hello" + name);
}

helloSomeone();

function formal(name = "Sam", title = "Sir") {
  return title + " " + name;
}

"Welcom " + formal();

function timesFive(numInput) {
  var result = numInput * 5;
  return result;
}

timesFive(4);
var answer = timesFive(10);
answer;

// SCOPE IN JS

// Local Scope
function timesFive(numInput) {
  //   Local scope to the function !
  var result = numInput * 5;
  return result;
}

// Global Scope
var v = " GLOBAL V";
var stuff = "GLOBAL STUFF";

function fun(stuff) {
  console.log(v);
  stuff = "Reassign stuff inside func";
  console.log(stuff);
}

fun();
console.log(stuff);
