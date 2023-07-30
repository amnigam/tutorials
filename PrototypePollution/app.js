const express = require('express'); 
const path = require('path'); 
const fs = require('fs'); 

const app = express();
app.set('view engine', 'pug'); 
app.use(express.static(path.join(__dirname, 'public'))); 
app.use(express.urlencoded( {extended: true} )); 
app.use(express.json()); 

const data = JSON.parse(fs.readFileSync(`${__dirname}/public/planets.txt`, { encoding: 'utf-8' }));
console.log(data);

app.get('/', (req, res) => {
    const paramsObj = req.params; 
    console.log(`Parameters Object: `, paramsObj); 
    res.render('main', {
        ua: req.headers['user-agent']
    }); 
})

app.get('/planet/position/:pos', (req,res) => {
    if (req.params.pos <1 || req.params.pos > 9) {
        res.send('Please Enter a valid Planet Position in our Solar System!'); 
        return; 
    }

    console.log(req.headers); 
    const pos = req.params.pos; 

    const x = data[pos-1].name; 
    const userHeader = req.headers['x-someheader']; 

    if (userHeader) {
        res.set( {
            "X-SomeHeader": userHeader
        }
        ); 
    }
    res.send(x); 
})

app.post('/planet/position/:pos', (req, res) => {
    const reqBody = JSON.stringify(req.body);       // Make sure the Header Content-Type is set to application/json 
    let userObj = {};
    let workObj = {}; 

    console.log(reqBody); 
    userObj = recursiveMerge(workObj, JSON.parse(reqBody));
    console.log(userObj); 
    console.log(Object.prototype); 
    console.log(workObj.weight);


})

function recursiveMerge(dst, src) {
    for (let i in src) {
        console.log('Evaluating property: ', src[i]); 
        if (typeof dst[i] == 'object' && typeof src[i] == 'object') {
            recursiveMerge(dst[i], src[i]); 
        } else {
            dst[i] = src[i];            
        }
    }
    return dst; 
}

module.exports = app; 