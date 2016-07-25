var page = require('webpage').create();
system = require('system');
var fs = require('fs');// File System Module

var args = system.args;
var url = args[1];    // 대상 webpage url
var output = args[2]; // 저장할 파일이름, path for saving the local file 

page.open( url, function() { // open the file 
  fs.write(output,page.content,'w'); // Write the page to the local file using page.content
  phantom.exit(); // exit PhantomJs
});