const express = require('express'); 
const path = require('path'); 
const fs = require('fs'); 

const app = express();
app.set('view engine', 'pug'); 
app.use(express.static(path.join(__dirname, 'public'))); 
app.use(express.urlencoded( {extended: true} )); 
app.use(express.json()); 

const data = JSON.parse(fs.readFileSync(`${__dirname}/public/planets.txt`, { encoding: 'utf-8' }));

// Main Route where we handle Client Side Prototype Pollution. 
app.get('/', (req, res) => {
    const paramsObj = req.params; 
    res.render('main'); 
})

// Route where we handle Server Side Prototype Pollution. 
app.get('/server', (req, res) => {
    res.render('server'); 
})

// API Route for GET requests. For Client Side. 
app.get('/planet/position/:pos', (req,res) => {
    if (req.params.pos <1 || req.params.pos > 9) {
        res.send('Please Enter a valid Planet Position in our Solar System!'); 
        return; 
    }

    console.log(JSON.stringify(req.headers));
    const pos = req.params.pos; 
    const x = data[pos-1].name; 

    // Check if x-someheader is present or not. 
    let userHeader = ''; 
    if ('x-someheader' in req.headers) {
        userHeader = req.headers['x-someheader'];
    }  
    if (userHeader) {
        res.set( {
            "X-SomeHeader": userHeader
        }); 
    }
    res.send(x); 
})

// API Request for POST requests. For Server Side. 
app.post('/planet/position/:pos', (req, res) => {
    const reqBody = JSON.stringify(req.body);       // Make sure the Header Content-Type is set to application/json 
    let userObj = {};
    let workObj = {}; 
    const testObj = {
        color: "red", 
        taste: "salty"
    }; 

    console.log(reqBody); 
    console.log("Object Prototype before pollution: ",Object.prototype); 
    // Pollution Payload => {"__proto__":{"isPolluted":true}}

    userObj = recursiveMerge(workObj, JSON.parse(reqBody));
    console.log(userObj); 
    console.log(Object.prototype); 
    console.log(`Testing testObj for isPolluted property: ${testObj.isPolluted}`);
})

// A recursive merge function that sets up the Prototype Pollution Vulnerability. 
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

module.exports = app; 