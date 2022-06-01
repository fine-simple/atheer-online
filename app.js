import express from 'express';
import path from 'path';
import {exec, spawn} from 'child_process';
import livereload from 'livereload';
import connectLiveReload from 'connect-livereload';

const PORT = process.env.PORT || 3000;

let app = express()

if(process.env.LIVERELOAD){
    const liveReloadServer = livereload.createServer();
    liveReloadServer.server.once("connection", ()=>{
        setTimeout(()=>{
            liveReloadServer.refresh("/");
        }, 100);
    });
    app.use(connectLiveReload());
}

app.set('view engine', 'ejs');
app.use(express.static(path.resolve() + '/public'))

app.get('/public/favicon.ico', (req, res)=> {
    res.sendFile(path.resolve() + '/public/favicon.ico');
});

app.get('/', (req, res) => {    
    if(!req.query.q)
    {
        res.render('index.ejs', {stemmed: "", query: ""});
        return;
    }

    // trim query
    let q = req.query.q.trim();
    
    // stem type
    let stemType = "stem";
    if(req.query.type)
        stemType= req.query.type.toLowerCase().trim();

    const stemming = spawn('python3', ['-u', path.resolve() + '/deps/stem.py', q, stemType])
    
    stemming.stdout.on('data', (data)=>{
        res.render('index.ejs', {stemmed: data, query: q})
    });
});

app.get("/gitpull", (req, res)=>{
    exec(`cd '${path.resolve()}' && git pull`)
    res.redirect("/");
});

app.listen(PORT);

export default app;