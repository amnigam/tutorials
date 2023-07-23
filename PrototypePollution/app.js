const express = require('express'); 
const path = require('path'); 
const fs = require('fs'); 

const app = express();
app.set('view engine', 'pug'); 
app.use(express.static(path.join(__dirname, 'public'))); 
app.use(express.urlencoded( {extended: true} )); 

const data = JSON.parse(fs.readFileSync(`${__dirname}/public/planets.txt`, { encoding: 'utf-8' }));
console.log(data);

app.get('/', (req, res) => {
    res.render('main'); 
})

app.get('/planet/position/:pos', (req,res) => {
    if (req.params.pos <1 || req.params.pos > 9) {
        res.send('Please Enter a valid Planet Position in our Solar System!'); 
        return; 
    }

    const pos = req.params.pos; 
    const x = data[pos-1].name; 
    res.send(x); 

})


module.exports = app; 