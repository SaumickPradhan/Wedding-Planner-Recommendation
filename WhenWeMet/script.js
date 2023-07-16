var budget = document.getElementById('budget').value;
var Tier = document.getElementById('Tier').value;
var Event_Theme = document.getElementById('Event_Theme').value;
var num_people = document.getElementById('num_people').value;
var Cuisine = document.getElementById('Cuisine').value;
var Dietary_resctriction = document.getElementById('Dietary_resctriction').value;
var Genre = document.getElementById('Genre').value;
var Dress_Type = document.getElementById('Dress_Type').value;

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