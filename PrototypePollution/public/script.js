const btn = document.querySelector('button'); 
const body =document.body; 

function getRandomPos() {
    let a = Math.ceil(1);   //Lower Count of position
    let b = Math.floor(10);     // Exclusive upper count

    return Math.floor(Math.random()*(b-a) + a); 
}

btn.addEventListener('click', () => {
    let x = getRandomPos(); 
    // let url = `http:/localhost:3000/planet/position/${x}`; 
    let url = `planet/position/${x}`;

    console.log(url); 
    fetch(url)
    .then( (response) => response.text())
    .then( (data) => {
        const outDiv = document.createElement('div'); 
        outDiv.innerHTML = data; 
        console.log(data); 
        body.append(outDiv); 
    })
    .catch ( (err) => {
        console.log(err); 
    })
})