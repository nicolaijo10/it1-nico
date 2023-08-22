const utskrift = document.getElementById("utskrift")
//utskrift.innerText = "test";
//console.log(utskrift);

const språk = navigator.language;
console.log("Nettleser: " + språk);
if (språk === "nb-NO" || språk == "nb") {
    console.log("Du har norsk språk i nettleseren");
} else if(språk === "us") {
    console.log("Amerikansk.");
}
else {
    console.log("Du har et annet språk..");
}

const plattform = navigator.platform
console.log("Plattform:" + plattform);

const nettleser = navigator.userAgent;
console.log("Nettleser" + nettleser);
if (nettleser.includes("x64")) {
    console.log("Du sitter på et 64-bits system");
} else {
    console.log("Du har 32-bit");
}

//hent ut størrelsen på body/skjerm (screen, document)
let hoyde = window.innerHeight;
console.log("Høyde: " + hoyde);
let hoydeScreen = screen.height;
console.log("Høyde (screen): " + hoydeScreen)

let bredde = window.innerWidth;
console.log("Bredde: " + bredde);
let breddeScreen = screen.width;
console.log("Bredde (screen): " + breddeScreen)


// Hent ut geolokasjon, se gjerne W3Schools...
const x = document.getElementById("demo");
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude +
  "<br>Longitude: " + position.coords.longitude;
}

console.log(navigator.geolocation.getCurrentPosition(showPosition));

