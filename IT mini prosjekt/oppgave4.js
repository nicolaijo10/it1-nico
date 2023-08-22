// Opprett en array med 500 tilfeldige heltall
var array = [];
for (var i = 0; i < 500; i++) {
  array.push(Math.floor(Math.random() * 1000)); // Tilfeldig tall fra 0 til 999
}

// Funksjon for å finne høyeste verdi i arrayen
function finnHoyesteVerdi(arr) {
  var hoyesteVerdi = arr[0];
  for (var i = 1; i < arr.length; i++) {
    if (arr[i] > hoyesteVerdi) {
      hoyesteVerdi = arr[i];
    }
  }
  return hoyesteVerdi;
}

// Funksjon for å telle antallet ganger et gitt tall opptrer i arrayen
function tellAntall(tall, arr) {
  var antall = 0;
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] === tall) {
      antall++;
    }
  }
  return antall;
}

// Testfunksjoner
var hoyesteVerdi = finnHoyesteVerdi(array);
console.log("Høyeste verdi i arrayen er: " + hoyesteVerdi);

var tall = 42; // Eksempelvis tallet du ønsker å lete etter
var antallForekomster = tellAntall(tall, array);
console.log("Antall forekomster av " + tall + " i arrayen er: " + antallForekomster);
