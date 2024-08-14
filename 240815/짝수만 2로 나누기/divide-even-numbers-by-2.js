const fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

console.log(input[1].split(' ')
                    .map(x => parseInt(x))
                    .map(x => x % 2 == 0 ? x / 2 : x)
                    .join(' '))