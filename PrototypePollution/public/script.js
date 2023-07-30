const btn = document.querySelector('button'); 
const body = document.body; 
const user = document.querySelector('.user'); 
const reqData = document.getElementById('bodyData'); 
// const inp1 = document.getElementById('headerName');
const inp2 = document.getElementById('headerVal'); 

function getRandomPos() {
    let a = Math.ceil(1);   //Lower Count of position
    let b = Math.floor(10);     // Exclusive upper count

    return Math.floor(Math.random()*(b-a) + a); 
}

btn.addEventListener('click', () => {
    let x = getRandomPos(); 
    // let url = `http:/localhost:3000/planet/position/${x}`; 
    let url = `planet/position/${x}`;
    // const headerName = inp1.value; 
    const headerVal = inp2.value; 
    const bodyData = reqData.value; 

    let reflectedHeader = ''; 
    let header = {}; 

    headerVal? header = {
        "Content-type": "application/text",
        "X-SomeHeader": `${headerVal}`
    } : header = {
        "Content-type": "application/text"
    }; 

    console.log(url); 
    // console.log(header); 
    console.log(bodyData); 

    if (!bodyData) {
        fetch(url, {
            headers: header
        })
        .then( (response) => {
            reflectedHeader = response.headers.get('X-SomeHeader'); 
            return response.text()
        })
        .then( (data) => {
            const userDiv = document.createElement('div'); 
            userDiv.innerHTML = reflectedHeader;
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
    } else {
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
            console.log(err); 
        })
    }
})
    