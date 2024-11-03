var fs = require('fs');
fs.mkdir('./docs',0666,function(err){
    if(err) throw err;
    console.log('folder docs made');
    
    fs.rmdir('./docs',function(err){
        if(err) throw err;
        console.log('folder docs delete');
    });
});