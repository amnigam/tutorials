const btn = document.querySelector('button'); 
const reqData = document.getElementById('bodyData'); 

function getRandomPos() {
    let a = Math.ceil(1);   //Lower Count of position
    let b = Math.floor(10);     // Exclusive upper count

    return Math.floor(Math.random()*(b-a) + a); 
}

btn.addEventListener('click', () => {
    let x = getRandomPos(); 
    // let url = `http:/localhost:3000/planet/position/${x}`; 
    let url = `planet/position/${x}`;
    const bodyData = reqData.value; 

    console.log(`URL is: ${url}`); 
    console.log(`Request Body Data is: ${bodyData}`); 

    fetch(url, {
        method: 'POST',
        body: `${bodyData}`,
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then ( (response) => {
        return response.json()
    })
    .then ( (data) => {
        console.log('done!'); 
    })
    .catch ( (err) => {
        console.log("FETCH errored out!"); 
        console.log(err); 
    })
})
