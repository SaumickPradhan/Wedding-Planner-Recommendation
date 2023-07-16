var Tier = document.getElementById('Tier').value;

document.querySelector('button').addEventListener('click',function clickHandler(e){

    this.removeEventListener('click',clickHandler,false);

    e.preventDefault();
    var self = this;
    setTimeout(function(){
        self.className = 'loading';
    },125);

    setTimeout(function(){
        self.className = 'ready';
    },4300);
},false);

document.getElementById("myButton").onclick = function() {
    setTimeout(function() {
        window.location.href = '../Recommendation_Page/index.html';
    }, 5000); // 3000ms = 3s delay
};
