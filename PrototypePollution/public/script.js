const btn = document.querySelector('button'); 
const body = document.body; 
const user = document.querySelector('.user'); 
const inp = document.querySelector('input'); 

function getRandomPos() {
    let a = Math.ceil(1);   //Lower Count of position
    let b = Math.floor(10);     // Exclusive upper count

    return Math.floor(Math.random()*(b-a) + a); 
}

btn.addEventListener('click', () => {
    let x = getRandomPos(); 
    // let url = `http:/localhost:3000/planet/position/${x}`; 
    let url = `planet/position/${x}`;
    // const fetchPollution = inp.innerText; 
    const fetchPollution = inp.value; 
    console.log(fetchPollution);
    let userAgent = ''; 
    let header = {}; 

    fetchPollution? header = {
        "Content-type": "application/text",
        "X-SomeHeader": fetchPollution
    } : header = {
        "Content-type": "application/text"
    }; 

    console.log(url); 
    fetch(url, {
        headers: header
    })
    .then( (response) => {
        userAgent = response.headers.get('X-SomeHeader'); 
        return response.text()
    })
    .then( (data) => {
        const userDiv = document.createElement('div'); 
        userDiv.innerHTML = userAgent;
        // body.append(userDiv); 
        user.append(userDiv); 

        const outDiv = document.createElement('div'); 
        outDiv.innerHTML = data;
        console.log(data); 
        body.append(outDiv); 
    })
    .catch ( (err) => {
        console.log(err); 
    })
})