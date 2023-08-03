const btn1 = document.querySelector('.btn1'); 
const btn2 = document.querySelector('.btn2'); 
const body = document.body; 
const user = document.querySelector('.user'); 
const inp1 = document.getElementById('pollutant');
const inp2 = document.querySelector('.reflectedHeader'); 
const inp3 = document.querySelector('#headerVal'); 

// Click Event Listener for Pollute Button
btn2.addEventListener('click', () => {
    // const headerVal = JSON.stringify(inp1.value); 
    const pollutant = inp1.value; 
    console.log(`Value of the pollutant is: ${pollutant}`); 
    if (pollutant) {
        // Payload => {"__proto__": {"x-someheader":"red"}}; {"__proto__": {"x-someheader":"<img src=x onerror=alert(1)>"}} 
        let pollutedObj = recursiveMerge({}, JSON.parse(pollutant)); 
    } else {
        console.log('No value to pollute!'); 
        alert('Enter some value to pollute prototype with!'); 
    }
    console.log(`Object Prototype is: ${Object.prototype}`); 
})

// Click Event Listener for Fetch button. 
btn1.addEventListener('click', () => {
    let x = getRandomPos();         // Get a random value to fetch data from the API. 
    let url = `planet/position/${x}`;
    const headerVal = inp3.value; 
    let reflected = {};         // Empty Object Literal without properties being initialized. First Mistake. 
    let header = {}; 

    // Send X-SomeHeader in Request only if a value is present in the box to be sent. 
    headerVal? header = {
        "Content-type": "application/text",
        "X-SomeHeader": `${headerVal}`
    } : header = {
        "Content-type": "application/text",
    }; 

    console.log(`URL is: ${url}`); 

    fetch(url, {
        headers: header
    })
    .then( (response) => {
        // This if block assigns value to reflected Object only if X-SomeHeader is present. 
        // If someone pollutes global Object prototype, they will still be able to provide x-someheader value to reflected Object. 
        if (response.headers.get('X-SomeHeader')) {
            reflected['x-someheader'] = response.headers.get('X-SomeHeader'); 
        }
        console.log(`Reflected Data is: ${reflected['x-someheader']}`); 
        return response.text()
    })
    .then( (data) => {
        // Here, innerHTML is being used which is a notorious sink for DOM XSS. 
        inp2.innerHTML = reflected['x-someheader'];
        // console.log(inp2); 
        const outDiv = document.createElement('div'); 
        outDiv.innerHTML = data;
        console.log(data); 
        body.append(outDiv); 
    })
    .catch ( (err) => {
        console.log(err); 
    })
})

function recursiveMerge(dst, src) {
    for (let i in src) {
        console.log('Evaluating property: ', i); 
        if (typeof dst[i] == 'object' && typeof src[i] == 'object') {
            recursiveMerge(dst[i], src[i]); 
        } else {
            dst[i] = src[i];            
        }
    }
    return dst; 
}

function getRandomPos() {
    let a = Math.ceil(1);   //Lower Count of position
    let b = Math.floor(10);     // Exclusive upper count

    return Math.floor(Math.random()*(b-a) + a); 
}
