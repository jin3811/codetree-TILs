const fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')[1].split(' ')

console.log(input.map(x => Math.abs(x))
                 .join(' '))