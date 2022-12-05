const countries = ['Norge', 'Japan', 'USA', 'Italia', 'Canada', 'Russland', 'Sør-Korea', 'Kina']
const places = ['Lillehammer', 'Nagano', 'Salt Lake City', 'Torino', 'Vancouver', 'Sotsji', 'Pyeongchang', 'Beijing']
const years = [1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022]

let theYear = -1
let countTrials = 0
let countCorrect = 0;
let elQuestion = document.getElementById('question')
let btnCheck = document.getElementById('checkBtn')
let btnNew = document.getElementById('newBtn')
let elAnswer = document.getElementById('answer')
let elScore = document.getElementById('score')
btnNew.addEventListener("click",newQuestion)
btnCheck.addEventListener("click",checkAnswer)

function skrivUt() {
    for (let i = 0; i < countries.length; i++){
        console.log("Vinter-OL i " + years[i] + " ble arrangert i " +  places[i] + " i " + countries[i])
    }
}

skrivUt.call();


//Initialiserer siden med å generere nytt spørsmål
newQuestion()


//Generer nytt spørsmål og legger det ut på siden
function newQuestion() {
   theYear = getRandomYear();
   countTrials++;
   elQuestion.innerHTML = 'Hvor ble OL arrangert året ' + theYear + '?'
   elAnswer.style.backgroundColor = 'white'
   elAnswer.value = ''
}

//Sjekker om svaret er rett og oppdaterer scoen
function checkAnswer(){
    let answer = elAnswer.value;
    if (answer == whichPlace(theYear)) {
        elAnswer.style.backgroundColor = 'green'
        countCorrect++;
    }
    else {
        elAnswer.style.backgroundColor = 'red'  
    }

    elScore.innerHTML = 'Din score: ' + countCorrect + ' : ' + countTrials
}
function whichPlace(year) {
    let idx = years.indexOf(year)
    return places[idx]
}

function whichYear(place) {
    let idx = places.indexOf(place)
    return years[idx]
} 

function getRandomYear() {
    let randomYear = years[Math.floor(Math.random() * years.length)];
    return randomYear
}