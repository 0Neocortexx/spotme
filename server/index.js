const express = require('express');
const app = express();
const path = require('path');
const router = express.Router();

// Instalar o express na aplicação: npm install --save express

router.get('/', function(req,res) {
    // sendFile = render_template
        res.sendFile(path.join('/home/jonathan/spotme/public/index.html'));
    })

app.use('/', router);
app.listen(process.env.port | 3000);
console.log("Testa lá ...")