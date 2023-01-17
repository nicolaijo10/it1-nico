let person1 =  {navn: "Jamal" , alder: 19 , aktivitet1: 0 , aktivitet2: 0, aktivitet3: 0, resultat: 0};
let person2 =  {navn: "Ali" , alder: 21 , aktivitet1: 0 , aktivitet2: 0, aktivitet3: 0, resultat: 0};
let person3 =  {navn: "Jonas" , alder: 89 , aktivitet1: 0 , aktivitet2: 0, aktivitet3: 0, resultat: 0};
let person4 =  {navn: "Erna" , alder: 60 , aktivitet1: 0 , aktivitet2: 0, aktivitet3: 0, resultat: 0};
let person5 =  {navn: "Jesus" , alder: 70 , aktivitet1: 0 , aktivitet2: 0, aktivitet3: 0, resultat: 0};

let personData = [person1, person2, person3, person4, person5]

console.log(personData[1].navn);
console.log(personData[1].alder);

for (let j = 0; j < personData.length; j++) {
    console.log(personData[j].navn);
    console.log(personData[j].alder);  
};


//Forms 3

const skjema = document.getElementById("skjemaRegistrering")

skjema.addEventListener("submit", registerBruker);

function registerBruker(evt) {
    evt.preventDefault();
    let nyttNavn = document.getElementById("#inpNavn").value;
    let nyttAlder = document.getElementById("#inpAlder").value;
    
    // Oppretter et objekt fra input
    let objBruker = {
        Navn : nyttNavn,
        Alder : nyttAlder,
        Aktivitet1 : nyAktivitet1,
        Aktivitet2 : nyAktivitet2,
        Aktivitet3 : nyAktivitet3
    };
    personData.push(objBruker);
    console.log(personData); //sjekker om obj ble lagt til

    //utskrift til HTML
    let ut = "<li>" + nyttNavn + ", " + nyttAlder + "</li>";
    document.getElementById("utskrift").innerHTML += ut;
};


//forms Aktiviteter
/*
const Aktiviteter = document.getElementById("AktivitetRegistrering")

Aktiviteter.addEventListener("submit", registrerPoeng)

function registrerPoeng(poengEvt) {
    poengEvt.preventDefault();
    let navn = document.querySelector("#navnOpptater").value;
    let nyPoeng1 = document.querySelector("#akt1").value;
    let nyPoeng2 = document.querySelector("#akt2").value;
    let nyPoeng3 = document.querySelector("#akt3").value;


};
*/

function poengRegning() {
    let Poeng1 = personData[personNr].aktivitet1
    let Poeng2 = personData[personNr].aktivitet2
    let Poeng3 = personData[personNr].aktivitet3

    let nyPoeng1 = document.querySelector("#akt1").value;
    let nyPoeng2 = document.querySelector("#akt2").value;
    let nyPoeng3 = document.querySelector("#akt3").value;
};