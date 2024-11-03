var fs =require('fs');

var inname = './output.txt';
var outname = './output2.txt';

fs.exists(outname, function(exists){
    if(exists){
        fs.unlink(outname, function(err){
            if(err) throw err;
            console.log('delete' + outname);
        });
    }
    var infile = fs.createReadStream(inname, {flag:'r'});
    var outfile = fs.createWriteStream(outname, {flags:'w'});
    infile.pipe(outfile);
    console.log('copy' + inname + ' -> ' + outname);    
});