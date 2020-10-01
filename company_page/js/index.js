var i = 0;
var txt = "Let's make a game!"; /* The text */
var speed = 110; /* The speed/duration of the effect in milliseconds */

function typeWriterslogan() {
  if (i < txt.length) {
    document.getElementById("slogan").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriterslogan, speed);
  }
}

window.onload = typeWriterslogan;