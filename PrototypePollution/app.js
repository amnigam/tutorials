const express = require('express'); 
const path = require('path'); 
const fs = require('fs'); 
const { hostname } = require('os');

const app = express();
app.set('view engine', 'pug'); 
app.use(express.static(path.join(__dirname, 'public'))); 
app.use(express.urlencoded( {extended: true} )); 

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

    // const headers = JSON.parse(req.headers); 
    console.log(req.headers); 
    console.log(req.hostname); 

    const pos = req.params.pos; 
    const x = data[pos-1].name; 
    const userHeader = req.headers['x-someheader']; 
    res.set( {
        "X-SomeHeader": userHeader
    }
    ); 
    res.send(x); 

})


module.exports = app; 