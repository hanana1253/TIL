function sum(...args){
    var result = 0;
    for (var i = 0; i < args.length; i++){
        result = result + args[i];
    }   
    return result;
}

console.log(sum(1, 2, 3, 4));