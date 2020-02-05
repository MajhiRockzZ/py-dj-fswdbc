/* EVENTS */
$("h1").click(function() {
  console.log("There was a click!");
});

$("li").click(function() {
  console.log("Any li was clicked!");
});

$("h1").click(function() {
  $(this).text("I was changed!");
});

/* KEY PRESS */
$("input")
  .eq(0)
  .keypress(function() {
    $("h3").toggleClass("turnBlue");
  });

$("input")
  .eq(0)
  .keypress(function(event) {
    if (event.which === 13) {
      $("h3").toggleClass("turnBlue");
    }
  });

/* on() */
$("h1").on("dbclick", function() {
  $(this).toggleClass("turnBlue");
});

$("h1").on("mouseenter", function() {
  $(this).toggleClass("turnBlue");
});

$("input")
  .eq(1)
  .on("click", function() {
    $(".container").fadeOut(3000);
  });
