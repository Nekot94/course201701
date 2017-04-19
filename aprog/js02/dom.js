// alert('Андрей');
console.log('Андрей');
document.body.firstElementChild.innerHTML = 'Андрей';
console.log(document.body.lastElementChild.tagName);
console.log(document.body.lastElementChild.previousElementSibling);
document.getElementById('i1').innerHTML = 'Не Андрей';
document.getElementsByClassName('j2')[0].style.color = "red";
document.getElementsByClassName('j2')[0].style.backgroundColor = "wheat";
var elem = document.getElementsByTagName("div");

for(var i = 0; i<elem.length; i++){
	elem[i].setAttribute("title", "AMIN");

}
function donate(){
	while (true){
		alert("ГАНИ БАБКИ");
	}
}
function game(object){
	object.style.height = "10000px";
}


