//con un minuto
const startingMinutes = 1;
let time = startingMinutes*60;
var tiempo = document.getElementById('tiempo').value;
console.log("tiempo -> ", startingMinutes);
console.log("tiempo en span-> ",  document.getElementById('countdown'));

console.log("tiempo en span-> ",  document.getElementById('tiempo'));


console.log("tiempo en tiempo -> ",  tiempo);




console.log("timesss !");

const countdownEl = document.getElementById('countdown');


setInterval(UpdateCountdown, 1000);

function UpdateCountdown(){
    const minutes = Math.floor(time/60);
    let seconds = time % 60;


    seconds = seconds < 10 ? '0' + seconds : seconds;

    countdownEl.innerHTML = `${minutes} : ${seconds}`;
    time--;
    time = time < 0 ? 0 : time; 
    if(time<=0){
        console.log("se acabo tu tiempo cunt");        

        document.getElementById('submit').click();
            
    }
    if (time<=30){
        document.getElementById('countdown').className ='animacion';
    }
}
