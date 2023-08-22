// Oppgave 1
const pris = document.getElementById("pris");
pris.innerHTML = 500

const pris2 = document.getElementById("pris2");
pris2.innerHTML = 500

const pris3 = document.getElementById("pris3");
pris3.innerHTML = 500

const pris6 = document.getElementsByClassName("pris6");
pris6.innerHTML = 500

// Forsøker her å gjøre det for alle på en effektiv måte
const allePriser = document.querySelectorAll('span')
console.log(allePriser)

//Oppgave 2
// Koden i oppgave 2A lager først en variabel som heter terning
// Variabelen blir satt som 0 og så lager de en løkke under
// løkken sier at så lenge "terning" ikke er lik 6
// så vil "terning" være det samme som et tilfeldig tall mellom 0 og 6
// Etter det så logger de den og du får et tilfeldig tall i consollen mellom 0 og 6
// Koden stopper når du triller tallet 6

let antallTerningKast = 0;

let terning = 0;

while (terning != 6) {
    terning = Math.floor(Math.random() * 6) + 1;
    console.log(terning);
    antallTerningKast++;
    //console.log(antallTerningKast);
}


if (antallTerningKast > 4) {
    console.log("Uflaks!")
} else if (antallTerningKast < 3) {
    console.log("Flaks")
} else if (antallTerningKast == 3 || antallTerningKast == 4) {
    console.log("Som forventet")
}


//Oppgave 3
//Forsøker først å bruke prompt til å lage

let bVerdi = parseInt(prompt("Velg B verdi"))

let hVerdi = parseInt(prompt("Velg H verdi"))

let aVerdi = parseInt(prompt("Velg A verdi"))


console.log(bVerdi)
console.log(hVerdi)
console.log(aVerdi)


function regnUt() {
    verdi = (aVerdi + bVerdi) * hVerdi/2
    console.log(verdi)
}

regnUt.call()

//Så kan vi prøve med input felt
let inputFelt = document.getElementById('inputA')
console.log(inputFelt.number)


//Oppgave 4 
let tilfeldig = Math.floor(Math.random() * 150) + 1;
let tilfeldig2 = Math.floor(Math.random() * 150) + 1;


const danMarksPlass = []
const solHeimsViken = []

for (let i = 0; i < 1440; i++){
    tilfeldig = Math.floor(Math.random() * 150) + 1;
    tilfeldig2 = Math.floor(Math.random() * 150) + 1;
    danMarksPlass.push(tilfeldig);
    solHeimsViken.push(tilfeldig2);
}

console.log(tilfeldig)
console.log(solHeimsViken)
console.log(danMarksPlass)


//B

const average = danMarksPlass.reduce((a, b) => a + b, 0) / danMarksPlass.length;
console.log("Danamrksplass sin gjennomsnittsumm er " +  average);

const average2 = solHeimsViken.reduce((a, b) => a + b, 0) / solHeimsViken.length;
console.log("Solheimsviken sin gjennomsnittsumm er " +  average2);

console.log(Math.max(...danMarksPlass));
console.log(Math.max(...solHeimsViken));
console.log(Math.min(...danMarksPlass));
console.log(Math.min(...solHeimsViken));

console.log("Den høyeste verdien er funnet begge steder og er 150. Den laveste verdien er også funnet begge steder og er 1")

// C

var filteredDanmarks = danMarksPlass.filter(item => item < 141);
var filteredSolheim = solHeimsViken.filter(item => item < 141);

console.log(filteredDanmarks);
console.log(Math.max(...filteredDanmarks));
console.log(filteredSolheim);
console.log(Math.max(...filteredSolheim));