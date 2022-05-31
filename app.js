import express from 'express';
import path from 'path';
import {spawn} from 'child_process';

let app = express()

app.set('view engine', 'ejs');
app.use(express.static(path.resolve() + '/public'))

app.get('/', function(req, res){
    console.log(req.query)
    const stemming = spawn('python3', ['-u', path.resolve() + 'deps/stem.py', req.query.q])
    stemming.stdout.on('data', (data)=>{
        res.render('index.ejs', {stemmed: data, query: req.query.q})
    });
});

app.listen(3000);

export default app;