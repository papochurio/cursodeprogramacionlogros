function menu() {
    console.log("1- sumar")
    console.log("2- restar")
    console.log("3- multiplicar")
    console.log("4- division")
    console.log("5- salir")
}

function realizaroperaciones(opcion, numero1, numero2) {
    switch (opcion) {
        case "1":
            console.log(numero1 + numero2);
            break;
        case "2":
            console.log(numero1 - numero2);
            break;
        case "3":
            console.log(numero1 * numero2);
            break;
        case "4":
            console.log(numero1 / numero2);
            break;
        
        default:
            console.log("numero invalido, vuelve a intentar")
    }
}


function calculadora() {
    const readline = require("readline");
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    
    menu();
    
    rl.question("seleccione una opcion: ", (opcion) => {
        if (opcion === "5") {
            console.log("¡ADIOS!");
            rl.close();
            return;
        }
            rl.question("escribe un numero: ", (input1) => {
                const numero1 = parseFloat(input1);
            
            rl.question("escribe un numero: ", (input2) => {
                const numero2 = parseFloat(input2);
                    
                const resultado = realizaroperaciones(opcion, numero1, numero2);
                
                console.log("resultado: " + resultado);
               
                   
                rl.close();
            });
        });
    });
} 
calculadora();
