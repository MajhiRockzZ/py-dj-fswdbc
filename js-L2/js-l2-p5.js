/* ---- Object Example ---- */
var simple = {
  prop: "Hello",
  myMethod: function() {
    console.log("The myMethod was called");
  }
};

simple;
console.dir(simple);

simple.myMethod;
simple.myMethod();

/* ---- this Example ---- */
var myObj = {
  name: "Sumesh",
  greet: function() {
    console.log("Hello" + this.name);
  }
};

myObj;
myObj.name;
myObj.greet();
