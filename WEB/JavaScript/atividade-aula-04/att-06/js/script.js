var soma = 0
var quant_impar = 0
var quant_par = 0


for (num=1; num<=10; num++){
    if (num% 2 == 0){
        quant_par += 1
    } else {
        quant_impar += 1
    }
};
console.log(`Impar ${quant_impar}`)
console.log(`Par ${quant_par}`)