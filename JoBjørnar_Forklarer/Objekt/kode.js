let personer = [
    { navn: "Nicolai", fodselsaar: 2005 },
    { navn: "Lars"   , fodselsaar: 1957 }
];

console.log(personer[0].navn);

// 1
for(let person of personer) {
    console.log(person.navn)
}

//2 
for(let i = 0; i < personer.length; i++) {
    console.log(personer[i].navn);
}