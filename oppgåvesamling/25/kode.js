
console.log(Math.random());

console.log(getRandomIntInclusive(1,20));

let tilfeldigTall = getRandomIntInclusive(1,20);
console.log(tilfeldigTall);

// kilde: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random
function getRandomIntInclusive(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1) + min); // The maximum is inclusive and the minimum is inclusive
  }

let arrayTilfeldigeTall = [];

for (let i = 0; i <= 100; i++) {
    arrayTilfeldigeTall[i] = getRandomIntInclusive(1,20);
}

console.log(arrayTilfeldigeTall)
console.table(arrayTilfeldigeTall)

let antallTiere = 0;
let antallOverTi = 0;
let sum = 0;

for (let i = 0; i < arrayTilfeldigeTall.length; i++) {
    if (arrayTilfeldigeTall[i] === 10) {
        antallTiere++;
    }

    if (arrayTilfeldigeTall[i] > 10) {
        antallOverTi++;
    }

    sum = sum + arrayTilfeldigeTall[i];
}

let utskrift = document.getElementById("utskrift");
utskrift.innerHTML = "<li>Antall 10-ere: " + antallTiere; + "</li>"
utskrift.innerHTML += "<li>Antall over 10-ere: " + antallOverTi; + "</li>"