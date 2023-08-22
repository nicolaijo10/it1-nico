
// Oppgave 11, Skrive tall opp til 50 med while-løkke
let teller = 0;

while (teller <= 50) {
    console.log(teller);
    teller++;

}

// Oppgave 12, Skrive tall opp til 50 med for-løkke
for (let i = 0; i <= 50; i++) {
    console.log(i);

}

// Oppgave 13, 3 gangen opp til 999
for (let i = 0; i < 1000; i+=3) {
    console.log(i);

}

//Oppgave 14, Partall mellom 1 og 100
for (let i = 2; i <= 100; i+=2) {
    console.log(i);

}

//Oppgave 15, Summer alle tallen fra 1 til 100
let sum = 0;

for (let i = 1; i <= 100; i++) {
    sum += i;
    console.log(sum)
}

//Oppgave 16, ## tekst
let tekst = "";

for (let i = 0; i < 4; i++) {
    tekst += "#";
    console.log(tekst);

}

