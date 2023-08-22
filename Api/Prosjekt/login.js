let deltakere = [
    { navn: "Ole",
      email: "ole1203@gmail.com", 
      fodselsaar: 2005 },
    { navn: "Iben", 
      email: "iben2005965@gmail.com", 
      fodselsaar: 2002 },
    { navn: "Martin", 
      email: "martinint8123@gmail.com", 
      fodselsaar: 1995 },
    { navn: "Jesper", 
      email: "jesper9759023@gmail.com", 
      fodselsaar: 1980 },
    { navn: "Aleksander", 
      email: "aleks95892@gmail.com", 
      fodselsaar: 2003 },
    { navn: "Samuel", 
      email: "samu2839@gmail.com", 
      fodselsaar: 2000 }
  ];

let resultatListe = [
  { navn: "team1",
    poeng: 561}
]

resultatListe.sort(poeng)

// knappEl.addEventListener("click", meldPaa);

document.getElementById("skjemaRegistrer").addEventListener("submit", meldPaa)

document.getElementById("folk")

for (let index = 0; index < array.length; index++) {
  const element = array[index];
  
}

function meldPaa(evt) {
    evt.preventDefault();
    console.log(document.getElementById("navn").value);
    console.log(document.getElementById("email").value);
    console.log(document.getElementById("fodselsaar").value);

    let obj = {
        navn : document.getElementById("navn").value,
        email : document.getElementById("email").value,
        fodselsaar : document.getElementById("fodselsaar").value
    }

    let alder = 2023 - obj.fodselsaar

    console.log(alder)

    if (alder < 16 || alder > 70) {
      alert("Alderen din er ikke bra nok")
      return
    }

    deltakere.push(obj);
}

console.log(deltakere);

