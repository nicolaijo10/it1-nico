fetch('https://randomuser.me/api/?results=10')
	.then(response => response.json())
	// .then(response => console.log(response))
    .then(response => behandleSvar(response))
	.catch(err => console.error(err));

function behandleSvar(svar) {
    
    for (let j = 0; j < svar.results.length; j++) {
        console.log(j)
        // Testing
        console.log(svar);
        console.log("Navn: " + svar.results[j].name.first);
        console.log("Epost: " + svar.results[j].email);
        console.log("Bilde: " + svar.results[j].picture.large);

        // HTML-visning
        let navn = document.createElement("p");
        navn.innerText = "Navn: " + svar.results[j].name.first;
        let epost = document.createElement("p");
        epost.innerText = "Epost: " + svar.results[j].email;
        let bilde = document.createElement("img");
        bilde.src = svar.results[j].picture.large;
        document.querySelector("#utskrift").appendChild(navn);
        document.querySelector("#utskrift").appendChild(epost);
        document.querySelector("#utskrift").appendChild(bilde);
    }
}